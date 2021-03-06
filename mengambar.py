# mengambar.py

from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.colorpicker import ColorPicker
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.relativelayout import RelativeLayout

col = [0,0,1,1]


class SelectedColorEllipse(Widget):
    selected_color = ListProperty(col)

class ColPckr(ColorPicker):
    pass

class ColPopup(Popup):
    pass

class mengambar(Widget):
    selected_color = ListProperty(col)
    def select_ColPckr(self,*args):
        ColPopup().open()

     
    def on_touch_move(self, touch):
        if touch.x <100 and touch.y < 100:
            return super(mengambar, self).on_touch_move(touch)
        sce = SelectedColorEllipse()
        sce.selected_color = self.selected_color
        sce.center = touch.pos
        self.add_widget(sce)

        

class mengambarApp(App):
    def build(self):
        return mengambar()

if __name__=='__main__':
    mengambarApp().run()
