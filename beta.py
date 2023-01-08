import keyboard
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from time import sleep


def web_link1():
    if selected.get() == 1:
        sleep(1)
        key = keyboard.read_hotkey(suppress=False)
        keyboard.add_hotkey("ctrl + win + NumLock", lambda: keyboard.press(key))
        lbl1_1.configure(text=key)
    if selected.get() == 2:
        keyboard.add_hotkey("ctrl + win + NumLock",
                            lambda: keyboard.release(webbrowser.open_new_tab(EnterText1.get())))
        lbl1_1.configure(text="Вы сохранили сылку на кливашу")
    if selected.get() == 3:
        lbl1_1.configure(text="Вы ничего не сохранили на кливашу")


def web_link2():
    if selected.get() == 4:
        sleep(1)
        key = keyboard.read_hotkey(suppress=False)
        lbl2_1.configure(text=key)
        keyboard.add_hotkey("ctrl + win + PageUp", lambda: keyboard.press(key))
    if selected.get() == 5:
        keyboard.add_hotkey("ctrl + win + PageUp",
                            lambda: keyboard.release(webbrowser.open_new_tab(EnterText2.get())))
    if selected.get() == 6:
        lbl2_2.configure(text="Вы ничего не сохранили на кливашу")


def web_link3():
    if selected.get() == 7:
        sleep(1)
        key = keyboard.read_hotkey(suppress=False)
        lbl3_1.configure(text=key)
        keyboard.add_hotkey("ctrl + win + PageDown", lambda: keyboard.press(key))
    if selected.get() == 8:
        keyboard.add_hotkey("ctrl + win + PageDown",
                            lambda: keyboard.release(webbrowser.open_new_tab(EnterText3.get())))
    if selected.get() == 9:
        lbl3_2.configure(text="Вы ничего не сохранили на кливашу")


def web_link4():
    if selected.get() == 10:
        sleep(1)
        key = keyboard.read_hotkey(suppress=False)
        lbl4_1.configure(text=key)
        keyboard.add_hotkey("ctrl + win + PageDown", lambda: keyboard.press(key))
    if selected.get() == 11:
        keyboard.add_hotkey("ctrl + alt + shift + win + 4",
                            lambda: keyboard.release(webbrowser.open_new_tab(EnterText4.get())))
    if selected.get() == 12:
        lbl4_2.configure(text="Вы ничего не сохранили на кливашу")


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()

# тело приложения
window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.title("Приложение")
window.resizable(width=True, height=True)
window.wm_attributes("-topmost")
window.geometry('700x700')
window["bg"] = "gray"
idea = tk.Label(window, text="text", font=("Arial Bold", 15), fg="white", bg="gray")
idea.place(x=325, y=25)

# отображение комбинации клавиш которую сохранил или когда ничего не сохраниили
lbl1_1 = tk.Label(window)
lbl1_1.place(x=325, y=500)
lbl1_2 = tk.Label(window)
lbl1_2.place(x=325, y=500)

lbl2_1 = tk.Label(window)
lbl2_1.place(x=325, y=530)
lbl2_2 = tk.Label(window)
lbl2_2.place(x=325, y=530)

lbl3_1 = tk.Label(window)
lbl3_1.place(x=325, y=560)
lbl3_2 = tk.Label(window)
lbl3_2.place(x=325, y=560)

lbl4_1 = tk.Label(window)
lbl4_1.place(x=325, y=590)
lbl4_2 = tk.Label(window)
lbl4_2.place(x=325, y=590)

# кнопоки сохранить

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

# выбор для пользователя

selected = IntVar()
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)

rad1.place(x=220, y=80)
rad2.place(x=320, y=80)
rad3.place(x=420, y=80)

rad4 = Radiobutton(window, text='Первый', value=4, variable=selected)
rad5 = Radiobutton(window, text='Второй', value=5, variable=selected)
rad6 = Radiobutton(window, text='Третий', value=6, variable=selected)

rad4.place(x=220, y=180)
rad5.place(x=320, y=180)
rad6.place(x=420, y=180)

rad7 = Radiobutton(window, text='Первый', value=7, variable=selected)
rad8 = Radiobutton(window, text='Второй', value=8, variable=selected)
rad9 = Radiobutton(window, text='Третий', value=9, variable=selected)

rad7.place(x=220, y=300)
rad8.place(x=320, y=300)
rad9.place(x=420, y=300)

rad10 = Radiobutton(window, text='Первый', value=10, variable=selected)
rad11 = Radiobutton(window, text='Второй', value=11, variable=selected)
rad12 = Radiobutton(window, text='Третий', value=12, variable=selected)

rad10.place(x=220, y=420)
rad11.place(x=320, y=420)
rad12.place(x=420, y=420)

window.mainloop()

while True:
    keyboard.wait()
