from kivy.config import Config

Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

from controller.ctrlVideo import CtrlVideo
from controller.ctrlPlayList import CtrlPlayList

Window.size = (800, 500)


class P(FloatLayout):
    pass


# Container class for the app's widgets
class SampBoxLayout(BoxLayout):

    # Callback for the checkbox
    def checkbox_click(self, instance, value):
        if value is True:
            self.ids.title.disabled = False
            print("Checkbox Checked")
        else:
            self.ids.title.disabled = True
            print("Checkbox Unchecked")

    def extract_mp3(self):
        url = self.ids.url.text
        check = self.ids.pl.active
        title = self.ids.title.text
        if check:
            if title == "":
                show_popup()
                return
            cp = CtrlPlayList(url, title)
            status = cp.descargaMp3()

        else:
            cv = CtrlVideo(url)
            status = cv.descargaMp3()

        self.ids.status.color = (.3, .7, .3)
        self.ids.status.text = f"{status}"


# App derived from App class
class Mp3App(App):

    # build is a method of Kivy's App class used
    # to place widgets onto the GUI.
    def build(self):
        # setting up window background color
        Window.clearcolor = (.90, .90, .90, .90)
        return SampBoxLayout()


def show_popup():
    show = P()

    popupWindow = Popup(title="Alerta!!", content=show, size_hint=(None, None), size=(400, 200))

    popupWindow.open()
