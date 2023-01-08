import keyboard
import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Radiobutton
# from time import sleep


def web_link1():
    keyboard.add_hotkey("ctrl + alt + shift + win + 1",
                        lambda: keyboard.release(webbrowser.open_new_tab(EnterText1.get())))


def web_link2():
    keyboard.add_hotkey("ctrl + alt + shift + win + 2",
                        lambda: keyboard.release(webbrowser.open_new_tab(EnterText2.get())))


def web_link3():
    keyboard.add_hotkey("ctrl + alt + shift + win + 3",
                        lambda: keyboard.release(webbrowser.open_new_tab(EnterText3.get())))


def web_link4():
    keyboard.add_hotkey("ctrl + alt + shift + win + 4",
                        lambda: keyboard.release(webbrowser.open_new_tab(EnterText4.get())))


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.title("Приложение")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost")

window.geometry('700x700')

window["bg"] = "gray"
idea = tk.Label(window, text="text", font=("Arial Bold", 15), fg="white", bg="gray")
idea.place(x=325, y=25)

EnterText1 = tk.Entry(fg="black", width=50)
EnterText1.place(x=220, y=65)

btn1 = tk.Button(window, text="Сохранить", command=web_link1, width="40", height="2",
                 fg="black", bg="white")
btn1.place(x=220, y=110)

EnterText2 = tk.Entry(fg="black", width=50)
EnterText2.place(x=220, y=175)

btn2 = tk.Button(window, text="Сохранить", command=web_link2, width="40", height="2",
                 fg="black", bg="white")
btn2.place(x=220, y=220)

EnterText3 = tk.Entry(fg="black", width=50)
EnterText3.place(x=220, y=285)

btn3 = tk.Button(window, text="Сохранить", command=web_link3, width="40", height="2",
                 fg="black", bg="white")
btn3.place(x=220, y=330)

EnterText4 = tk.Entry(fg="black", width=50)
EnterText4.place(x=220, y=395)

btn4 = tk.Button(window, text="Сохранить", command=web_link4, width="40", height="2",
                 fg="black", bg="white")
btn4.place(x=220, y=440)



rad1 = Radiobutton(window, text='Первый', value=1)
rad2 = Radiobutton(window, text='Второй', value=2)
rad3 = Radiobutton(window, text='Третий', value=3)


rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

rad1.place(x=220, y= 420)




window.mainloop()

while True:
    keyboard.wait()
# s = 1
# k1 = int(input(
#     "если вы хотите сохранить комбинацию на первую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
# if k1 == 2:
#     w1 = str(input("введите сылку страницы которую хотите сохранить - "))
#     s = 1
#     keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.release(webbrowser.open_new_tab(w1)))
# elif k1 == 1:
#     print(f"Введите комбинацию - ")
#     sleep(1)
#     key = keyboard.read_hotkey(suppress=False)
#     print(key)
#     keyboard.add_hotkey("ctrl + alt + shift + win + 1", lambda: keyboard.press(key))
# elif k1 == 0:
#     print("0")
# k2 = int(input(
#     "если вы хотите сохранить комбинацию на вторую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
# if k2 == 2:
#     w2 = str(input("введите сылку страницы которую хотите сохранить - "))
#     s = 1
#     keyboard.add_hotkey("ctrl + alt + shift + win + 2", lambda: keyboard.release(webbrowser.open_new_tab(w2)))
# elif k2 == 1:
#     print(f"Введите комбинацию - ")
#     sleep(1)
#     key = keyboard.read_hotkey(suppress=False)
#     print(key)
#     keyboard.add_hotkey("ctrl + alt + shift + win + 2", lambda: keyboard.press(f"{key}"))
# elif k2 == 0:
#     print("0")
# k3 = int(input(
#     "если вы хотите сохранить комбинацию на третью клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
# if k3 == 2:
#     w3 = str(input("введите сылку страницы которую хотите сохранить - "))
#     s = 1
#     keyboard.add_hotkey("ctrl + alt + shift + win + 3", lambda: keyboard.release(webbrowser.open_new_tab(w3)))
# elif k3 == 1:
#     print(f"Введите комбинацию - ")
#     sleep(1)
#     key = keyboard.read_hotkey(suppress=False)
#     print(key)
#     keyboard.add_hotkey("ctrl + alt + shift + win + 3", lambda: keyboard.press(f"{key}"))
# elif k3 == 0:
#     print("0")
# k4 = int(input(
#     "если вы хотите сохранить комбинацию на четвёртую клавишу клавиатуры введит 1, если вы хотите сохранить сылку на веб страницу на клавишу введите 2, если вы не хотите ничего записывать введите 0 - "))
# if k4 == 2:
#     w4 = str(input("введите сылку страницы которую хотите сохранить - "))
#     s = 1
#     keyboard.add_hotkey("ctrl + alt + shift + win + 4", lambda: keyboard.release(webbrowser.open_new_tab(w4)))
# elif k4 == 1:
#     print(f"Введите комбинацию - ")
#     sleep(1)
#     key = keyboard.read_hotkey(suppress=False)
#     print(key)
#     keyboard.add_hotkey("ctrl + alt + shift + win + 4", lambda: keyboard.press(f"{key}"))
# elif k4 == 0:
#     print("0")
# if s == 1:
#     keyboard.wait()
