"""
___page : us page ke frame ka naam
___pg : us page ke function ka naam
"""

# majdooron ko bulawa
from tkinter import *

# khatarnak Setup
root = Tk()
root.geometry("1000x1000")
root.title("AD2")

# mere pyaare variables
font1 = "ComicSansMS 25"
font2 = "ComicSansMS 15"

# kaamkaji log


def homepg():
    print("This is home page.")


def cmndpg():
    print("This is commands page.")
    cmndpage.pack()

def newpg():
    newpage.pack()

def show():
    root.mainloop()


# yha Frames hain
sidebar = Frame(root, bg='white', width=200, relief=SOLID, borderwidth=1)
sidebar.pack(side=LEFT, fill=Y)
topbar = Frame(root, bg='white', height=100, relief=SOLID, borderwidth=1)
topbar.pack(side=TOP, fill=X)
newpage = Frame(root, bg='white', borderwidth=1, )
cmndpage = Frame(root, bg='white', borderwidth=1)


# yha Labels hain
Label(topbar, text='''Hello there! I am your personal voice assistant. You are viewing the GUI page.''', font=font1,
      bg="white", pady=20).pack(fill=Y)
Label(cmndpage, text='''These are the commands:''', font=font2, bg="white").pack()
Label(newpage, text="Hello new user!", font=font2, bg="white").pack()

# yha Buttons hain
Button(sidebar, text="Home", command=homepg, borderwidth=0.5, width=15, font=font2, pady=10, padx=10).pack(side=TOP)
Button(sidebar, text="Commands", command=cmndpg, borderwidth=0.5, width=15, font=font2, pady=10, padx=10).pack(side=TOP)

# root.mainloop()
