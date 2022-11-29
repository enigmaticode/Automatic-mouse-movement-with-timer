#python 3.9

import threading
import pyautogui, time
from pynput.keyboard import Listener, Key
from pynput import keyboard

break_program = False

def timer(seconds, event1):
    while seconds > 0 and not event1.is_set():
        time.sleep(1)
        seconds -= 1
        print(seconds)
        if seconds == 0:
            on_press(keyboard.Key.esc)

def on_press(key):
    global break_program
    print(key)
    if key == keyboard.Key.esc:
        print('esc pressed')
        break_program = True
        return False

def mouse(event1):
    pyautogui.moveTo(500, 500)
    while break_program == False:
        pyautogui.move(0, 50)
        time.sleep(3)
        pyautogui.move(0, -50)
        time.sleep(3)
    event1.set()

def move(event1):
    with keyboard.Listener(on_press=on_press) as listener:
        mouse(event1)

event1 = threading.Event()

enable_timer = input('Do you want to use the timer? Y or N: ').upper()
if enable_timer == 'Y':
    seconds = int(input("Enter the seconds: "))
    t1 = threading.Thread(target=timer, args=(seconds, event1)).start()
    t2 = threading.Thread(target=move, args=(event1,)).start()
elif enable_timer == 'N':
    move(event1)
else: print("wrong choice!")



