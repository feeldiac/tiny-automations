import datetime
import time
import pyautogui
import pygetwindow as gw
import pyperclip

# The main objective of this automation is to avoid me to
# enter to my job's discord and say good morning or whatever.


def getMessage():
    dicc = {
        0: {"spanishName": "Lunes"},
        1: {"spanishName": "Martes"},
        2: {"spanishName": "Miércoles"},
        3: {"spanishName": "Jueves"},
        4: {"spanishName": "Viernes"},
        5: {"spanishName": "Sábado"},
        6: {"spanishName": "Domingo"},
    }

    weekday = datetime.datetime.today().weekday()
    today = dicc[weekday]["spanishName"].lower()

    return f"Buenos días, feliz {today}."


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

    message = getMessage()

    # Use pyperclip to ensure accents
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
else:
    print("👎 Unable to find the channel.")
