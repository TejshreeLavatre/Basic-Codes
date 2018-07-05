#Building a basic GUI using tkinter

import tkinter
import os

Main = tkinter.Tk()
#Main Window
Main.title("Grid Demonstration")
Main.geometry("480x480") #Dimensions of Main Window

label = tkinter.Label(Main, text="Tkinter Grid Demo")
label.grid(row=0, column=0, sticky="news", columnspan=5)

#Row and Column configurations
Main.columnconfigure(0, weight=100)
Main.columnconfigure(1, weight=10)
Main.columnconfigure(2, weight=1)
Main.columnconfigure(3, weight=100)
Main.columnconfigure(4, weight=100)
Main.rowconfigure(0, weight=1)
Main.rowconfigure(1, weight=1)
Main.rowconfigure(2, weight=100)
Main.rowconfigure(3, weight=10)
Main.rowconfigure(4, weight=100)

FileList = tkinter.Listbox(Main)
FileList.grid(row=1, column=0, sticky="news", rowspan=2)
FileList.config(border=3, relief="raised")
for item in os.listdir("C:/Windows/System32"):
    FileList.insert(tkinter.END, item) #Replace tkinter.END with 0 to reverse the order of the list

#Adding a scrollbar to the list
ListScrollBar = tkinter.Scrollbar(Main, orient=tkinter.VERTICAL, command=FileList.yview)
ListScrollBar.grid(row=1, column=1, sticky="news", rowspan=2)
FileList["yscrollcommand"] = ListScrollBar.set #Linking the ListScrollBar to the FileList

#Frame for radio buttons
#"LabelFrame" is used to enable us to enter a title in the Frame border itself
FrameTitle = tkinter.LabelFrame(Main, text="File Details")
FrameTitle.grid(row=2, column=3, sticky="ne")

RadioButtonValue = tkinter.IntVar()
RadioButtonValue.set(1)

#Radio Buttons
rb1 = tkinter.Radiobutton(FrameTitle, text="Filename", value=1, variable=RadioButtonValue)
rb2 = tkinter.Radiobutton(FrameTitle, text="Path", value=2, variable=RadioButtonValue)
rb3 = tkinter.Radiobutton(FrameTitle, text="Timestamp", value=3, variable=RadioButtonValue)
rb1.grid(row=0, column=0, sticky="w")
rb2.grid(row=1, column=0, sticky="w")
rb3.grid(row=2, column=0, sticky="w")

Main.mainloop()
