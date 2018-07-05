#Building a basic GUI using tkinter

import tkinter
import os

Main = tkinter.Tk()
#Main Window
Main.title("Grid Demonstration")
Main.geometry("480x480") #Dimensions of Main Window
Main["padx"] = 8

label = tkinter.Label(Main, text="Tkinter Grid Demo")
label.grid(row=0, column=0, sticky="news", columnspan=5)

#Row and Column configurations
Main.columnconfigure(0, weight=100)
Main.columnconfigure(1, weight=1)
Main.columnconfigure(2, weight=1000)
Main.columnconfigure(3, weight=600)
Main.columnconfigure(4, weight=1000)
Main.rowconfigure(0, weight=1)
Main.rowconfigure(1, weight=10)
Main.rowconfigure(2, weight=1)
Main.rowconfigure(3, weight=3)
Main.rowconfigure(4, weight=3)

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
FrameTitle.grid(row=1, column=4, sticky="nw")

RadioButtonValue = tkinter.IntVar()
RadioButtonValue.set(1)

#Radio Buttons
rb1 = tkinter.Radiobutton(FrameTitle, text="Filename", value=1, variable=RadioButtonValue)
rb2 = tkinter.Radiobutton(FrameTitle, text="Path", value=2, variable=RadioButtonValue)
rb3 = tkinter.Radiobutton(FrameTitle, text="Timestamp", value=3, variable=RadioButtonValue)
rb1.grid(row=0, column=0, sticky="w")
rb2.grid(row=1, column=0, sticky="w")
rb3.grid(row=2, column=0, sticky="w")

#To display Result
ResultLabel = tkinter.Label(Main, text="Result")
ResultLabel.grid(row=1, column=3, sticky="sw")
Result = tkinter.Entry(Main)
Result.grid(row=2, column=3, sticky="nw")

#Frame for Time spinners
timeFrame = tkinter.LabelFrame(Main, text="Time")
timeFrame.grid(row=3, column=0, sticky="new")

#Time Spinners
HourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
MinuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
SecondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
HourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=": ").grid(row=0, column=1)
MinuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
SecondSpinner.grid(row=0, column=4)
timeFrame["padx"] = 36

#Frame for Date Spinners
DateFrame = tkinter.Frame(Main)
DateFrame.grid(row=4, column=0, sticky="new")

#Date Labels
DayLabel = tkinter.Label(DateFrame, text="Day")
MonthLabel = tkinter.Label(DateFrame, text="Month")
Yearlabel = tkinter.Label(DateFrame, text="Year")
DayLabel.grid(row=0, column=0, sticky="n")
MonthLabel.grid(row=0, column=1, sticky="n")
Yearlabel.grid(row=0, column=2, sticky="n")

#Date Spinners
DaySpin = tkinter.Spinbox(DateFrame, width=5, from_=1, to=31)
MonthSpin = tkinter.Spinbox(DateFrame, width=5, values=("Jan", "Feb", "March", "April",
                                                        "May", "June", "July", "August",
                                                        "Sept", "Oct", "Nov", "Dec"))
YearSpin = tkinter.Spinbox(DateFrame, width=5, from_=1990, to=2020)
DaySpin.grid(row=1, column=0)
MonthSpin.grid(row=1, column=1)
YearSpin.grid(row=1, column=2)

#OK and Cancel Buttons
OKButton = tkinter.Button(Main, text="OK")
CancelButton = tkinter.Button(Main, text="Cancel", command=Main.destroy)
OKButton.grid(row=4, column=3, sticky="ne")
CancelButton.grid(row=4, column=4, sticky="nw")

Main.mainloop()
