import keyboard
import webbrowser
keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.release(webbrowser.open_new_tab('https://www.youtube.com/')))
keyboard.wait()