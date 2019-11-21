import threading
from pynput.keyboard import Key, Controller

keyboard = Controller()


def lockTheScreen():
    print("Time ends screen is going to locked\n")
    keyboard.press(Key.ctrl)
    keyboard.press(Key.cmd)
    keyboard.press('q')


timer = threading.Timer(5, lockTheScreen)
timer.start()
print("Time Starts\n")
