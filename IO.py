from pynput.mouse import Controller as Mouse, Button
from pynput.keyboard import Controller as Keyboard, Key

CONTROLLER_ID = 0

STOPPER_OFFSET = 2

LEFT_SPEED = 0.8
RIGHT_SPEED = 0.3
VIBRATE_TIME = 0.2

MOVE_SPEED = 10
SCROLL_SPEED = 0.5

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

BUTTON_DICT = {
    'L1': COMMAND_DICT['Control'],
    'L3': COMMAND_DICT['Backspace'],
    'R1': COMMAND_DICT['Shift'],
    'R3': COMMAND_DICT['Enter'],
    'Menu': COMMAND_DICT['Start'],
    'Left': COMMAND_DICT['Left'],
    'Right': COMMAND_DICT['Right'],
    'Up': COMMAND_DICT['Up'],
    'Down': COMMAND_DICT['Down'],
    'A': COMMAND_DICT['Left Click'],
    'B': COMMAND_DICT['Right Click'],
    'Y': COMMAND_DICT['Middle Click'],
    'X': COMMAND_DICT['Unmapped']
}

STICK_DICT = {
    'Left Stick': MOVEMENT_DICT['Move'],
    'Right Stick': MOVEMENT_DICT['Scroll'],
}

if __name__ == "__main__":
    raise ImportError("This is not meant to be run as a main program, it is a supplementary module.")
