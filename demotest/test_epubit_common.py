from PageObjects.Camera_ListPage import camera_listpage
from PageObjects.Image_ListPage import Image_listpage   
from PageObjects.AI_ListPage import AIListPage
from PageObjects.Audio_ListPage import audio_listpage
from PageObjects.Video_ListPage import video_listpage

class TestEpiBitCommon:
    def test_camera(self, homepage):
        camera = camera_listpage(homepage.get_executor())
        camera.set_camera()

    def test_image(self, homepage):
        image = Image_listpage(homepage.get_executor())
        image.set_image()
        
    def test_ai(self, homepage):
        ai = AIListPage(homepage.get_executor())
        ai.set_ai()

    def test_audio(self, homepage):
        audio = audio_listpage(homepage.get_executor())
        audio.set_audio()

    def test_video(self, homepage):
        video = video_listpage(homepage.get_executor())
        video.set_all_video_configs()
        
        