import streamlit as st
import pyautogui
import pygetwindow as gw
import time
import threading

# Function to run the auto-clicker
def auto_clicker(app_name, click_x, click_y, interval, duration):
    try:
        # Find the application window
        window = gw.getWindowsWithTitle(app_name)[0]

        # Bring the window to the foreground
        window.activate()

        # Run the script for the specified duration
        start_time = time.time()

        # Simulate mouse clicks without moving the mouse
        while time.time() - start_time < duration:
            pyautogui.click(click_x, click_y, button='left', duration=0)
            time.sleep(interval)
    except KeyboardInterrupt:
        st.write("\nProgram terminated by user.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

# Streamlit UI
st.title("Auto-Clicker Configuration")

app_name = st.text_input("Application Name", "TelegramDesktop")
click_x = st.number_input("Click X Coordinate", value=350)
click_y = st.number_input("Click Y Coordinate", value=636)
interval = st.number_input("Interval Between Clicks (seconds)", value=1.5)
duration = st.number_input("Duration to Run (seconds)", value=50)

if st.button("Start Auto-Clicker"):
    st.write("Auto-Clicker started...")
    threading.Thread(target=auto_clicker, args=(app_name, click_x, click_y, interval, duration)).start()