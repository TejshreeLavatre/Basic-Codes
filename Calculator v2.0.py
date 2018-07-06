#Better version of a Calculator

import tkinter

padding = 8
program = tkinter.Tk()
program.title("Calculator v2.0")
program.geometry("400x400")
program["padx"] = padding

keys = [[("C", 1), ("CE", 1)],
        [("7", 1), ("8", 1), ("9", 1), ("+", 1)],
        [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
        [("1", 1), ("2", 1), ("3", 1), ("*", 1)],
        [("0", 1), ("=", 2), ("/", 1)]
        ]

result = tkinter.Entry(program)
result.grid(row=0, column=0, sticky="news")

keysgrid = tkinter.Frame(program)
keysgrid.grid(row=1, column=0, sticky="news")

row = 0
for entry in keys:
    col = 0
    for key in entry:
        tkinter.Button(keysgrid, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

program.update()
program.minsize(keysgrid.winfo_width() + padding, result.winfo_height() + keysgrid.winfo_height())
program.maxsize(keysgrid.winfo_width() + padding, result.winfo_height() + keysgrid.winfo_height())
program.mainloop()
