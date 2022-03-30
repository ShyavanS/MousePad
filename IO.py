from pynput.mouse import Controller as Mouse, Button
from pynput.keyboard import Controller as Keyboard, Key
from Mapping import *

STOPPER_OFFSET = 4

TRIGGER_MIN = 0.0
TRIGGER_MAX = 0.25

STICK_TICK = 0.01
TRIGGER_TICK = 0.1

DEFAULT_CONTROLLER_ID = 0

DEFAULT_LEFT_SPEED = 0.8
DEFAULT_RIGHT_SPEED = 0.3

DEFAULT_VIBRATE_BUTTON_TIME = 0.2
DEFAULT_VIBRATE_TRIGGER_TIME = 0.05

DEFAULT_MOVE_SPEED = 10.0
DEFAULT_SCROLL_SPEED = 0.5

DEFAULT_BUTTON_DICT = {
    'L1': "Control",
    'L2': "Volume Up",
    'L3': "Backspace",
    'R1': "Shift",
    'R2': "Volume Down",
    'R3': "Enter",
    'Menu': "Start",
    'Left': "Left",
    'Right': "Right",
    'Up': "Up",
    'Down': "Down",
    'A': "Left Click",
    'B': "Right Click",
    'Y': "Middle Click",
    'X': "Play/Pause"
}

DEFAULT_STICK_DICT = {
    'Left Stick': "Move",
    'Right Stick': "Scroll"
}

try:
    CONTROLLER_ID, LEFT_SPEED, RIGHT_SPEED, VIBRATE_BUTTON_TIME, VIBRATE_TRIGGER_TIME, MOVE_SPEED, SCROLL_SPEED, BUTTON_DICT, STICK_DICT = load_settings()
except FileNotFoundError:
    save_settings(DEFAULT_CONTROLLER_ID, DEFAULT_LEFT_SPEED, DEFAULT_RIGHT_SPEED, DEFAULT_VIBRATE_BUTTON_TIME,
                  DEFAULT_VIBRATE_TRIGGER_TIME, DEFAULT_MOVE_SPEED, DEFAULT_SCROLL_SPEED, DEFAULT_BUTTON_DICT, DEFAULT_STICK_DICT)
    CONTROLLER_ID, LEFT_SPEED, RIGHT_SPEED, VIBRATE_BUTTON_TIME, VIBRATE_TRIGGER_TIME, MOVE_SPEED, SCROLL_SPEED, BUTTON_DICT, STICK_DICT = load_settings()

mouse = Mouse()
keyboard = Keyboard()

COMMAND_DICT = {
    'Left Click': [mouse, Button.left],
    'Right Click': [mouse, Button.right],
    'Middle Click': [mouse, Button.middle],
    'Start': [keyboard, Key.cmd],
    'Control': [keyboard, Key.ctrl],
    'Alt': [keyboard, Key.alt],
    'Delete': [keyboard, Key.delete],
    'Backspace': [keyboard, Key.backspace],
    'Space': [keyboard, Key.space],
    'Tab': [keyboard, Key.tab],
    'Enter': [keyboard, Key.enter],
    'Shift': [keyboard, Key.shift],
    'Caps Lock': [keyboard, Key.caps_lock],
    'Left': [keyboard, Key.left],
    'Right': [keyboard, Key.right],
    'Up': [keyboard, Key.up],
    'Down': [keyboard, Key.down],
    'Escape': [keyboard, Key.esc],
    'Volume Mute': [keyboard, Key.media_volume_mute],
    'Volume Down': [keyboard, Key.media_volume_down],
    'Volume Up': [keyboard, Key.media_volume_up],
    'Play/Pause': [keyboard, Key.media_play_pause],
    'Previous Track': [keyboard, Key.media_previous],
    'Next Track': [keyboard, Key.media_next],
    'Home': [keyboard, Key.home],
    'End': [keyboard, Key.end],
    'Insert': [keyboard, Key.insert],
    'Page Down': [keyboard, Key.page_down],
    'Page Up': [keyboard, Key.page_up],
    'F1': [keyboard, Key.f1],
    'F2': [keyboard, Key.f2],
    'F3': [keyboard, Key.f3],
    'F4': [keyboard, Key.f4],
    'F5': [keyboard, Key.f5],
    'F6': [keyboard, Key.f6],
    'F7': [keyboard, Key.f7],
    'F8': [keyboard, Key.f8],
    'F9': [keyboard, Key.f9],
    'F10': [keyboard, Key.f10],
    'F11': [keyboard, Key.f11],
    'F12': [keyboard, Key.f12],
    'F13': [keyboard, Key.f13],
    'F14': [keyboard, Key.f14],
    'F15': [keyboard, Key.f15],
    'F16': [keyboard, Key.f16],
    'F17': [keyboard, Key.f17],
    'F18': [keyboard, Key.f18],
    'F19': [keyboard, Key.f19],
    'F20': [keyboard, Key.f20],
    'Menu': [keyboard, Key.menu],
    'Num Lock': [keyboard, Key.num_lock],
    'Pause/Break': [keyboard, Key.pause],
    'Print Screen': [keyboard, Key.print_screen],
    'Scroll Lock': [keyboard, Key.scroll_lock],
    'Unmapped': None
}

MOVEMENT_DICT = {
    'Move': [mouse.move, -1, MOVE_SPEED],
    'Scroll': [mouse.scroll, 1, SCROLL_SPEED],
    'Unmapped': None
}

if __name__ == "__main__":
    raise ImportError(
        "This is not meant to be run as a main program, it is a supplementary module.")
