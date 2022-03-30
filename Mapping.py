import json


def save_settings(controller_id, left_speed, right_speed, vibrate_button_time, vibrate_trigger_time, move_speed, scroll_speed, button_dict, stick_dict):
    MASTER_DICT = {
        'CONTROLLER_ID': controller_id,
        'LEFT_SPEED': left_speed,
        'RIGHT_SPEED': right_speed,
        'VIBRATE_BUTTON_TIME': vibrate_button_time,
        'VIBRATE_TRIGGER_TIME': vibrate_trigger_time,
        'MOVE_SPEED': move_speed,
        'SCROLL_SPEED': scroll_speed,
        'BUTTON_DICT': button_dict.copy(),
        'STICK_DICT': stick_dict.copy()
    }

    with open("settings.json", "w") as stdout:
        json.dump(MASTER_DICT, stdout, indent=4)


def load_settings():
    with open("settings.json", "r") as stdin:
        MASTER_DICT = json.load(stdin)

        controller_id = MASTER_DICT['CONTROLLER_ID']

        left_speed = MASTER_DICT['LEFT_SPEED']
        right_speed = MASTER_DICT['RIGHT_SPEED']

        vibrate_button_time = MASTER_DICT['VIBRATE_BUTTON_TIME']
        vibrate_trigger_time = MASTER_DICT['VIBRATE_TRIGGER_TIME']

        move_speed = MASTER_DICT['MOVE_SPEED']
        scroll_speed = MASTER_DICT['SCROLL_SPEED']

        button_dict = MASTER_DICT['BUTTON_DICT']
        stick_dict = MASTER_DICT['STICK_DICT']

    return controller_id, left_speed, right_speed, vibrate_button_time, vibrate_trigger_time, move_speed, scroll_speed, button_dict, stick_dict
