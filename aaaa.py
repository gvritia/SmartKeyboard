import keyboard
import webbrowser
keyboard.add_abbreviation("igj", keyboard.release(webbrowser.open_new_tab('https://www.youtube.com/')))
keyboard.wait()