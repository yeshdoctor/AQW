from pynput import keyboard
from pynput.mouse import Button, Controller
import time
mouse = Controller()
import pynput
from pynput.keyboard import Controller,Key
kb = Controller()

time.sleep(5)
count = 0
max_no_spins = 338
while (count<max_no_spins):
    mouse.position = (3383.07421875, 76.0078125)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(5)
    for i in range(0,20):
        mouse.position = (3498.734375, 184.4140625)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(5)
        mouse.position = (3000.31640625, 928.69921875)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        max_no_spins = max_no_spins + 1
    mouse.position = (3789.97265625, 39.40625)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    for i in range(0, 20):
        mouse.position = (3068.765625, 255.13671875)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(10)