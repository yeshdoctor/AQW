from PIL import ImageGrab
import matplotlib.pyplot as plt
import numpy as np
import time
from pynput import keyboard
from pynput.mouse import Button, Controller
import pyautogui

mouse = Controller()
import pynput
from pynput.keyboard import Controller, Key

kb = Controller()
x_top_right = 412  ##42,49,
y_top_right = 49
x_bottom_left = 42
y_bottom_left = 371
heal_x = 918
heal_y = 1001
background = (x_bottom_left, y_top_right, x_top_right, y_bottom_left)


def create_bboxes(x_top_right, y_top_right, x_bottom_left, y_bottom_left):
    x_weights = [0.42085350772390956, 0.9805592236265694, 0.02898824121234987, 0.5350772390953489, 0.025026724517386658,
                 0.5349514766605882, 0.028569033096480748, 0.5363139030371628]
    y_weights = [0.1584775843625401, 0.20471895361275894, 0.4344549256053681, 0.46948847612564426, 0.6624282796849168,
                 0.6982519692696684, 0.8847977243994943, 0.9310998735777497]
    x_dist = x_top_right - x_bottom_left
    y_dist = y_bottom_left - y_top_right
    boxes = []
    for i in range(0, 4):
        j = 2 * i
        left = round(x_bottom_left + x_dist * x_weights[j]) - x_bottom_left
        top = round(y_top_right + y_dist * y_weights[j]) - 6 - y_top_right
        right = round(x_bottom_left + x_dist * x_weights[j + 1]) - x_bottom_left
        bottom = round(y_top_right + y_dist * y_weights[j + 1]) - y_top_right
        bbox = (int(left), int(right), int(top), int(bottom))
        #print(bbox)
        boxes.append(bbox)
    return boxes


def get_pos(hb):
    pos = []
    for i, val in enumerate(hb):
        if i == 0: continue
        l, r, t, b = val
        pos.append((int((l + r) / 2),int( (t + b) / 2)))
    return pos


hb = create_bboxes(x_top_right, y_top_right, x_bottom_left, y_bottom_left)

mouse_loc = {
    1: (143.26953125, 201.6015625),
    2: (145.5234375, 279.359375),
    3: (139.60546875, 351.10546875)
}

#print(mouse_loc)
t1 = time.time()
im = np.array(ImageGrab.grab(bbox=background))
print(im.shape)
#plt.imshow(im)
#plt.show()
background_red_vales = np.empty(4)
for i, box in enumerate(hb):
    #print(box)
    l, r, t, b = box
    # print(l,r,t,b)
    plt.imshow(im[t:b,l:r,:])
    background_red_vales[i] = np.mean(im[t:b, l:r, 0])
    plt.show()
print("BG RED: ")
print(background_red_vales)

def on_press(button):
    if keyboard.KeyCode(char=']') == button:
        image = np.array(ImageGrab.grab(bbox=background))
        local_red = np.empty(4)
        for i, box in enumerate(hb):
            l, r, t, b = box
            # print(l,r,t,b)
            # plt.imshow(im[t:b,l:r,:])
            local_red[i] = np.mean(image[t:b, l:r, 0]) / background_red_vales[i]
        hot = np.argmin(local_red)
        print ("LOCAL RED:")
        print(local_red)
        print(hot)
        if hot == 0:
            kb.tap('3')
        else:
            c_pos = pyautogui.position()
            pyautogui.keyDown('shift')
            time.sleep(0.05)
            pyautogui.click(mouse_loc[hot])
            time.sleep(0.05)
            pyautogui.keyUp('shift')
            pyautogui.click(heal_x,heal_y)
            pyautogui.moveTo(c_pos)
            pyautogui.press('esc')

with pynput.keyboard.Listener(on_press=on_press) as listener: listener.join()
