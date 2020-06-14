from tkinter import *
import os
os.system('clear')

root = Tk()
root.title('UE App')
root.geometry('1000x600')
root.configure(background='#272d36')

article = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec risus tortor, mattis ut fermentum vel, accumsan at nunc. Nulla eu dictum risus. Mauris pulvinar fermentum facilisis. Quisque pharetra purus sed sem tincidunt, in lacinia diam placerat. Aenean ut justo auctor, suscipit lorem nec, porttitor enim. Integer venenatis risus venenatis dui eleifend auctor. Nunc eu lacinia quam. Donec quis laoreet risus, vitae gravida eros. Curabitur condimentum quam et risus egestas dictum. Aenean leo neque, finibus non mi et, commodo pharetra lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam et feugiat elit. Ut et porta elit. Integer volutpat sapien mi, ac euismod felis aliquam in. Nullam ut porta leo. Etiam ac tellus id purus lobortis euismod. Aenean quis ipsum nunc. Etiam ac nisl purus. Ut facilisis euismod mauris, sed elementum dolor laoreet pharetra. Pellentesque vel accumsan est, sit amet imperdiet mi. Mauris volutpat condimentum est, id interdum justo egestas eget. Vivamus suscipit nibh erat, non lobortis lacus tincidunt eu. Nulla interdum purus in condimentum pulvinar. Vivamus nunc elit, vehicula nec mauris et, condimentum condimentum arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat eu justo porttitor feugiat. Nullam facilisis felis et magna fermentum, a egestas sapien eleifend. Nulla rhoncus mauris ut justo porta accumsan. In vel elit sit amet ipsum blandit fermentum eleifend blandit mi.'

header = Frame(root, height=80, background='#212730')
header.pack(side=TOP, fill=X)
header.pack_propagate(0)

split = Frame(root, background='#1a1f26')
split.pack(fill=X)

content = Frame(root, background='#272d36', relief=FLAT, borderwidth=20)
content.pack(expand=1, fill=BOTH)

spacing = Frame(content, height=0, background='#272d36')
spacing.pack(fill=X)

sectionLeft = Frame(content, width=200, background='#272d36')
sectionLeft.pack(side=LEFT, fill=BOTH)
sectionLeft.pack_propagate(0)

section = Frame(content, width=2, background='#1a1f26')
section.pack(side=LEFT, fill=Y)

newsItem = Label(sectionLeft, height=2, padx=10, text='PTR TESTING', background='#272d36', fg='white', cursor='hand', anchor=W)
newsItem.pack(side=TOP, fill=X)

newsItemB = Label(sectionLeft, height=2, padx=10, text='ITEM TWO', background='#272d36', fg='white', cursor='hand', anchor=W)
newsItemB.pack(side=TOP, fill=X)

newsItem.bind('<Enter>', lambda event, label=newsItem: label.configure(bg='#212730', fg='yellow'))
newsItem.bind('<Leave>', lambda event, label=newsItem: label.configure(bg='#272d36', fg='white'))

newsItemB.bind('<Enter>', lambda event, label=newsItemB: label.configure(bg='#212730', fg='yellow'))
newsItemB.bind('<Leave>', lambda event, label=newsItemB: label.configure(bg='#272d36', fg='white'))

sectionRight = Frame(content, background='#272d36')
sectionRight.pack(side=RIGHT, expand=1, fill=BOTH)

# newsSplit = Frame(sectionRight, height=1, background='#1a1f26')
# newsSplit.pack(side=TOP, fill=X)

newsContent = Frame(sectionRight, borderwidth=20, background='#212730')
newsContent.pack(expand=1, fill=BOTH)

newsTitle = Label(newsContent, text='PTR Testing', anchor=W, font=('Helvetica Neue', 24), bg='#212730', fg='white')
newsTitle.pack(fill=X)

newsMeta = Frame(newsContent, bg='#212730')
newsMeta.pack(fill=X)

newsAuthor = Label(newsMeta, text='Muushi', anchor=W, font=('Helvetica Neue', 11), bg='#212730', fg='orange')
newsAuthor.pack(side=LEFT, fill=X)

newsDate = Label(newsMeta, text='12 Jun 2020', anchor=E, font=('Helvetica Neue', 11), bg='#212730', fg='grey')
newsDate.pack(side=RIGHT, fill=X)

newsSpacing = Frame(newsContent, height=10, bg='#212730')
newsSpacing.pack(fill=X)

newsSplit = Frame(newsContent, height=1, bg='yellow')
newsSplit.pack(fill=X)

newsSpacing = Frame(newsContent, height=10, bg='#212730')
newsSpacing.pack(fill=X)

newsArticle = Text(newsContent, background='#212730', wrap='word', font=('Helvetica Neue', 14), fg='white', borderwidth=0, highlightthickness=0)
newsArticle.insert('1.0', article)
newsArticle.pack(expand=1, fill=BOTH)

logo = Label(header, padx=10, text='UE', font=('Helvetica Neue', 40, 'bold'), fg='white', bg='#212730')
logo.pack(side=LEFT)

menu = Frame(header, height=80, width=500, background='#212730')
menu.pack(side=LEFT)
menu.pack_propagate(0)

home = Label(menu, text='HOME', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
home.pack(side=LEFT, fill=Y)

home.bind('<Enter>', lambda event, label=home: label.configure(bg='#272d36', fg='yellow'))
home.bind('<Leave>', lambda event, label=home: label.configure(bg='#212730', fg='white'))

roster = Label(menu, text='ROSTER', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
roster.pack(side=LEFT, fill=Y)

roster.bind('<Enter>', lambda event, label=roster: label.configure(bg='#272d36', fg='yellow'))
roster.bind('<Leave>', lambda event, label=roster: label.configure(bg='#212730', fg='white'))

applications = Label(menu, text='APPLICATIONS', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
applications.pack(side=LEFT, fill=Y)

applications.bind('<Enter>', lambda event, label=applications: label.configure(bg='#272d36', fg='yellow'))
applications.bind('<Leave>', lambda event, label=applications: label.configure(bg='#212730', fg='white'))

user = Frame(header, height=80, width=200, background='#212730')
user.pack(side=RIGHT)
user.pack_propagate(0)

register = Label(user, text='REGISTER', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
register.pack(side=RIGHT, fill=Y)

register.bind('<Enter>', lambda event, label=register: label.configure(bg='#272d36', fg='yellow'))
register.bind('<Leave>', lambda event, label=register: label.configure(bg='#212730', fg='white'))

login = Label(user, text='LOGIN', padx=10, background='#212730', font='bold', fg='white', cursor='hand')
login.pack(side=RIGHT, fill=Y)

login.bind('<Enter>', lambda event, label=login: label.configure(bg='#272d36', fg='yellow'))
login.bind('<Leave>', lambda event, label=login: label.configure(bg='#212730', fg='white'))




root.mainloop()