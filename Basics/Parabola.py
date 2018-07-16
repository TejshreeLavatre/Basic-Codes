try:
    import tkinter
except ImportError: #Python 2
    import Tkinter as tkinter


def parabola(x):
    y = x * x
    return y


mainWindow = tkinter.Tk()
mainWindow.title("Parabola function")
mainWindow.geometry("350x350")

canvas = tkinter.Canvas(mainWindow, width=350, height=350)
canvas.grid(row=0, column=0)

for w in range(-100, 100):
    z = parabola(w)
    print(z)

mainWindow.mainloop()