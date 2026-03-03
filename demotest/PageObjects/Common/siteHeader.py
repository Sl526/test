'''
页眉公共区块
'''
from selenium.webdriver.common.by import By
from BaseLayer.executorBase import ExecutorBase

class SiteHeader(ExecutorBase):
    WAIT_TIMEOUT = 10
    def login(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/div[2]/form/div[4]/div/button/span')

    def Configure(self):
        return self.get_element(By.XPATH,'//*[@id="app"]/div/section/header/div[4]/ul/li[2]')
    
    def click_login(self):
        self._click_element(self.login())
        from PageObjects.Camera_ListPage import camera_listpage
        return camera_listpage(self.get_executor())

    def click_configure(self):
        self._click_element(self.Configure())
        from PageObjects.Camera_ListPage import camera_listpage
        return camera_listpage(self.get_executor())