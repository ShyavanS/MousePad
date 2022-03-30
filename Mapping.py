import json


def save_settings(controller_id, left_speed, right_speed, vibrate_button_time, vibrate_trigger_time, move_speed, scroll_speed, button_dict, stick_dict):
    master_dict = {
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
        json.dump(master_dict, stdout, indent=4)


def load_settings():
    with open("settings.json", "r") as stdin:
        master_dict = json.load(stdin)

        controller_id = master_dict['CONTROLLER_ID']

        left_speed = master_dict['LEFT_SPEED']
        right_speed = master_dict['RIGHT_SPEED']

        vibrate_button_time = master_dict['VIBRATE_BUTTON_TIME']
        vibrate_trigger_time = master_dict['VIBRATE_TRIGGER_TIME']

        move_speed = master_dict['MOVE_SPEED']
        scroll_speed = master_dict['SCROLL_SPEED']

        button_dict = master_dict['BUTTON_DICT']
        stick_dict = master_dict['STICK_DICT']

    return controller_id, left_speed, right_speed, vibrate_button_time, vibrate_trigger_time, move_speed, scroll_speed, button_dict, stick_dict
