#!/usr/bin/python3
from pynput import keyboard
import pyautogui 
pyautogui.FAILSAFE = False

x = 500
y = 500

steps = 25
detached = False
b_steps = 0

def all_down():
    global y
    y = pyautogui.size()[1] - 25
    pyautogui.moveTo(x, y) 


def all_up():
    global y
    y = 25
    pyautogui.moveTo(x, y)

def end_of_line():
    global x
    x = pyautogui.size()[0] - 25
    pyautogui.moveTo(x, y)


def begin_of_line():
    global x
    x = 25
    pyautogui.move(x, y)


def up_right():
    all_up()
    end_of_line()


def up_left():
    all_up()
    begin_of_line()


def down_right():
    all_down()
    end_of_line()


def down_left():
    all_down()
    begin_of_line()


def detach_mouse():
    global steps
    global detached
    global b_steps 

    if detached:
        steps = b_steps
        detached = False
    else:
        b_steps = steps
        steps = 0
        detached = True

def slow_down():
    global steps
    steps -= 5


def speed_up():
    global steps
    steps += 5


def move_down():
    global y
    global steps
    y += steps
    pyautogui.moveTo(x, y)


def move_up():
    global y
    global steps 
    y -= steps
    pyautogui.moveTo(x, y)


def move_right():
    global x
    global steps
    x += steps
    pyautogui.moveTo(x, y)


def move_left():
    global x
    global steps
    x -= steps
    pyautogui.moveTo(x, y)


def click():
    pyautogui.click()


def on_press(key):
    try:
        if key.char == 'k': move_up()
        elif key.char == 'j': move_down()
        elif key.char == 'l': move_right()
        elif key.char == 'h': move_left()
        elif key.char == '$': end_of_line()
        elif key.char == '^': begin_of_line()
        elif key.char == 'g': slow_down()
        elif key.char == 'f': speed_up()
        elif key.char == 'u': all_up()
        elif key.char == 'd': all_down()
        elif key.char == 'w': up_right()
        elif key.char == 'q': up_left()
        elif key.char == 'a': down_left()
        elif key.char == 's': down_right()
    except AttributeError:
        if  key == keyboard.Key.enter or key == keyboard.Key.space:
            click()
        if key == keyboard.Key.esc:
            detach_mouse()

def on_release(key):
    if key == keyboard.Key.f1:
        return False

# Collect events until released
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
