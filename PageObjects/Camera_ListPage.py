from selenium.webdriver.common.by import By
from BaseLayer.executorBase import ExecutorBase
from PageObjects.Common.siteHeader import SiteHeader


class Camera_listPage(SiteHeader, ExecutorBase):
    CAMERA_MENU_XPATH = '//*[@id="app"]/div/section/main/div/section/aside/div/ul/li[2]'
    CAPTURE_SWITCH_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[2]/div/div/span'
    WORK_MODE_INPUT_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[3]/div[1]/div/div/div[1]/input'
    WORK_MODE_SDR_XPATH = '//li/span[text()="SDR"]'
    WORK_MODE_HDR_XPATH = '//li/span[text()="HDR"]'
    FPS_INPUT_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div/div[1]/input'
    FPS_25_XPATH = '//li/span[text()="25"]'
    FPS_30_XPATH = '//li/span[text()="30"]'
    DAY_NIGHT_INPUT_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[6]/div/div/div[1]/input'
    DAY_MODE_XPATH = '//li/span[text()="Day Mode"]'
    NIGHT_MODE_XPATH = '//li/span[text()="Night Mode"]'
    AUTO_MODE_XPATH = '//li/span[text()="Auto Mode"]'
    ROTATION_INPUT_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[7]/div/div/div/input'
    ROTATION_0_XPATH = '//li/span[text()="0°"]'
    ROTATION_90_XPATH = '//li/span[text()="90°"]'
    ROTATION_180_XPATH = '//li/span[text()="180°"]'
    ROTATION_270_XPATH = '//li/span[text()="270°"]'
    MIRROR_SWITCH_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/form/div/div[1]/div/div/div/span'
    FLIP_SWITCH_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/form/div/div[2]/div/div/div/span'
    OK_BUTTON_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[8]/div/button'
    #endregion

    def set_camera(self):
        """
        设置相机参数主流程。
        """
        steps = [
            ("点击相机菜单", self._click_camera_menu),
            ("点击抓图开关", self._click_capture),
            ("配置工作模式", self._configure_work_mode),
            ("配置帧率", self._configure_fps),
            ("配置日夜模式", self._configure_day_night),
            #("配置旋转", self._configure_rotation),
            ("点击镜像", self._click_mirror),
            # ("点击翻转", self._click_flip),
            ("点击确认按钮", self._click_ok),
        ]

        for step_name, step_func in steps:
            try:
                self.logger.info(f"🚀 开始执行: {step_name}")
                step_func()
                self.logger.info(f" 成功完成: {step_name}")
            except Exception as e:
                self.logger.error(f"❌ 步骤异常但继续: {step_name} | 错误: {str(e)}")

        self.logger.info("📸 相机配置流程执行完毕（所有步骤已尝试）。")

    #region 私有操作方法 (Individual Actions)
    def _click_camera_menu(self):
        self._click_element((By.XPATH, self.CAMERA_MENU_XPATH))

    def _click_capture(self):
        self._click_element((By.XPATH, self.CAPTURE_SWITCH_XPATH))

    def _configure_work_mode(self):
        self._click_element((By.XPATH, self.WORK_MODE_INPUT_XPATH))
        self._click_element((By.XPATH, self.WORK_MODE_HDR_XPATH)) # 默认选HDR

    def _configure_fps(self):
        self._click_element((By.XPATH, self.FPS_INPUT_XPATH))
        self._click_element((By.XPATH, self.FPS_25_XPATH)) # 默认选25

    def _configure_day_night(self):
        self._click_element((By.XPATH, self.DAY_NIGHT_INPUT_XPATH))
        self._click_element((By.XPATH, self.DAY_MODE_XPATH)) # 默认选白天

    # def _configure_rotation(self):
    #     self._click_element((By.XPATH, self.ROTATION_INPUT_XPATH))
    #     self._click_element((By.XPATH, self.ROTATION_0_XPATH)) # 默认选0度

    def _click_mirror(self):
        self._click_element((By.XPATH, self.MIRROR_SWITCH_XPATH))

    def _click_flip(self):
        self._click_element((By.XPATH, self.FLIP_SWITCH_XPATH))

    def _click_ok(self):
        self._click_element((By.XPATH, self.OK_BUTTON_XPATH))
    #endregion