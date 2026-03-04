from selenium.webdriver.common.by import By
from BaseLayer.executorBase import ExecutorBase
from PageObjects.Common.siteHeader import SiteHeader
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class Image_listPage(SiteHeader,ExecutorBase):
    
    def Image(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/aside/div/ul/li[3]')
    
    def Image_Attr(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[2]/div/div/div/input')
    
    def Audo_Mode(self): 
        return self.get_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    
    def Manual_Mode(self):
        return self.get_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[2]')
    
    def Brightness(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[3]/div/div[1]/div/div/div[1]/div/input')
    
    def Saturation(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[3]/div/div[2]/div/div/div[1]/div/input')
    
    def Contrast(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[3]/div/div[3]/div/div/div[1]/div/input')
    
    def Sharpness(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[3]/div/div[4]/div/div/div[1]/div/input')
    
    def ldc(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[4]/div/div/span')

    def X_Ratio(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div[2]/div/div/div[1]/div/input')

    def Y_Ratio(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div[3]/div/div/div[1]/div/input')

    def Distortion_Ratio(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div[5]/div/div/div[1]/div/input')
    
    def Keep_Aspect_Ratio(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div[1]/div/div/span')

    def XY_Ratio(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div[4]/div/div/div[1]/div/input')

    def ok(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/main/div/section/main/div/form/div[7]/div/button')
    
    def set_image(self):
        """设置图片参数"""
        actions = [
            ("点击图片管理", self.Image, self._click_element),
            ("点击图片属性", self.Image_Attr, self._click_element),
            ("切换到手动模式", self.Manual_Mode, self._click_element),
            ("设置亮度", self.Brightness, lambda el: self._send_keys_to_input(el, "100")),
            ("设置饱和度", self.Saturation, lambda el: self._send_keys_to_input(el, "100")),
            ("设置对比度", self.Contrast, lambda el: self._send_keys_to_input(el, "100")),
            ("设置锐度", self.Sharpness, lambda el: self._send_keys_to_input(el, "100")),
            ("打开LDC设置", self.ldc, self._click_element),
            ("设置X比例", self.X_Ratio, lambda el: self._send_keys_to_input(el, "100")),
            ("设置Y比例", self.Y_Ratio, lambda el: self._send_keys_to_input(el, "100")),
            ("设置畸变比例", self.Distortion_Ratio, lambda el: self._send_keys_to_input(el, "10000")),
            ("启用保持比例", self.Keep_Aspect_Ratio, self._click_element),
            ("设置XY比例", self.XY_Ratio, lambda el: self._send_keys_to_input(el, "100")),
            ("确认设置", self.ok, self._click_element),
            
            ("点击图片属性", self.Image_Attr, self._click_element),
            ("切换到自动模式", self.Audo_Mode, self._click_element),
            ("关闭LDC设置", self.ldc, self._click_element),
            ("确认设置", self.ok, self._click_element)
        ]
        
        for action_name, element_func, action_func in actions:
            try:
                element = element_func()
                if element:
                    action_func(element)
                    self.logger.info(f"✅ {action_name} 成功")
                else:
                    self.logger.warning(f"⚠️ {action_name} 元素未找到，跳过")
            except (NoSuchElementException, ElementClickInterceptedException) as e:
                self.logger.error(f"❌ {action_name} 失败: {str(e)}")
            except Exception as e:
                self.logger.error(f"❌ {action_name} 发生异常: {str(e)}")
        
        self.logger.info("✨ 图片设置流程完成（部分步骤失败已跳过）")