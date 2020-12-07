from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()
import pynput
from pynput.keyboard import Controller

kb = Controller()


def escape(button):
    if button == keyboard.Key.esc:
        pos = mouse.position
        mouse.position = (844.64453125, 39.41015625)  # adjust according to X position
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = pos


def ncm(button):
    if keyboard.KeyCode(char='0') == button:  # right corner
        pos = mouse.position
        mouse.position = (3548.46875, 389.28125)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = pos
    if keyboard.KeyCode(char='9') == button:  # left corner
        pos = mouse.position
        mouse.position = (1705.36328125, 390.80078125)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = pos


one = 0
two = 0
three = 0
four = 0
five = 0


def key_spam(button):
    global one, two, three, four, five
    if button == keyboard.KeyCode(char='1'):
        one += 1
        if one == 1:
            kb.tap('1')
            kb.tap('1')
        if one == 3:
            one = 0
    if button == keyboard.KeyCode(char='2'):
        two += 1
        if two == 1:
            kb.tap('2')
            kb.tap('2')
        if two == 3:
            two = 0
    if button == keyboard.KeyCode(char='3'):
        three += 1
        if three == 1:
            kb.tap('3')
            kb.tap('3')
        if three == 3:
            three = 0
    if button == keyboard.KeyCode(char='4'):
        four += 1
        if four == 1:
            kb.tap('4')
            kb.tap('4')
        if four == 3:
            four = 0
    if button == keyboard.KeyCode(char='5'):
        five += 1
        if five == 1:
            kb.tap('5')
            kb.tap('5')
        if five == 3:
            five = 0

def on_press(button):
    escape(button)
    #ncm(button)
    key_spam(button)


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
