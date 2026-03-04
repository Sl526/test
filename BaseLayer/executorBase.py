'''
测试工具操作类
'''
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException
)
import logging
import time

class ExecutorBase():

    OPERATION_SLEEP = 1

    def __init__(self, executor=None, url=None, headless=False):
        """
        初始化执行器
        :param executor: 外部传入的 WebDriver 实例（若提供则忽略 headless 设置）
        :param url: 启动后访问的 URL
        :param headless: 是否启用无头模式（默认 False）
        """
        if executor is None:
            self.__init__executor(headless)
        else:
            self.driver = executor

        if url is not None:
            self.driver.get(url)

    def __init__executor(self, headless=False):
        """初始化 Edge 浏览器驱动，支持无头模式配置"""
        options = EdgeOptions()
        
        if headless:
            options.add_argument('--headless=new') 
            options.add_argument('--disable-gpu')   
            options.add_argument('--window-size=1920,1080')  
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        else:
            pass 
        
        self.driver = webdriver.Edge(options=options)
        
        if not headless:
            self.driver.maximize_window()
        
        self.driver.implicitly_wait(10)

    def get_executor(self):
        return self.driver
    
    def quit_executor(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def __get_locator(self, key):
        if key.lower() == "xpath":
            return By.XPATH
        raise ValueError(f"Unsupported locator type: {key}")

    def get_element(self, key, value):
        return self.driver.find_element(self.__get_locator(key), value)
    
    def get_elements(self, key, value):
        return self.driver.find_elements(self.__get_locator(key), value)
    
    def switch_to_last_window(self):
        handles = self.driver.window_handles
        if handles:
            self.driver.switch_to.window(handles[-1])
    
    def wait_for_element_disappear(self, get_element_func, seconds=5):
        WebDriverWait(self.driver, seconds).until_not(lambda d: get_element_func())
    
    def logger():
        logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        return logging.getself.logger(__name__)

    def _wait_for_element(self, locator, timeout=None):

        timeout = timeout or self.WAIT_TIMEOUT
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            self.logger.error(f"元素超时未加载：{locator}")
            raise

    def _click_element(self, locator):
        """
        通用点击方法：包含异常处理和日志
        :param locator: (By, 定位表达式)
        """
        try:
            element = self._wait_for_element(locator)
            element.click()
            self.logger.info(f"成功点击元素：{locator}")
        except (ElementClickInterceptedException, NoSuchElementException) as e:
            self.logger.error(f"点击元素失败：{locator}，错误：{str(e)}")
            raise
        finally:
            time.sleep(self.OPERATION_SLEEP)
            
    def _send_keys_to_input(self, locator, value):
        """
        通用输入方法：清空原有内容 + 输入值 + 日志 + 停顿
        :param locator: (By, 定位表达式)
        :param value: 要输入的值（数字/字符串）
        """
        try:
            element = self._wait_for_element(locator)
            element.clear()
            element.send_keys(str(value))
            self.logger.info(f"成功在元素{locator}输入值：{value}")
        except Exception as e:
            self.logger.error(f"输入值失败：{locator}，值：{value}，错误：{str(e)}")
            raise
        finally:
            time.sleep(self.OPERATION_SLEEP)

    
