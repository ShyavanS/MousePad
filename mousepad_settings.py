from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from os import environ
from tendo import singleton

environ["PBR_VERSION"] = "4.0.2"

mousepad = singleton.SingleInstance()

Builder.load_file('gui_layout.kv')


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

    def vibration_time(self, value):
        self.ids.vibration_id.text = value

    def controller_num(self, value):
        self.ids.controller_id.text = value

    def left_joystick(self, value):
        self.ids.left_stick.text = value

    def press_up(self, value):
        self.ids.up_button.text = value

    def press_left(self, value):
        self.ids.left_button.text = value

    def press_right(self, value):
        self.ids.right_button.text = value

    def press_down(self, value):
        self.ids.down_button.text = value

    def press_l1(self, value):
        self.ids.l1_button.text = value

    def press_l2(self, value):
        self.ids.l2_button.text = value

    def press_y(self, value):
        self.ids.y_button.text = value

    def press_x(self, value):
        self.ids.x_button.text = value

    def press_b(self, value):
        self.ids.b_button.text = value

    def press_a(self, value):
        self.ids.a_button.text = value

    def right_joystick(self, value):
        self.ids.right_stick.text = value

    def press_r2(self, value):
        self.ids.r1_button.text = value

    def press_r2(self, value):
        self.ids.r2_button.text = value
    pass


class MousePad(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MousePad().run()
