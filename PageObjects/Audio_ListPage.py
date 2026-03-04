from selenium.webdriver.common.by import By
from BaseLayer.executorBase import ExecutorBase
from PageObjects.Common.siteHeader import SiteHeader


class AudiolistPage(SiteHeader, ExecutorBase):

    AUDIO_MENU_XPATH = '//*[@id="app"]/div/section/main/div/section/aside/div/ul/li[5]'
    MICROPHONE_VOLUME_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[2]/div/div/div[1]/div/input'
    SPEAKER_VOLUME_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[4]/div/div/div[1]/div/input'
    AUDIO_DETECT_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[5]/div/div/span'
    DECIBEL_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[6]/div/div/div[1]/div/input'
    PUSH_INTERVAL_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/form/div[7]/div/div/div[1]/div/input'
    OK_BUTTON_XPATH = '//*[@id="app"]/div/section/main/div/section/main/div/div/button'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_microphone_volume = 10
        self.default_speaker_volume = 10
        self.default_decibel = 150
        self.default_push_interval = 600

    def _click_audio_menu(self):
        """点击音频菜单"""
        try:
            self._click_element((By.XPATH, self.AUDIO_MENU_XPATH))
            self.logger.info("成功点击音频菜单")
            return True
        except Exception as e:
            self.logger.error(f"点击音频菜单失败：{str(e)}")
            return False

    def _set_microphone_volume(self, volume=None):
        """设置麦克风音量"""
        volume = volume if volume is not None else self.default_microphone_volume
        try:
            self._send_keys_to_input((By.XPATH, self.MICROPHONE_VOLUME_XPATH), volume)
            self.logger.info(f"成功设置麦克风音量为：{volume}")
            return True
        except Exception as e:
            self.logger.error(f"设置麦克风音量失败：{str(e)}")
            return False

    def _set_speaker_volume(self, volume=None):
        """设置扬声器音量"""
        volume = volume if volume is not None else self.default_speaker_volume
        try:
            self._send_keys_to_input((By.XPATH, self.SPEAKER_VOLUME_XPATH), volume)
            self.logger.info(f"成功设置扬声器音量为：{volume}")
            return True
        except Exception as e:
            self.logger.error(f"设置扬声器音量失败：{str(e)}")
            return False

    def _enable_audio_detect(self):
        """启用音频检测"""
        try:
            self._click_element((By.XPATH, self.AUDIO_DETECT_XPATH))
            self.logger.info("成功启用音频检测")
            return True
        except Exception as e:
            self.logger.error(f"启用音频检测失败：{str(e)}")
            return False

    def _set_decibel(self, decibel=None):
        """设置分贝阈值"""
        decibel = decibel if decibel is not None else self.default_decibel
        try:
            self._send_keys_to_input((By.XPATH, self.DECIBEL_XPATH), decibel)
            self.logger.info(f"成功设置分贝阈值为：{decibel}")
            return True
        except Exception as e:
            self.logger.error(f"设置分贝阈值失败：{str(e)}")
            return False

    def _set_push_interval(self, interval=None):
        """设置推送间隔"""
        interval = interval if interval is not None else self.default_push_interval
        try:
            self._send_keys_to_input((By.XPATH, self.PUSH_INTERVAL_XPATH), interval)
            self.logger.info(f"成功设置推送间隔为：{interval}")
            return True
        except Exception as e:
            self.logger.error(f"设置推送间隔失败：{str(e)}")
            return False

    def _click_ok_button(self):
        """点击确认按钮"""
        try:
            self._click_element((By.XPATH, self.OK_BUTTON_XPATH))
            self.logger.info("成功点击确认按钮")
            return True
        except Exception as e:
            self.logger.error(f"点击确认按钮失败：{str(e)}")
            return False

    def set_audio(self, microphone_volume=None, speaker_volume=None, 
                  decibel=None, push_interval=None):
        """
        设置音频配置，单步失败不中断整体流程
        支持自定义参数，未提供参数时使用默认值
        """
        steps = [
            ("点击音频菜单", self._click_audio_menu),
            ("设置麦克风音量", lambda: self._set_microphone_volume(microphone_volume)),
            ("设置扬声器音量", lambda: self._set_speaker_volume(speaker_volume)),
            ("启用音频检测", self._enable_audio_detect),
            ("设置分贝阈值", lambda: self._set_decibel(decibel)),
            ("设置推送间隔", lambda: self._set_push_interval(push_interval)),
            ("点击确认按钮", self._click_ok_button)
        ]

        for step_name, step_func in steps:
            try:
                self.logger.info(f"开始执行步骤：{step_name}")
                step_func()
                self.logger.info(f"步骤成功：{step_name}")
            except Exception as e:
                self.logger.error(f"步骤失败但继续执行：{step_name} - 错误: {str(e)}")

        self.logger.info("音频配置流程执行完毕，无论成功或失败均已完成遍历。")