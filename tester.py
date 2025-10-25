from tkinter import *

window = Tk()

window.title("Pyclicker")
window.geometry("400x450")
icon = PhotoImage(file='Untitled.png')
window.iconphoto(True,icon)

window.config(background="#525252")
labelSlogan = Label(window,text="The only clicker software you'll need.",background="#525252",fg="white",)
labelSlogan.pack()
labelSlogan.place(x=80,y=30)
button = Button(window,text='Start')
button.pack()

window.mainloop()

