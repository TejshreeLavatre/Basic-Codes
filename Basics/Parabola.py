try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter


def parabola(drawing, size):
    for x in range(size):
        y = x * x / size
        plot(drawing, x, y)
        plot(drawing, -x, y)


def circle(drawing, radius, g, h, colour="red"):  #Defaults circle's colour to red unless specified otherwise
    drawing.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)


def draw_axes(drawing):
    drawing.update()
    x_origin = drawing.winfo_width() / 2
    y_origin = drawing.winfo_height() / 2
    drawing.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    drawing.create_line(-x_origin, 0, x_origin, 0, fill="black")
    drawing.create_line(0, -y_origin, 0, y_origin, fill="black")


def plot(plotting, x, y):
    plotting.create_line(x, -y, x + 1, -y + 1, fill="blue")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola function")
mainWindow.geometry("400x400")

canvas = tkinter.Canvas(mainWindow, width=400, height=400)
canvas.grid(row=0, column=0)

draw_axes(canvas)
parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 20, 0, 0, "yellow")
circle(canvas, 50, 50, 50, "green")
circle(canvas, 50, -50, 50, "black")
circle(canvas, 50, 50, -50, "purple")
circle(canvas, 50, -50, -50, "orange")
circle(canvas, 10, 20, 20)
circle(canvas, 10, -20, 20)
circle(canvas, 10, 20, -20)
circle(canvas, 10, -20, -20)

mainWindow.mainloop()
