from tkinter import *

window = Tk()

window.title("Pyclicker")
window.geometry("400x450")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(bg="#525252")

labelSlogan = Label(window,text="The only clicker software you'll need.", background="#525252", fg="white")
labelSlogan.pack()
labelSlogan.place(x = 80, y = 30)

startButton = Button(window, text='Start', bg="#525252", fg="white", activebackground='#726248', activeforeground='white')
startButton.pack()
startButton.place(x=143, y =110)

stopButton = Button(window, text='Stop', bg="#525252", fg="white", activebackground='#726248', activeforeground='white')
stopButton.pack()
stopButton.place(x = 207, y =110)

secondsEntry = Entry(bg = "#726248", fg = "white")
secondsEntry.pack
secondsEntry.place(x = 120, y = 80)

window.mainloop()

