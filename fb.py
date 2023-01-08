import keyboard
import webbrowser
from time import sleep
s = 1
k1 = int(input("если вы хотите сохранить комбинацию на первую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
if k1 == 2:
    w1 = str(input("введите сылку страницы которую хотите сохранить - "))
    s = 1
    keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.release(webbrowser.open_new_tab(w1)))
elif k1 == 1:
    print(f"Введите комбинацию - ")
    sleep(1)
    key = keyboard.read_hotkey(suppress=False)
    print(key)
    keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.press(key))
elif k1 == 0:
    print("0")
k2 = int(input("если вы хотите сохранить комбинацию на вторую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
if k2 == 2:
    w2 = str(input("введите сылку страницы которую хотите сохранить - "))
    s = 1
    keyboard.add_hotkey("ctrl + alt + shift + win + 2", lambda: keyboard.release(webbrowser.open_new_tab(w2)))
elif k2 == 1:
    print(f"Введите комбинацию - ")
    sleep(1)
    key = keyboard.read_hotkey(suppress=False)
    print(key)
    keyboard.add_hotkey("ctrl + alt + shift + win + 2", lambda: keyboard.press(f"{key}"))
elif k2 == 0:
    print("0")
k3 = int(input("если вы хотите сохранить комбинацию на третью клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
if k3 == 2:
    w3 = str(input("введите сылку страницы которую хотите сохранить - "))
    s = 1
    keyboard.add_hotkey("ctrl + alt + shift + win + 3", lambda: keyboard.release(webbrowser.open_new_tab(w3)))
elif k3 == 1:
    print(f"Введите комбинацию - ")
    sleep(1)
    key = keyboard.read_hotkey(suppress=False)
    print(key)
    keyboard.add_hotkey("ctrl + alt + shift + win + 3", lambda: keyboard.press(f"{key}"))
elif k3 == 0:
    print("0")
k4 = int(input("если вы хотите сохранить комбинацию на четвёртую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
if k4 == 2:
    w4 = str(input("введите сылку страницы которую хотите сохранить - "))
    s = 1
    keyboard.add_hotkey("ctrl + alt + shift + win + 4", lambda: keyboard.release(webbrowser.open_new_tab(w4)))
elif k4 == 1:
    print(f"Введите комбинацию - ")
    sleep(1)
    key = keyboard.read_hotkey(suppress=False)
    print(key)
    keyboard.add_hotkey("ctrl + alt + shift + win + 4", lambda: keyboard.press(f"{key}"))
elif k4 == 0:
    print("0")
if s == 1:
    keyboard.wait()
