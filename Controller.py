from time import time as timestamp, sleep
from threading import Thread
from XInput import *
from constants import *

def retrieve_controllers():
    controllers = get_connected()
    controller_ids = [controllers.index(i) for i in controllers if i]

    return controller_ids


def poll_controller():
    state = get_state(CONTROLLER_ID)
    triggers = get_trigger_values(state)
    sticks = get_thumb_values(state)
    events = get_events()

    return events, triggers, sticks


def vibrate_controller(left_speed, right_speed, vibrate_time):
    set_vibration(CONTROLLER_ID, left_speed, right_speed)
    sleep(vibrate_time)
    set_vibration(CONTROLLER_ID, 0, 0)

    return True


def button_handler(events, on):
    for event in events:
        if event.type == EVENT_BUTTON_PRESSED and on == True:
            if event.button == "LEFT_THUMB":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['L3']][0].press(
                    COMMAND_DICT[BUTTON_DICT['L3']][1])
                # print("L3 pressed") # For Debugging
                # print(f"{BUTTON_DICT['L3']} activated") # For Debugging
            elif event.button == "RIGHT_THUMB":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['R3']][0].press(
                    COMMAND_DICT[BUTTON_DICT['R3']][1])
                # print("R3 pressed") # For Debugging
                # print(f"{BUTTON_DICT['R3']} activated") # For Debugging

            elif event.button == "LEFT_SHOULDER":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['L1']][0].press(
                    COMMAND_DICT[BUTTON_DICT['L1']][1])
                # print("L1 pressed") # For Debugging
                # print(f"{BUTTON_DICT['L1']} activated") # For Debugging
            elif event.button == "RIGHT_SHOULDER":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['R1']][0].press(
                    COMMAND_DICT[BUTTON_DICT['R1']][1])
                # print("R1 pressed") # For Debugging
                # print(f"{BUTTON_DICT['R1']} activated") # For Debugging

            elif event.button == "BACK":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                # print("View pressed") # For Debugging

            elif event.button == "START":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['Menu']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Menu']][1])
                # print("Menu pressed") # For Debugging
                # print(f"{BUTTON_DICT['Menu']} activated") # For Debugging

            elif event.button == "DPAD_LEFT":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['Left']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Left']][1])
                # print("Left pressed") # For Debugging
                # print(f"{BUTTON_DICT['Left']} activated") # For Debugging
            elif event.button == "DPAD_RIGHT":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['Right']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Right']][1])
                # print("Right pressed") # For Debugging
                # print(f"{BUTTON_DICT['Right']} activated") # For Debugging
            elif event.button == "DPAD_UP":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['Up']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Up']][1])
                # print("Up pressed") # For Debugging
                # print(f"{BUTTON_DICT['Up']} activated") # For Debugging
            elif event.button == "DPAD_DOWN":
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['Down']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Down']][1])
                # print("Down pressed") # For Debugging
                # print(f"{BUTTON_DICT['Down']} activated") # For Debugging

            elif event.button == "A":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['A']][0].press(
                    COMMAND_DICT[BUTTON_DICT['A']][1])
                # print("A pressed") # For Debugging
                # print(f"{BUTTON_DICT['A']} activated") # For Debugging
            elif event.button == "B":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['B']][0].press(
                    COMMAND_DICT[BUTTON_DICT['B']][1])
                # print("B pressed") # For Debugging
                # print(f"{BUTTON_DICT['B']} activated") # For Debugging
            elif event.button == "Y":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['Y']][0].press(
                    COMMAND_DICT[BUTTON_DICT['Y']][1])
                # print("Y pressed") # For Debugging
                # print(f"{BUTTON_DICT['Y']} activated") # For Debugging
            elif event.button == "X":
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_BUTTON_TIME,))
                COMMAND_DICT[BUTTON_DICT['X']][0].press(
                    COMMAND_DICT[BUTTON_DICT['X']][1])
                # print("X pressed") # For Debugging
                # print(f"{BUTTON_DICT['X']} activated") # For Debugging

        elif event.type == EVENT_BUTTON_RELEASED and on == True:
            if event.button == "LEFT_THUMB":
                COMMAND_DICT[BUTTON_DICT['L3']][0].release(
                    COMMAND_DICT[BUTTON_DICT['L3']][1])
                # print("L3 released") # For Debugging
                # print(f"{BUTTON_DICT['L3']} deactivated") # For Debugging
            elif event.button == "RIGHT_THUMB":
                COMMAND_DICT[BUTTON_DICT['R3']][0].release(
                    COMMAND_DICT[BUTTON_DICT['R3']][1])
                # print("R3 released") # For Debugging
                # print(f"{BUTTON_DICT['R3']} deactivated") # For Debugging

            elif event.button == "LEFT_SHOULDER":
                COMMAND_DICT[BUTTON_DICT['L1']][0].release(
                    COMMAND_DICT[BUTTON_DICT['L1']][1])
                # print("L1 released") # For Debugging
                # print(f"{BUTTON_DICT['L1']} deactivated") # For Debugging
            elif event.button == "RIGHT_SHOULDER":
                COMMAND_DICT[BUTTON_DICT['R1']][0].release(
                    COMMAND_DICT[BUTTON_DICT['R1']][1])
                # print("R1 released") # For Debugging
                # print(f"{BUTTON_DICT['R1']} deactivated") # For Debugging

            elif event.button == "BACK":
                on = False
                # print("View released") # For Debugging
                # print("controller input off") # For Debugging
            elif event.button == "START":
                COMMAND_DICT[BUTTON_DICT['Menu']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Menu']][1])
                # print("Menu released") # For Debugging
                # print(f"{BUTTON_DICT['Menu']} deactivated") # For Debugging

            elif event.button == "DPAD_LEFT":
                COMMAND_DICT[BUTTON_DICT['Left']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Left']][1])
                # print("Left released") # For Debugging
                # print(f"{BUTTON_DICT['Left']} deactivated") # For Debugging
            elif event.button == "DPAD_RIGHT":
                COMMAND_DICT[BUTTON_DICT['Right']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Right']][1])
                # print("Right released") # For Debugging
                # print(f"{BUTTON_DICT['Right']} deactivated") # For Debugging
            elif event.button == "DPAD_UP":
                COMMAND_DICT[BUTTON_DICT['Up']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Up']][1])
                # print("Up released") # For Debugging
                # print(f"{BUTTON_DICT['Up']} deactivated") # For Debugging
            elif event.button == "DPAD_DOWN":
                COMMAND_DICT[BUTTON_DICT['Down']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Down']][1])
                # print("Down released") # For Debugging
                # print(f"{BUTTON_DICT['Down']} deactivated") # For Debugging

            elif event.button == "A":
                COMMAND_DICT[BUTTON_DICT['A']][0].release(
                    COMMAND_DICT[BUTTON_DICT['A']][1])
                # print("A released") # For Debugging
                # print(f"{BUTTON_DICT['A']} deactivated") # For Debugging
            elif event.button == "B":
                COMMAND_DICT[BUTTON_DICT['B']][0].release(
                    COMMAND_DICT[BUTTON_DICT['B']][1])
                # print("B released") # For Debugging
                # print(f"{BUTTON_DICT['B']} deactivated") # For Debugging
            elif event.button == "Y":
                COMMAND_DICT[BUTTON_DICT['Y']][0].release(
                    COMMAND_DICT[BUTTON_DICT['Y']][1])
                # print("Y released") # For Debugging
                # print(f"{BUTTON_DICT['Y']} deactivated") # For Debugging
            elif event.button == "X":
                COMMAND_DICT[BUTTON_DICT['X']][0].release(
                    COMMAND_DICT[BUTTON_DICT['X']][1])
                # print("X released") # For Debugging
                # print(f"{BUTTON_DICT['X']} deactivated") # For Debugging

        elif event.type == EVENT_BUTTON_PRESSED and on == False:
            if event.button == "BACK":
                t = Thread(target=vibrate_controller, args=(
                    0, LEFT_SPEED, 0, VIBRATE_BUTTON_TIME,))
                # print("view pressed") # For Debugging

        elif event.type == EVENT_BUTTON_RELEASED and on == False:
            if event.button == "BACK":
                on = True
                # print("view released") # For Debugging
                # print("controller input on") # For Debugging

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
                # print("L2 state:", l2)
                t = Thread(target=vibrate_controller, args=(
                    LEFT_SPEED, 0, VIBRATE_TRIGGER_TIME,))
                COMMAND_DICT[BUTTON_DICT['L2']][0].press(
                    COMMAND_DICT[BUTTON_DICT['L2']][1])
                # print("L2 pressed") # For Debugging
                # print(f"{BUTTON_DICT['L2']} activated") # For Debugging
                l2_pressed = True
            elif l2_pressed == True:
                COMMAND_DICT[BUTTON_DICT['L2']][0].release(
                    COMMAND_DICT[BUTTON_DICT['L2']][1])
                # print("L2 released") # For Debugging
                # print(f"{BUTTON_DICT['L2']} deactivated") # For Debugging
                l2_pressed = False
        except TypeError:
            pass

        try:
            if r2 != 0:
                # print("R2 state:", r2)
                t = Thread(target=vibrate_controller, args=(
                    0, RIGHT_SPEED, VIBRATE_TRIGGER_TIME,))
                COMMAND_DICT[BUTTON_DICT['R2']][0].press(
                    COMMAND_DICT[BUTTON_DICT['R2']][1])
                # print("R2 pressed") # For Debugging
                # print(f"{BUTTON_DICT['R2']} activated") # For Debugging
                r2_pressed = True
            elif r2_pressed == True:
                COMMAND_DICT[BUTTON_DICT['R2']][0].release(
                    COMMAND_DICT[BUTTON_DICT['R2']][1])
                # print("R2 released") # For Debugging
                # print(f"{BUTTON_DICT['R2']} deactivated") # For Debugging
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
                # print("Left Stick state:", left_stick) # For Debugging
                MOVEMENT_DICT[STICK_DICT['Left Stick']][0](MOVEMENT_DICT[STICK_DICT['Left Stick']][2] * left_stick[0],
                                                           MOVEMENT_DICT[STICK_DICT['Left Stick']][2] * MOVEMENT_DICT[STICK_DICT['Left Stick']][1] * left_stick[1])
        except TypeError:
            pass

        try:
            if right_stick[0] != 0 and right_stick[1] != 0:
                # print("Right stick state:", right_stick) # For Debugging
                MOVEMENT_DICT[STICK_DICT['Right Stick']][0](MOVEMENT_DICT[STICK_DICT['Right Stick']][2] * right_stick[0],
                                                            MOVEMENT_DICT[STICK_DICT['Right Stick']][2] * MOVEMENT_DICT[STICK_DICT['Right Stick']][1] * right_stick[1])
        except TypeError:
            pass

        last_stick = current

    return last_stick


if __name__ == "__main__":
    raise ImportError(
        "This is not meant to be run as a main program, it is a supplementary module.")
