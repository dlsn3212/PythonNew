from tkinter import *

root = Tk()
#Label(tk, text = 'Hello World').pack()
root.title('Event Test')
root.geometry('640x400+20+20')

def callback():
    exit(0)

button = Button(root,text='Quit',width=20, command = callback)

button.pack(padx = 10, pady = 10)
root.mainloop()
