from tkinter import *
import os
os.system('clear')

root = Tk()
root.title('Index')
root.geometry('1000x600')

def hello():
    hello_label = Label(root, text='Hello ' + myTextbox.get())
    hello_label.pack()

myLabel = Label(root, text='Enter your first name:')
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text='Submit', command=hello)
myButton.pack()

root.mainloop()