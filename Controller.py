from time import time as timestamp, sleep
from threading import Thread
from XInput import *
from IO import *


def poll_controller(user_index):
    state = get_state(user_index)
    triggers = get_trigger_values(state)
    sticks = get_thumb_values(state)
    events = get_events()

    return events, triggers, sticks


def vibrate_controller(user_index, left_speed, right_speed, vibrate_time):
    set_vibration(user_index, left_speed, right_speed)
    sleep(vibrate_time)
    set_vibration(0, 0, 0)

    return True


def button_handler(events, on):
    for event in events:
        if event.type == EVENT_BUTTON_PRESSED and on == True:
            if event.button == "LEFT_THUMB":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['L3']][0].press(
                    COMMAND_DICT[BUTTON_DICT['L3']][1])
                print("L3 pressed")
                print(f"{BUTTON_DICT['L3']} activated")
            elif event.button == "RIGHT_THUMB":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['R3']][0].press(
                    COMMAND_DICT[BUTTON_DICT['R3']][1])
                print("R3 pressed")
                print(f"{BUTTON_DICT['R3']} activated")

            elif event.button == "LEFT_SHOULDER":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['L1']][0].press(
                    COMMAND_DICT[BUTTON_DICT['L1']][1])
                print("L1 pressed")
                print(f"{BUTTON_DICT['L1']} activated")
            elif event.button == "RIGHT_SHOULDER":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['R1']][0].press(
                    COMMAND_DICT[BUTTON_DICT['R1']][1])
                print("R1 pressed")
                print(f"{BUTTON_DICT['R1']} activated")

            elif event.button == "BACK":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                print("View pressed")

            elif event.button == "START":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['Menu']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Menu']][1])
                print("Menu pressed")
                print(f"{BUTTON_DICT['Menu']} activated")

            elif event.button == "DPAD_LEFT":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['Left']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Left']][1])
                print("Left pressed")
                print(f"{BUTTON_DICT['Left']} activated")
            elif event.button == "DPAD_RIGHT":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['Right']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Right']][1])
                print("Right pressed")
                print(f"{BUTTON_DICT['Right']} activated")
            elif event.button == "DPAD_UP":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['Up']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Up']][1])
                print("Up pressed")
                print(f"{BUTTON_DICT['Up']} activated")
            elif event.button == "DPAD_DOWN":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['Down']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Down']][1])
                print("Down pressed")
                print(f"{BUTTON_DICT['Down']} activated")

            elif event.button == "A":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['A']][0].press(
                    COMMAND_DICT[BUTTON_DICT['A']][1])
                print("A pressed")
                print(f"{BUTTON_DICT['A']} activated")
            elif event.button == "B":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['B']][0].press(
                    COMMAND_DICT[BUTTON_DICT['B']][1])
                print("B pressed")
                print(f"{BUTTON_DICT['B']} activated")
            elif event.button == "Y":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['Y']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Y']][1])
                print("Y pressed")
                print(f"{BUTTON_DICT['Y']} activated")
            elif event.button == "X":
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['X']][0].press(
                    COMMAND_DICT[BUTTON_DICT['X']][1])
                print("X pressed")
                print(f"{BUTTON_DICT['X']} activated")

        elif event.type == EVENT_BUTTON_RELEASED and on == True:
            if event.button == "LEFT_THUMB":
                COMMAND_DICT[BUTTON_DICT['L3']][0].release(
                    COMMAND_DICT[BUTTON_DICT['L3']][1])
                print("L3 released")
                print(f"{BUTTON_DICT['L3']} deactivated")
            elif event.button == "RIGHT_THUMB":
                COMMAND_DICT[BUTTON_DICT['R3']][0].release(
                    COMMAND_DICT[BUTTON_DICT['R3']][1])
                print("R3 released")
                print(f"{BUTTON_DICT['R3']} deactivated")

            elif event.button == "LEFT_SHOULDER":
                COMMAND_DICT[BUTTON_DICT['L1']][0].release(
                    COMMAND_DICT[BUTTON_DICT['L1']][1])
                print("L1 released")
                print(f"{BUTTON_DICT['L1']} deactivated")
            elif event.button == "RIGHT_SHOULDER":
                COMMAND_DICT[BUTTON_DICT['R1']][0].release(
                    COMMAND_DICT[BUTTON_DICT['R1']][1])
                print("R1 released")
                print(f"{BUTTON_DICT['R1']} deactivated")

            elif event.button == "BACK":
                on = False
                print("View released")
                print("controller input off")
            elif event.button == "START":
                COMMAND_DICT[BUTTON_DICT['Menu']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Menu']][1])
                print("Menu released")
                print(f"{BUTTON_DICT['Menu']} deactivated")

            elif event.button == "DPAD_LEFT":
                COMMAND_DICT[BUTTON_DICT['Left']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Left']][1])
                print("Left released")
                print(f"{BUTTON_DICT['Left']} deactivated")
            elif event.button == "DPAD_RIGHT":
                COMMAND_DICT[BUTTON_DICT['Right']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Right']][1])
                print("Right released")
                print(f"{BUTTON_DICT['Right']} deactivated")
            elif event.button == "DPAD_UP":
                COMMAND_DICT[BUTTON_DICT['Up']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Up']][1])
                print("Up released")
                print(f"{BUTTON_DICT['Up']} deactivated")
            elif event.button == "DPAD_DOWN":
                COMMAND_DICT[BUTTON_DICT['Down']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Down']][1])
                print("Down released")
                print(f"{BUTTON_DICT['Down']} deactivated")

            elif event.button == "A":
                COMMAND_DICT[BUTTON_DICT['A']][0].release(
                    COMMAND_DICT[BUTTON_DICT['A']][1])
                print("A released")
                print(f"{BUTTON_DICT['A']} deactivated")
            elif event.button == "B":
                COMMAND_DICT[BUTTON_DICT['B']][0].release(
                    COMMAND_DICT[BUTTON_DICT['B']][1])
                print("B released")
                print(f"{BUTTON_DICT['B']} deactivated")
            elif event.button == "Y":
                COMMAND_DICT[BUTTON_DICT['Y']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Y']][1])
                print("Y released")
                print(f"{BUTTON_DICT['Y']} deactivated")
            elif event.button == "X":
                COMMAND_DICT[BUTTON_DICT['X']][0].release(
                    COMMAND_DICT[BUTTON_DICT['X']][1])
                print("X released")
                print(f"{BUTTON_DICT['X']} deactivated")

        elif event.type == EVENT_BUTTON_PRESSED and on == False:
            if event.button == "BACK":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                print("view pressed")

        elif event.type == EVENT_BUTTON_RELEASED and on == False:
            if event.button == "BACK":
                on = True
                print("view released")
                print("controller input on")

    try:
        t.start()
    except UnboundLocalError:
        pass

    return on


def trigger_handler(triggers, last_trigger, l2_pressed, r2_pressed):
    l2 = max(min(TRIGGER_MAX, triggers[0]), TRIGGER_MIN) * STOPPER_OFFSET
    r2 = max(min(TRIGGER_MAX, triggers[1]), TRIGGER_MIN) * STOPPER_OFFSET

    current = timestamp()

    tick = current - last_trigger

    if tick >= TRIGGER_TICK:
        try:
            if l2 != 0:
                print("L2 state:", l2)
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['L2']][0].press(
                    COMMAND_DICT[BUTTON_DICT['L2']][1])
                print("L2 pressed")
                print(f"{BUTTON_DICT['L2']} activated")
                l2_pressed = True
            elif l2_pressed == True:
                COMMAND_DICT[BUTTON_DICT['L2']][0].release(
                    COMMAND_DICT[BUTTON_DICT['L2']][1])
                print("L2 released")
                print(f"{BUTTON_DICT['L2']} deactivated")
                l2_pressed = False
        except TypeError:
            pass

        try:
            if r2 != 0:
                print("R2 state:", r2)
                t = Thread(target=vibrate_controller, args=(
                    0, 0, RIGHT_SPEED, VIBRATE_TIME,))
                COMMAND_DICT[BUTTON_DICT['R2']][0].press(
                    COMMAND_DICT[BUTTON_DICT['R2']][1])
                print("R2 pressed")
                print(f"{BUTTON_DICT['R2']} activated")
                r2_pressed = True
            elif r2_pressed == True:
                COMMAND_DICT[BUTTON_DICT['R2']][0].release(
                    COMMAND_DICT[BUTTON_DICT['R2']][1])
                print("R2 released")
                print(f"{BUTTON_DICT['R2']} deactivated")
                r2_pressed = False
        except TypeError:
            pass

        try:
            t.start()
        except UnboundLocalError:
            pass

        last_trigger = current

    return last_trigger, l2_pressed, r2_pressed


def stick_handler(sticks, last_stick):
    left_stick = sticks[0]
    right_stick = sticks[1]

    current = timestamp()
    tick = current - last_stick

    if tick >= STICK_TICK:
        try:
            if left_stick[0] != 0 and left_stick[1] != 0:
                print("Left Stick state:", left_stick)

            MOVEMENT_DICT[STICK_DICT['Left Stick']][0](MOVEMENT_DICT[STICK_DICT['Left Stick']][2] * left_stick[0],
                                                       MOVEMENT_DICT[STICK_DICT['Left Stick']][2] * MOVEMENT_DICT[STICK_DICT['Left Stick']][1] * left_stick[1])
        except TypeError:
            pass

        try:
            if right_stick[0] != 0 and right_stick[1] != 0:
                print("Right stick state:", right_stick)

            MOVEMENT_DICT[STICK_DICT['Right Stick']][0](MOVEMENT_DICT[STICK_DICT['Right Stick']][2] * right_stick[0],
                                                        MOVEMENT_DICT[STICK_DICT['Right Stick']][2] * MOVEMENT_DICT[STICK_DICT['Right Stick']][1] * right_stick[1])
        except TypeError:
            pass

        last_stick = current

    return last_stick


if __name__ == "__main__":
    raise ImportError(
        "This is not meant to be run as a main program, it is a supplementary module.")
