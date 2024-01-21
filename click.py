import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at position ({x}, {y})")

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()
pyautogui.sleep(10)  # Run the script for 1 hour (you can change the duration as needed)
