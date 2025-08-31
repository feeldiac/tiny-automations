import pygetwindow as gw
import pyautogui
import pyperclip
import time

# Get all open windows
wins = gw.getWindowsWithTitle("Discord")

# Filter with "#stuff" word (just for testing purpose with my Discord server)
discord_window = None
for w in wins:
    print("Detectado:", w.title)  # debug
    if "#stuff" in w.title:
        discord_window = w
        break

if discord_window:
    discord_window.activate()
    time.sleep(2)

    # Use pyperclip to ensure accents
    pyperclip.copy("¡Buenos días equipo! ☀️")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
else:
    print("No encontré la ventana del canal #stuff 😢")
