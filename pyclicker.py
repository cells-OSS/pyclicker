from pynput import keyboard
from pynput import mouse
from tkinter import *
import time
import threading

mouse_controller = mouse.Controller()

clicking = False
delay = 1
listener = None

def click_loop():
    while clicking:
        mouse_controller.click(mouse.Button.left)
        time.sleep(delay)

def on_press(key):
    global clicking
    try:
        if key == keyboard.Key.insert:
            clicking = not clicking
            if clicking:
                print("Clicking started")
                threading.Thread(target=click_loop, daemon=True).start()
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

window = Tk()

window.title("Pyclicker")
window.geometry("300x200")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(bg="#525252")

labelSlogan = Label(window,text="The only clicker software you'll need.", background="#525252", fg="white")
labelSlogan.pack()
labelSlogan.place(x = 30, y = 30)

secondsEntry = Entry(bg = "#726248", fg = "white")
secondsEntry.pack
secondsEntry.place(x = 70, y = 80)

startButton = Button(window, text='Start', bg="#525252", fg="white", activebackground='#726248', activeforeground='white', command = start)
startButton.pack()
startButton.place(x=93, y =110)

stopButton = Button(window, text='Stop', bg="#525252", fg="white", activebackground='#726248', activeforeground='white', command = stop)
stopButton.pack()
stopButton.place(x = 157, y =110)


window.mainloop()


