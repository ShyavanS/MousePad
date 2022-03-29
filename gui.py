from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file('tabs.kv')


class MyLayout(TabbedPanel):
    def left_vib(self, *args):
        self.left_text.text = str(int(args[1]))
        self.left_text.font_size = 8

    def right_vib(self, *args):
        self.right_text.text = str(int(args[1]))
        self.right_text.font_size = 8

    def scroll_sen(self, *args):
        self.scroll_text.text = str(int(args[1]))
        self.scroll_text.font_size = 8

    def cursor_sen(self, *args):
        self.cursor_text.text = str(int(args[1]))
        self.cursor_text.font_size = 8
    pass


class MousePad(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MousePad().run()
