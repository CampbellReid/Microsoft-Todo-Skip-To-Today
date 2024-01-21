import tkinter as tk
import pyautogui
import os
import datetime
import cv2
import numpy as np
import argparse
import signal

def find_template_location(screenshot, template):
    # Convert the screenshot and template images to grayscale
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(np.array(template), cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + template_gray.shape[1], top_left[1] + template_gray.shape[0])

    # Calculate the center point
    center_x = (top_left[0] + bottom_right[0]) // 2
    center_y = (top_left[1] + bottom_right[1]) // 2

    return center_x, center_y

def button_clicked():
    # Get the current directory where the main.py file is located
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Generate a unique filename using the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    # Save the screenshot in the current directory with the unique filename
    screenshot_path = os.path.join(current_directory, filename)
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f"Screenshot saved as {screenshot_path}")

    # Load the template image
    template = cv2.imread("template.png")

    # Perform template matching using the screenshot and template
    center_x, center_y = find_template_location(np.array(screenshot), template)
    print(f"Template found at ({center_x}, {center_y})")

    # Get the current mouse position
    original_x, original_y = pyautogui.position()

    # Click on the center positions
    pyautogui.click(center_x, center_y)

    # Click on the specified position
    pyautogui.click(click_x, click_y)

    # Return the mouse to the original position
    pyautogui.moveTo(original_x, original_y)

    # Delete the screenshot file after it has been used
    os.remove(screenshot_path)
    print(f"Screenshot {screenshot_path} deleted")

template = cv2.imread("template.png")

# Location of the place to click first
parser = argparse.ArgumentParser(description='Process command line inputs.')
parser.add_argument('--click_x', type=int, default=1026, help='X-coordinate of the click position')
parser.add_argument('--click_y', type=int, default=201, help='Y-coordinate of the click position')
args = parser.parse_args()

click_x = args.click_x
click_y = args.click_y

window = tk.Tk()

# https://stackoverflow.com/a/66788780
def signal_handler(signal, frame):
    window.destroy()
    
def check():
    window.after(500, check)  #  time in ms.

signal.signal(signal.SIGINT, signal_handler)
window.geometry("800x600")  # Set the window size to 800x600 pixels

button = tk.Button(window, text="Checkoff item", command=button_clicked)
button.pack()

# this let's the terminal ^C get sampled every so often
window.after(500, check)  #  time in ms.

window.bind_all('<Control-c>', signal_handler)
 
window.mainloop()