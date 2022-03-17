from XInput import *
from pynput.mouse import Controller as Mouse, Button
from pynput.keyboard import Controller as Keyboard, Key
from time import time, sleep
from threading import Thread

mouse = Mouse()
keyboard = Keyboard()

def poll_controller(user_index):
    try:
        get_state(user_index)
    except XInputNotConnectedError:
        input("Controller may not be connected, try checking the connection and hit enter to check again.")
        poll_controller(user_index)
    
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
    LEFT_SPEED = 0.5
    RIGHT_SPEED = 0.1
    VIBRATE_TIME = 0.2

    for event in events:            
        if event.type == EVENT_BUTTON_PRESSED and on == True:
            if event.button == "LEFT_THUMB":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                keyboard.press(Key.backspace)
                print("L3 pressed")
                print("backspace key activated")
            elif event.button == "RIGHT_THUMB":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                keyboard.press(Key.enter)
                print("R3 pressed")
                print("enter key activated")

            elif event.button == "LEFT_SHOULDER":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                keyboard.press(Key.ctrl)
                print("L1 pressed")
                print("ctrl key activated")
            elif event.button == "RIGHT_SHOULDER":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                keyboard.press(Key.shift)
                print("R1 pressed")
                print("shift key activated")

            elif event.button == "BACK":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                print("select pressed")
                
            elif event.button == "START":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                keyboard.press(Key.cmd)
                print("start pressed")
                print("start key activated")

            elif event.button == "DPAD_LEFT":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                keyboard.press(Key.left)
                print("left pressed")
                print("left key activated")
            elif event.button == "DPAD_RIGHT":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                keyboard.press(Key.right)
                print("right pressed")
                print("right key activated")
            elif event.button == "DPAD_UP":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                keyboard.press(Key.up)
                print("up pressed")
                print("up key activated")
            elif event.button == "DPAD_DOWN":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                keyboard.press(Key.down)
                print("down pressed")
                print("down key activated")

            elif event.button == "A":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                mouse.press(Button.left)
                print("cross pressed")
                print("left click activated")
            elif event.button == "B":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                mouse.press(Button.right)
                print("circle pressed")
                print("right click activated")
            elif event.button == "Y":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                mouse.press(Button.middle)
                print("triangle pressed")
                print("middle click activated")
            elif event.button == "X":
                t = Thread(target=vibrate_controller, args=(0,0,RIGHT_SPEED,VIBRATE_TIME,))
                print("square pressed")
                print("double click activated")

        elif event.type == EVENT_BUTTON_RELEASED and on == True:
            if event.button == "LEFT_THUMB":
                keyboard.release(Key.backspace)
                print("L3 released")
                print("backspace key deactivated")
            elif event.button == "RIGHT_THUMB":
                keyboard.release(Key.enter)
                print("R3 released")
                print("enter key deactivated")

            elif event.button == "LEFT_SHOULDER":
                keyboard.release(Key.ctrl)
                print("L1 released")
                print("ctrl key deactivated")
            elif event.button == "RIGHT_SHOULDER":
                keyboard.release(Key.shift)
                print("R1 released")
                print("shift key deactivated")

            elif event.button == "BACK":
                on = False
                print("select released")
                print("controller input off")
            elif event.button == "START":
                keyboard.release(Key.cmd)
                print("start released")
                print("start key deactivated")

            elif event.button == "DPAD_LEFT":
                keyboard.release(Key.left)
                print("left released")
                print("left key deactivated")
            elif event.button == "DPAD_RIGHT":
                keyboard.release(Key.right)
                print("right released")
                print("right key deactivated")
            elif event.button == "DPAD_UP":
                keyboard.release(Key.up)
                print("up released")
                print("up key deactivated")
            elif event.button == "DPAD_DOWN":
                keyboard.release(Key.down)
                print("down released")
                print("down key deactivated")

            elif event.button == "A":
                mouse.release(Button.left)
                print("cross released")
                print("left click deactivated")
            elif event.button == "B":
                mouse.release(Button.right)
                print("circle released")
                print("right click deactivated")
            elif event.button == "Y":
                mouse.release(Button.middle)
                print("triangle released")
                print("middle click deactivated")
            elif event.button == "X":
                mouse.click(Button.left, 2)
                print("square released")
                print("double click deactivated")
        
        elif event.type == EVENT_BUTTON_PRESSED and on == False:
            if event.button == "BACK":
                t = Thread(target=vibrate_controller, args=(0,LEFT_SPEED,0,VIBRATE_TIME,))
                print("select pressed")

        elif event.type == EVENT_BUTTON_RELEASED and on == False:
            if event.button == "BACK":
                on = True
                print("select released")
                print("controller input on")


    try:
        t.start()
    except UnboundLocalError:
        pass

    return on

def trigger_handler(triggers, last_trigger):
    l2 = triggers[0]
    r2 = triggers[1]

    current = time()
    tick = current - last_trigger
    
    if tick >= 0.01:
        if l2 != 0:
            print("L2 state:", l2)
        if r2 != 0:
            print("R2 state:", r2)
        last_trigger = current

    return last_trigger

def stick_handler(sticks, last_stick):
    MOVE_SPEED = 10
    SCROLL_SPEED = 0.5
    
    stick1 = sticks[0]
    stick2 = sticks[1]

    current = time()
    tick = current - last_stick
    
    if tick >= 0.01:
        if stick1[0] != 0 and stick1[1] != 0:
            print("left stick state:", stick1)

        if stick2[0] != 0 and stick2[1] != 0:
            print("right stick state:", stick2)

        try:
            mouse.move(MOVE_SPEED * stick1[0], MOVE_SPEED * -stick1[1])
            mouse.scroll(SCROLL_SPEED * stick2[0], SCROLL_SPEED * stick2[1])
        except TypeError:
            pass

        last_stick = current

    return last_stick

def main():
    on = True
    last_stick = time()
    last_trigger = time()
    while True:
        events, triggers, sticks = poll_controller(0)
        on = button_handler(events, on)
        if on == True:
            last_trigger = trigger_handler(triggers, last_trigger)
            last_stick = stick_handler(sticks, last_stick)            

if __name__ == "__main__":
    main()
else:
    raise ImportError("This is not meant to be imported as a module, only as a prototype program for testing")