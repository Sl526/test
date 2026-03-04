from PageObjects.camera_listpage import Camera_listPage
from PageObjects.image_listpage import Image_listPage
from PageObjects.ai_listpage import Ai_ListPage
from PageObjects.audio_listpage import Audio_listPage
from PageObjects.video_listpage import Video_listPage

class TestEpiBitCommon:
    def test_camera(self, homepage):
        camera = Camera_listPage(homepage.get_executor())
        camera.set_camera()

    def test_image(self, homepage):
        image = Image_listPage(homepage.get_executor())
        image.set_image()
        
    def test_ai(self, homepage):
        ai = Ai_ListPage(homepage.get_executor())
        ai.set_ai()

    def test_audio(self, homepage):
        audio = Audio_listPage(homepage.get_executor())
        audio.set_audio()

    def test_video(self, homepage):
        video = Video_listPage(homepage.get_executor())
        video.set_all_video_configs()
        
        