import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at position ({x}, {y})")

listener = mouse.Listener(on_click=on_click)
listener.start()

try:
    while True:
        pyautogui.sleep(1)
except KeyboardInterrupt:
    listener.stop()
    listener.join()
