# TODO: Comment all code
# TODO: Create GUI and GUI module
# TODO: Refine Controller module
# TODO: Add end-user button remapping support in GUI
# TODO: Add end-user speed multiplier modification support in GUI
# TODO: Create readme
# TODO: Build releases and generate installer files
# TODO: Implement startup service
# TODO: Add multiple controller support
# TODO: Add logging functionality for debugging
# TODO: Add autoupdater
# TODO: Create testing plan
# TODO: Bug testing

from Controller import *


def main():
    on = True

    last_stick = timestamp()
    last_trigger = timestamp()

    l2_pressed = False
    r2_pressed = False

    while True:
        try:
            events, triggers, sticks = poll_controller(CONTROLLER_ID)
        except XInputNotConnectedError:
            input(
                "Controller may not be connected, try checking the connection and hit enter to check again.")
            continue

        try:
            on = button_handler(events, on)
        except (Keyboard.InvalidKeyException, TypeError):
            pass

        if on == True:
            last_trigger, l2_pressed, r2_pressed = trigger_handler(
                triggers, last_trigger, l2_pressed, r2_pressed)
            last_stick = stick_handler(sticks, last_stick)


if __name__ == "__main__":
    main()
else:
    raise ImportError(
        "This is not meant to be imported as a module, it is the main program for MousePad.")
