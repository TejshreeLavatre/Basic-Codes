###Plotting a parabola using tkinter

try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

def parabola(x):
    y = x * x
    return y

MainWindow = tkinter.Tk()

MainWindow.title("Parabola function")
MainWindow.geometry("450x450")

canvas = tkinter.Canvas(MainWindow, width=500, height=500)
canvas.grid(row=0, column=0)


for x in range(-100, 100):
    z = parabola(x)
    print(z)

MainWindow.mainloop()
