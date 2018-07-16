# try:
import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(drawing):
    drawing.update()
    x_origin = drawing.winfo_width() / 2
    y_origin = drawing.winfo_height() / 2
    drawing.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    drawing.create_line(-x_origin, 0, x_origin, 0, fill="black")
    drawing.create_line(0, -y_origin, 0, y_origin, fill="black")


def plot(plotting, x, y):
    plotting.create_line(x, y, x + 1, y + 1, fill="blue")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola function")
mainWindow.geometry("350x350")

canvas = tkinter.Canvas(mainWindow, width=350, height=350)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for w in range(-100, 100):
    z = parabola(w)
    plot(canvas, w, -z)

mainWindow.mainloop()
