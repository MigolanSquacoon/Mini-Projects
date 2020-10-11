# counts clicks on the screen
from pynput import mouse
from pynput.keyboard import Listener, KeyCode
import threading

n = []  # the list
start_stop_key = KeyCode(char="*")
exit_key = KeyCode(char="-")

print("Hello!")
print("This is a click counter. It counts how many times you click.")
print("Start / Pause:", "*")
print("Exit:", "-")


class counter(threading.Thread):
    def __init__(self):
        super(counter, self).__init__()
        self.running = False
        self.program_running = True

    def start_counting(self):
        self.running = True

    def stop_counting(self):
        self.running = False

    def exit(self):
        self.stop_counting()
        self.program_running = False


count = counter()
count.start()


def on_click(x, y, button, pressed):
    if pressed:
        n.append(1)  # adds +1 click to the list


def on_press(key):
    if key == start_stop_key:
        if count.running:
            count.stop_counting()  # stop running
            clicks = sum(n)  # adds the clicks together
            print(clicks)  # prints the total number of clicks
            print("Stopped")
        else:
            count.start_counting()  # start it
            print("Started")
    elif key == exit_key:  # exits the program
        count.exit()
        ml.stop()
        kl.stop()
        print("Exited")


with mouse.Listener(on_click=on_click) as ml:
    with Listener(on_press=on_press) as kl:
        ml.join()
        kl.join()