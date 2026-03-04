from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from BaseLayer.executorBase import ExecutorBase
from PageObjects.Common.siteHeader import SiteHeader

class VideolistPage(SiteHeader, ExecutorBase):

    OPERATION_SLEEP = 1.0
    VIDEO_MENU_XPATH = '//*[@id="app"]/div/section/main/div/section/aside/div/ul/li[6]'
    MAIN_STREAM0_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/div[2]/form/div[2]/div/div/span'
    MAIN_STREAM0_ENCODE_TYPE_XPATH = '//*[@id="rc_encoder_type_0"]/div/div[1]/input'
    STREAM0_H264_XPATH = '//*[@id="rc_encoder_type_content_0"]/li[1]'
    STREAM0_H265_XPATH = '//*[@id="rc_encoder_type_content_0"]/li[2]'
    MAIN_STREAM0_RESOLUTION_XPATH = '//*[@id="resolution_opt_0"]/div/div[1]'
    RESOLUTION_MAP = {
        "2560x1440": '//*[@id="resolution_opt_content_0"]/li[1]',
        "2048x1536": '//*[@id="resolution_opt_content_0"]/li[2]',
        "2304x1296": '//*[@id="resolution_opt_content_0"]/li[3]',
        "2240x1256": '//*[@id="resolution_opt_content_0"]/li[4]',
        "1920x1080": '//*[@id="resolution_opt_content_0"]/li[5]',
        "1280x960": '//*[@id="resolution_opt_content_0"]/li[6]',
        "1280x720": '//*[@id="resolution_opt_content_0"]/li[7]'
    }
    
    SUB_STREAM1_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/div[2]/form/div[4]/div/div/div/span'
    SUB_STREAM1_ENCODE_TYPE_XPATH = '//*[@id="rc_encoder_type_1"]/div/div/input'
    SUB_STREAM1_H264_XPATH = '//*[@id="rc_encoder_type_content_1"]/li[1]'
    SUB_STREAM1_MJPEG_XPATH = '//*[@id="rc_encoder_type_content_1"]/li[2]'
    SUB_STREAM1_H265_XPATH = '//*[@id="rc_encoder_type_content_1"]/li[3]'
    SUB_STREAM1_RESOLUTION_XPATH = '//*[@id="resolution_opt_1"]/div/div[1]'
    RESOLUTION_SUP = {
        "720x576": '//*[@id="resolution_opt_content_1"]/li[1]',
        "704x576": '//*[@id="resolution_opt_content_1"]/li[2]',
        "640x480": '//*[@id="resolution_opt_content_1"]/li[3]',
        "352x288": '//*[@id="resolution_opt_content_1"]/li[4]',
    }
    OK_BUTTON_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/div[2]/form/div[10]/div/button'   
    

    def click_video_menu(self):
        try:
            self._click_element((By.XPATH, self.VIDEO_MENU_XPATH))
            
        except (NoSuchElementException, TimeoutException) as e:
            self.self.logger.warning(f"菜单点击失败，将继续执行：{str(e)}")

    def click_main_stream0_encode_type(self):
        try:
            self._click_element((By.XPATH, self.MAIN_STREAM0_ENCODE_TYPE_XPATH))
            
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.warning(f"编码类型点击失败，将继续执行：{str(e)}")

    def select_stream0_encode_type(self, encode_type):
        encode_map = {
            "STREAM0_H264": self.STREAM0_H264_XPATH,
            "STREAM0_H265": self.STREAM0_H265_XPATH
        }
        if encode_type not in encode_map:
            self.logger.error(f"不支持的编码类型：{encode_type}，仅支持H264/H265")
            return 
        try:
            self._click_element((By.XPATH, encode_map[encode_type]))
            
            self.logger.info(f"成功选择编码类型：{encode_type}")
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"选择编码类型 {encode_type} 失败：{str(e)}")

    def click_main_stream0_resolution(self):
        try:
            self._click_element((By.XPATH, self.MAIN_STREAM0_RESOLUTION_XPATH))
            
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.warning(f"分辨率下拉框点击失败：{str(e)}")

    def click_sub_stream1_encode_type(self):
        try:
            self._click_element((By.XPATH, self.SUB_STREAM1_ENCODE_TYPE_XPATH))
            
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.warning(f"编码类型点击失败，将继续执行：{str(e)}")

    def select_stream1_encode_type(self, encode_type):
        encode_map = {
            "STREAM1_H264": self.SUB_STREAM1_H264_XPATH,
            "STREAM1_MJPEG": self.SUB_STREAM1_MJPEG_XPATH,
            "STREAM1_H265": self.SUB_STREAM1_H265_XPATH
        }
        if encode_type not in encode_map:
            self.logger.error(f"不支持的编码类型：{encode_type}，仅支持H264/MJPEG/H265")
            return 
        try:
            self._click_element((By.XPATH, encode_map[encode_type]))
            self.logger.info(f"成功选择编码类型：{encode_type}")
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"选择编码类型 {encode_type} 失败：{str(e)}")

    def click_sub_stream1_resolution(self):
        try:
            self._click_element((By.XPATH, self.SUB_STREAM1_RESOLUTION_XPATH))
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.warning(f"分辨率下拉框点击失败：{str(e)}")

    def select_resolution(self, resolution):
        if resolution in self.RESOLUTION_MAP:
            try:
                self._click_element((By.XPATH, self.RESOLUTION_MAP[resolution]))
                self.logger.info(f"成功选择分辨率：{resolution} (MAIN_STREAM)")
                return True
            except (NoSuchElementException, TimeoutException) as e:
                self.logger.error(f"选择分辨率 {resolution} (MAIN_STREAM) 失败：{str(e)}")
        
        if resolution in self.RESOLUTION_SUP:
            try:
                self._click_element((By.XPATH, self.RESOLUTION_SUP[resolution]))
                self.logger.info(f"成功选择分辨率：{resolution} (SUB_STREAM)")
                return True
            except (NoSuchElementException, TimeoutException) as e:
                self.logger.error(f"选择分辨率 {resolution} (SUB_STREAM) 失败：{str(e)}")
        
        self.logger.error(f"不支持的分辨率：{resolution}，支持的分辨率：{list(self.RESOLUTION_MAP.keys()) + list(self.RESOLUTION_SUP.keys())}")
        return False

    def click_ok_button(self):
        try:
            self._click_element((By.XPATH, self.OK_BUTTON_XPATH))
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.warning(f"确认按钮点击失败：{str(e)}")

    def set_video_stream0_resolution_for_encode_type(self, encode_type):
        self.click_video_menu()
        self.click_main_stream0_encode_type()
        self.select_stream0_encode_type(encode_type)

        for idx, resolution in enumerate(self.RESOLUTION_MAP.keys()):
            try:
                self.click_main_stream0_resolution()
                if self.select_resolution(resolution):
                    self.click_ok_button()
                    self.logger.info(f"完成{encode_type}编码-{resolution}分辨率的设置")
            except Exception as e:
                self.logger.error(f"设置{encode_type}编码-{resolution}分辨率失败：{str(e)}")
                continue 
    
    def set_video_stream1_resolution_for_encode_type(self, encode_type):
        self.click_video_menu()
        self.click_sub_stream1_encode_type()
        self.select_stream1_encode_type(encode_type)

        for idx, resolution in enumerate(self.RESOLUTION_SUP.keys()):
            try:
                self.click_sub_stream1_resolution()  # 修正：使用子流分辨率方法
                if self.select_resolution(resolution):
                    self.click_ok_button()
                    self.logger.info(f"完成{encode_type}编码-{resolution}分辨率的设置")
            except Exception as e:
                self.logger.error(f"设置{encode_type}编码-{resolution}分辨率失败：{str(e)}")
                continue 

    def set_all_video_configs(self):
        try:
            self.set_video_stream0_resolution_for_encode_type("STREAM0_H264")  # 修正参数
        except Exception as e:
            self.logger.critical(f"STREAM0_H264 批量设置过程出现未预期错误：{str(e)}")

        try:
            self.set_video_stream0_resolution_for_encode_type("STREAM0_H265")  # 修正参数
        except Exception as e:
            self.logger.critical(f"STREAM0_H265 批量设置过程出现未预期错误：{str(e)}")

        try:
            self.set_video_stream1_resolution_for_encode_type("STREAM1_H264")  # 修正参数
        except Exception as e:
            self.logger.critical(f"STREAM1_H264 批量设置过程出现未预期错误：{str(e)}")

        try:
            self.set_video_stream1_resolution_for_encode_type("STREAM1_MJPEG")  # 修正参数
        except Exception as e:
            self.logger.critical(f"STREAM1_MJPEG 批量设置过程出现未预期错误：{str(e)}")

        try:
            self.set_video_stream1_resolution_for_encode_type("STREAM1_H265")  # 修正参数
        except Exception as e:
            self.logger.critical(f"STREAM1_H265 批量设置过程出现未预期错误：{str(e)}")
            
        self.logger.info("所有视频配置尝试已完成（无论成功或失败）")