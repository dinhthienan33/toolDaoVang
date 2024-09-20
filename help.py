import pyautogui
import time

print("Move your mouse to the desired location. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped.")