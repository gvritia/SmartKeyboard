import keyboard
# while True:
#     keyboard.wait("ctrl")
#     keyboard.press("ctrl + a")
# print(f"Введите комбинацию - ")
# key = keyboard.read_hotkey(suppress=False)
# print(key)
# keyboard.press(key)
# keyboard.wait()

print(f"Введите комбинацию - ")
key = keyboard.read_hotkey(suppress=False)
print(key)
keyboard.add_hotkey("ctrl +", lambda: keyboard.press(f"{key}"))
keyboard.wait()