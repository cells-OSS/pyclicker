from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import time
import threading
import os
import urllib.request
import subprocess
import sys

ICON_URL = "https://raw.githubusercontent.com/cells-OSS/pyclicker/main/icon.png"
if os.name == 'nt':
    icon_dir = os.path.join(os.getenv('APPDATA'), "pyclicker")
else:
    icon_dir = os.path.join(os.path.expanduser("~/.config/pyclicker"))
icon_path = os.path.join(icon_dir, "icon.png")

def ensure_icon_exists():
    if not os.path.exists(icon_dir):
        os.makedirs(icon_dir)
    if not os.path.exists(icon_path):
        try:
            urllib.request.urlretrieve(ICON_URL, icon_path)
        except Exception as e:
            print(f"Failed to download icon: {e}")


def install_packages(package):
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--break-system-packages"])

required_packages = ["pynput", "pyqt6"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing required package(s) {package}...")
        install_packages(package)

from pynput import keyboard
from pynput import mouse

os.system('cls' if os.name == 'nt' else 'clear')

mouse_controller = mouse.Controller()

clicking = False
delay = 1
listener = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui", self)

        #Connect the widgets.
        self.start.clicked.connect(self.start)
        self.stop.clicked.connect(self.when_stop_clicked)
        self.lineEdit.setText("1")



app = QApplication([])
window = MainWindow()
window.show()
app.exec()

def click_left():
    while clicking:
        mouse_controller.click(mouse.Button.left)
        time.sleep(delay)

def click_right():
    while clicking:
        mouse_controller.click(mouse.Button.right)
        time.sleep(delay)

def on_press_left(key):
    global clicking
    try:
        if key == keyboard.Key.insert:
            clicking = not clicking
            if clicking:
                print("Clicking started")
                threading.Thread(target=click_left, daemon=True).start()
            else:
                print("Clicking stopped")
    except AttributeError:
        pass

def on_press_right(key):
    global clicking
    try:
        if key == keyboard.Key.insert:
            clicking = not clicking
            if clicking:
                print("Clicking started")
                threading.Thread(target=click_right, daemon=True).start()
            else:
                print("Clicking stopped")
    except AttributeError:
        pass

def start():
    global delay, listener
    value = secondsEntry.get().strip()
    if value:
        try:
            delay = float(value)
        except ValueError:
            print(f"Invalid number. Using the default delay, {delay}")

    if listener is None:
        if mode == 1:
            on_press = on_press_left
        if mode == 2:
            on_press = on_press_right
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        print("Listener started")

def stop():
    global listener, clicking
    clicking = False
    if listener is not None:
        listener.stop()
        listener = None
        print("Listener stopped")

def LMB():
    global mode
    mode = 1

def RMB():
    global mode
    mode = 2

mode = None



