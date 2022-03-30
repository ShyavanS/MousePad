# TODO: Comment all code
# TODO: Work on GUI
# TODO: Add end-user button remapping support in GUI
# TODO: Add end-user speed multiplier modification support in GUI
# TODO: Create readme
# TODO: Add autoupdater
# TODO: Bug testing

from Controller import *
from os import environ
from tendo import singleton
from win10toast_click import ToastNotifier

environ["PBR_VERSION"] = "4.0.2"

mousepad = singleton.SingleInstance()


def main():
    on = True

    l2_pressed = False
    r2_pressed = False

    last_stick = timestamp()
    last_trigger = timestamp()

    notify = ToastNotifier()

    error_notified = False
    disable_notified = False

    while True:
        try:
            events, triggers, sticks = poll_controller(CONTROLLER_ID)

            error_notified = False
        except XInputNotConnectedError:
            if error_notified == False:
                notify.show_toast("Controller Disconnected", "Controller may not be connected, try checking if bluetooth is working or reconnect the usb cable.",
                                  icon_path="MousePad.ico", duration=5, threaded=True)

                error_notified = True
            continue

        try:
            on = button_handler(events, on)
        except (Keyboard.InvalidKeyException, TypeError):
            pass

        if on == True:
            if disable_notified == True:
                notify.show_toast("Controller Input Enabled", "The controller input has now been enabled, press the View Button to de-activate it.",
                                  icon_path="MousePad.ico", duration=5, threaded=True)

            last_trigger, l2_pressed, r2_pressed = trigger_handler(
                triggers, last_trigger, l2_pressed, r2_pressed)
            last_stick = stick_handler(sticks, last_stick)

            disable_notified = False
        else:
            if disable_notified == False:
                notify.show_toast("Controller Input Disabled", "The controller input has now been disabled, press the View Button to re-activate it.",
                                  icon_path="MousePad.ico", duration=5, threaded=True)

                disable_notified = True


if __name__ == "__main__":
    main()
else:
    raise ImportError(
        "This is not meant to be imported as a module, it is the main program for MousePad.")
