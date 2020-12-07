from pynput.mouse import Listener

xx, yy = 0, 0

def on_click(x, y, button, pressed):
    global xx, yy
    xx, yy = x, y
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


with Listener(on_click=on_click) as listener:
    listener.join()
    # here you can read xx and yy