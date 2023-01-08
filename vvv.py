import keyboard
#import webbrowser
print(f"Введите комбинацию - ")
key = keyboard.read_hotkey(suppress=True)
print(key)
keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.press("ctrl + a"))
keyboard.wait()
# w1 = str(input("введите сылку страницы которую хотите сохранить - "))
# keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.release(webbrowser.open_new_tab(w1)))
# keyboard.wait()