
import tkinter

_main = tkinter.Tk()
_main.title("Calculator")
_main.geometry("600x400")
_main["padx"] = 6

_main.rowconfigure(0, weight=1)
_main.rowconfigure(1, weight=1)
_main.rowconfigure(2, weight=1)
_main.rowconfigure(3, weight=1)
_main.rowconfigure(4, weight=1)
_main.rowconfigure(5, weight=1)
_main.rowconfigure(6, weight=1)
_main.columnconfigure(0, weight=1)
_main.columnconfigure(1, weight=1)
_main.columnconfigure(2, weight=1)
_main.columnconfigure(3, weight=1)
_main.columnconfigure(4, weight=1)

result = tkinter.Entry(_main)
result.grid(row=0, column=0, sticky="news", columnspan=4)

ClearButton = tkinter.Button(_main, text="C")
CEButton = tkinter.Button(_main, text="CE")
ClearButton.grid(row=1, column=0, sticky="news")
CEButton.grid(row=1, column=1, sticky="news")
t = 0
for i in range(1, 4):
    button = tkinter.Button(_main, text=i)
    button.grid(row=4, column=t, sticky="news")
    t += 1
t = 0
for i in range(4, 7):
    buttons = tkinter.Button(_main, text=i)
    buttons.grid(row=3, column=t, sticky="news")
    t += 1
t = 0
for i in range(7, 10):
    button = tkinter.Button(_main, text=i)
    button.grid(row=2, column=t, sticky="news")
    t += 1

Zero = tkinter.Button(_main, text="0")
Zero.grid(row=5, column=0, sticky="news")

equal = tkinter.Button(_main, text="=")
equal.grid(row=5, column=1, sticky="news", columnspan=2)

division = tkinter.Button(_main, text="/")
division.grid(row=5, column=3, sticky="news")

multiply = tkinter.Button(_main, text="*")
multiply.grid(row=4, column=3, sticky="news")

minus = tkinter.Button(_main, text="-")
minus.grid(row=3, column=3, sticky="news")

addition = tkinter.Button(_main, text="+")
addition.grid(row=2, column=3, sticky="news")

_main.mainloop()
