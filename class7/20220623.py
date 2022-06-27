from tkinter import *


def hi_fun():
    print("Hello Singular")
    display.config(text="Hi Singular", fg="red", bg="white")


def hi_happy():
    display.config(text="", fg="red", bg="white")


win = Tk()

win.title("My first GUI")

btn = Button(win, text="Click Me", command=hi_fun)
btn.pack()

display = Label(win, text="hello", fg="pink", bg="black")
display.pack()
but = Button(win, text="Click", command=hi_happy)

but.pack()

win.mainloop()