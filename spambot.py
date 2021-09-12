import pyautogui, time, pyperclip

# Short pause to position the mouse cursor
# where you want to spam (crtl c + ctrl v + enter)
time.sleep(5)

# Opening the file
file = open("text_spambot.txt", "r")

for word in file:
    # Using ctrl c + ctrl v to avoid special characters issues
    pyperclip.copy(word)
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
