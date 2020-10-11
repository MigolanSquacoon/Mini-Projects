import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random


delay = 0.008  # random.randint(6,11)
button = Button.left
start_stop_key = KeyCode(char="s")
exit_key = KeyCode(char="e")

print("hey! hey!")
print("start / pause: s ")
print("exit: e")


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click = ClickMouse(delay, button)
click.start()


def on_press(key):
    if key == start_stop_key:
        if click.running:
            click.stop_clicking()
            print("Paused")
        else:
            click.start_clicking()
            print("Started")
            # print(delay)
    elif key == exit_key:
        click.exit()
        listener.stop()
        print("Exited")


with Listener(on_press=on_press) as listener:
    listener.join()
