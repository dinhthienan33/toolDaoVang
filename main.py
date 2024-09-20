import pyautogui
import pygetwindow as gw
import time
import config

def main():
    try:
        # Step 2: Find the application window
        app_name = config.app_name
        window = gw.getWindowsWithTitle(app_name)[0]

        # Step 3: Bring the window to the foreground
        window.activate()

        # Step 4: Run the script for the specified duration
        start_time = time.time()
        duration = config.duration

        # Example coordinates for the click (replace with actual coordinates)
        click_x, click_y = config.click_x, config.click_y
        INTERVAL = config.INTERVAL  # Interval between clicks (adjust as needed)

        # Step 5: Simulate mouse clicks without moving the mouse
        while time.time() - start_time < duration:
            pyautogui.click(click_x, click_y, button='left')
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()