from selenium.webdriver.common.by import By
from BaseLayer.executorBase import ExecutorBase
from PageObjects.Common.siteHeader import SiteHeader
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AIListPage(SiteHeader, ExecutorBase):

    OPERATION_SLEEP = 1.0
    AI_MENU_XPATH = '//*[@id="app"]/div/section/main/div/section/aside/div/ul/li[4]'
    OK_BUTTON_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/div[3]/button'
    AI_OPTIONS_TAB_XPATH = '//*[@id="tab-options"]'
    AI_ENABLED_XPATH = '//*[@id="pane-options"]/form/div[1]/div/div/span'
    INTELLIGENT_ENCODING_XPATH = '//*[@id="pane-options"]/form/div[5]/div/div/span'
    HUMAN_FACE_XPATH = '//*[@id="pane-options"]/form/div[8]/div/div/div[1]/div/div/span'
    HUMAN_BODY_XPATH = '//*[@id="pane-options"]/form/div[9]/div/div/div[1]/div/div/span'
    VEHICLE_XPATH = '//*[@id="pane-options"]/form/div[10]/div/div/div[1]/div/div/span'
    BICYCLE_XPATH = '//*[@id="pane-options"]/form/div[11]/div/div/div[1]/div/div/span'
    PLATE_XPATH = '//*[@id="pane-options"]/form/div[12]/div/div/div[1]/div/div/span'
    EVENT_REPORT_TAB_XPATH = '//*[@id="tab-events"]'
    MOTION_DETECT_XPATH = '//*[@id="pane-events"]/form/div[1]/div/div[1]/span'
    MOTION_DETECT_Y_THRESHOLD_XPATH = '//*[@id="pane-events"]/form/div[1]/div/div[2]/div/div/div[1]/div/input'
    MOTION_DETECT_CONFIDENCE_XPATH = '//*[@id="pane-events"]/form/div[1]/div/div[3]/div/div/div[1]/div/input'
    OCCLUSION_DETECT_XPATH = '//*[@id="pane-events"]/form/div[2]/div/div[1]/span'
    OCCLUSION_DETECT_Y_THRESHOLD_XPATH = '//*[@id="pane-events"]/form/div[2]/div/div[2]/div/div/div[1]/div/input'
    OCCLUSION_DETECT_CONFIDENCE_XPATH = '//*[@id="pane-events"]/form/div[2]/div/div[3]/div/div/div[1]/div/input'
    SCENE_CHANGE_DETECT_XPATH = '//*[@id="pane-events"]/form/div[3]/div/div[1]/span'
    SCENE_CHANGE_THRESHOLD_XPATH = '//*[@id="pane-events"]/form/div[3]/div/div[2]/div/div/div[1]/div/input'
    SCENE_CHANGE_CONFIDENCE_XPATH = '//*[@id="pane-events"]/form/div[3]/div/div[3]/div/div/div[1]/div/input'
    ANTI_OVEREXPOSURE_TAB_XPATH = '//*[@id="tab-AEROI"]'
    HUMAN_ANTI_OVEREXPOSURE_XPATH = '//*[@id="pane-AEROI"]/form/div[1]/div/div/span'
    VEHICLE_ANTI_OVEREXPOSURE_XPATH = '//*[@id="pane-AEROI"]/form/div[2]/div/div/span'

   
    def click_ai_menu(self):
        """点击AI菜单"""
        self._click_element((By.XPATH, self.AI_MENU_XPATH))

    def click_ai_options_tab(self):
        """点击AI选项标签页"""
        self._click_element((By.XPATH, self.AI_OPTIONS_TAB_XPATH))

    def configure_ai_detection_types(self):
        """配置AI检测类型（人脸、人体、车辆、自行车、车牌、智能编码）"""
        self._click_element((By.XPATH, self.INTELLIGENT_ENCODING_XPATH))
        detect_types = [
            self.HUMAN_FACE_XPATH,
            self.HUMAN_BODY_XPATH,
            self.VEHICLE_XPATH,
            self.BICYCLE_XPATH,
            self.PLATE_XPATH
        ]
        for xpath in detect_types:
            self._click_element((By.XPATH, xpath))

    def configure_event_report(self):
        """配置事件上报（移动检测、遮挡检测、场景变化检测）"""
        self._click_element((By.XPATH, self.EVENT_REPORT_TAB_XPATH))
        self._click_element((By.XPATH, self.MOTION_DETECT_XPATH))
        self._send_keys_to_input((By.XPATH, self.MOTION_DETECT_Y_THRESHOLD_XPATH), 255)
        self._send_keys_to_input((By.XPATH, self.MOTION_DETECT_CONFIDENCE_XPATH), 100)
        self._click_element((By.XPATH, self.OCCLUSION_DETECT_XPATH))
        self._send_keys_to_input((By.XPATH, self.OCCLUSION_DETECT_Y_THRESHOLD_XPATH), 255)
        self._send_keys_to_input((By.XPATH, self.OCCLUSION_DETECT_CONFIDENCE_XPATH), 100)
        self._click_element((By.XPATH, self.SCENE_CHANGE_DETECT_XPATH))
        self._send_keys_to_input((By.XPATH, self.SCENE_CHANGE_THRESHOLD_XPATH), 100)
        self._send_keys_to_input((By.XPATH, self.SCENE_CHANGE_CONFIDENCE_XPATH), 100)

    def configure_anti_overexposure(self):
        """配置防过曝策略（人体/车辆防过曝）"""
        self._click_element((By.XPATH, self.ANTI_OVEREXPOSURE_TAB_XPATH))
        self._click_element((By.XPATH, self.HUMAN_ANTI_OVEREXPOSURE_XPATH))
        self._click_element((By.XPATH, self.VEHICLE_ANTI_OVEREXPOSURE_XPATH))

    def click_ok_button(self):
        """点击确认按钮"""
        self._click_element((By.XPATH, self.OK_BUTTON_XPATH))

    def reset_ai_basic_config(self):
        """重置AI基础配置（防过曝、AI启用、事件检测）"""
        self._click_element((By.XPATH, self.ANTI_OVEREXPOSURE_TAB_XPATH))
        self._click_element((By.XPATH, self.HUMAN_ANTI_OVEREXPOSURE_XPATH))
        self._click_element((By.XPATH, self.VEHICLE_ANTI_OVEREXPOSURE_XPATH))
        self._click_element((By.XPATH, self.AI_OPTIONS_TAB_XPATH))
        #self._click_element((By.XPATH, self.AI_ENABLED_XPATH))
        self._click_element((By.XPATH, self.EVENT_REPORT_TAB_XPATH))
        self._click_element((By.XPATH, self.MOTION_DETECT_XPATH))
        self._click_element((By.XPATH, self.OCCLUSION_DETECT_XPATH))
        self._click_element((By.XPATH, self.SCENE_CHANGE_DETECT_XPATH))

    def set_ai(self):
        """
        流程：AI菜单 → AI选项 → 检测类型 → 事件上报 → 防过曝 → 确认 → 重置基础配置 → 确认
        """
        steps = [
            ("点击AI菜单", self.click_ai_menu),
            ("点击AI选项卡", self.click_ai_options_tab),
            ("配置检测类型", self.configure_ai_detection_types),
            ("配置事件上报", self.configure_event_report),
            ("配置防过曝", self.configure_anti_overexposure),
            ("点击确认按钮1", self.click_ok_button),
            ("重置基础配置", self.reset_ai_basic_config),
            ("点击确认按钮2", self.click_ok_button)
        ]

        for step_name, step_func in steps:
            try:
                logger.info(f"正在执行步骤：{step_name}")
                step_func() # 执行该步骤
                logger.info(f"步骤成功：{step_name}")
            except Exception as e:
                logger.error(f"步骤失败，但继续执行下一条：{step_name} - 错误: {str(e)}")

        logger.info("AI配置流程（容错模式）执行完毕，无论成功或失败均已完成遍历。")
