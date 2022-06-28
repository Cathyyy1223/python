from tkinter import *


def show_juice():
    global juice
    display.config(text=juice)


def add_juice():
    global juice
    for i in juice:
        if i == entry.get():
            display.config(text="此果汁已在清單中")

    else:
        juice.append(entry.get())


def rem_juice():
    global juice
    display.config(text="此果汁不在清單中")


# def hi_fun():
#     print("Hello Singular")
#     display.config(text="Hi Singular", fg="red", bg="white")

# def hi_happy():
#     display.config(text=entry.get(), fg="red", bg="white")

juice = []
win = Tk()
win.title("My first GUI")

btn = Button(win, text="add", command=add_juice)
btn.grid(row=0, column=0)
bbtn = Button(win, text="show", command=show_juice)
bbtn.grid(row=1, column=0)
bbbtn = Button(win, text="remove", command=rem_juice)
bbbtn.grid(row=2, column=0)

display = Label(win, text="", fg="pink", bg="black")
display.grid(row=3, column=0)

entry = Entry(win)
entry.grid()

win.mainloop()
