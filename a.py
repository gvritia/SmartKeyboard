import keyboard
import webbrowser
s = 0
k = []
for i in range(4):
    x = int(input("если вы хотите сохранить комбинацию на первую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
    k.append(x)
    if k[i] == 2:
        w1 = str(input("введите сылку страницы которую хотите сохранить - "))
        s = 1
        # keyboard.add_hotkey(f"{keys['ctrl']}+{keys['shift']}", lambda: keyboard.release(webbrowser.open_new_tab(w1)))
        # keys = '+'.join(key)
        keyboard.add_hotkey(key, lambda: keyboard.release(webbrowser.open_new_tab(w1)))
        # keyboard.add_hotkey(f"{key[0]}+{key[1]}", lambda: keyboard.release(webbrowser.open_new_tab(w1)))
        # keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.release(webbrowser.open_new_tab(w1)))
    elif k[i] == 1:
        print("Введите комбинацию - ")
        key = keyboard.read_hotkey(suppress=False)
        # key = str(key).split('+')
        # print(keyboard.is_pressed(key))
    elif k[i] == 0:
        print("0")

if s == 1:
    keyboard.wait()