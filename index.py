from tkinter import *
import os
os.system('clear')

root = Tk()
root.title('UE App')
root.geometry('1000x600')
root.configure(background='#272d36')

header = Frame(root, height=80, background='#212730')
header.pack(side=TOP, fill=X)
header.pack_propagate(0)

logo = Label(header, padx=10, text='UE', font=('Helvetica Neue', 40, 'bold'), fg='white', bg='#212730')
logo.pack(side=LEFT)

menu = Frame(header, height=80, width=500, background='#212730')
menu.pack(side=LEFT)
menu.pack_propagate(0)

home = Label(menu, text='HOME', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
home.pack(side=LEFT, fill=Y)

home.bind('<Enter>', lambda event, h=home: h.configure(bg='#272d36'))
home.bind('<Leave>', lambda event, h=home: h.configure(bg='#212730'))

roster = Label(menu, text='ROSTER', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
roster.pack(side=LEFT, fill=Y)

roster.bind('<Enter>', lambda event, r=roster: r.configure(bg='#272d36'))
roster.bind('<Leave>', lambda event, r=roster: r.configure(bg='#212730'))

applications = Label(menu, text='APPLICATIONS', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
applications.pack(side=LEFT, fill=Y)

applications.bind('<Enter>', lambda event, label=applications: label.configure(bg='#272d36'))
applications.bind('<Leave>', lambda event, label=applications: label.configure(bg='#212730'))

user = Frame(header, height=80, width=200, background='#212730')
user.pack(side=RIGHT)
user.pack_propagate(0)

register = Label(user, text='REGISTER', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
register.pack(side=RIGHT, fill=Y)

register.bind('<Enter>', lambda event, label=register: label.configure(bg='#272d36'))
register.bind('<Leave>', lambda event, label=register: label.configure(bg='#212730'))

login = Label(user, text='LOGIN', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
login.pack(side=RIGHT, fill=Y)

login.bind('<Enter>', lambda event, label=login: label.configure(bg='#272d36'))
login.bind('<Leave>', lambda event, label=login: label.configure(bg='#212730'))




root.mainloop()