import time
import pyautogui
import pygetwindow as gw
import pyperclip

from src.discord_greetings_01.utils.message import get_message

# The main objective of this automation is to avoid me to
# enter to my job's discord and say good morning or whatever.

# Get all open windows
wins = gw.getWindowsWithTitle("Discord")

# Filter with "#stuff" word (just for testing purpose with my Discord server)
discord_window = None
for w in wins:
    print("👍 Detected this window: ", w.title)  # debug

    if "#stuff" in w.title:
        discord_window = w
        break

if discord_window:
    discord_window.activate()
    time.sleep(2)

    message = get_message()

    # Use pyperclip to ensure accents
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
else:
    print("👎 Unable to find the channel.")
