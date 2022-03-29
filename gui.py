from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file('tabs.kv')


class MyLayout(TabbedPanel):
    pass


class MyGui(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyGui().run()
