from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHigh.get())/100, 2))
    textBoxCalculate.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHigh.get())/100, 2))
    if (float(textBoxWeight.get()) / (float(textBoxHigh.get()) / 100) ** 2) >= 30.0:
        textBoxResult.configure(text="อ้วนมาก :(")
    elif (float(textBoxWeight.get()) / (float(textBoxHigh.get()) / 100) ** 2) >= 25.0:
        textBoxResult.configure(text="อ้วน :o")
    elif (float(textBoxWeight.get()) / (float(textBoxHigh.get()) / 100) ** 2) >= 23.0:
        textBoxResult.configure(text="น้ำหนักเกิน :|")
    elif (float(textBoxWeight.get()) / (float(textBoxHigh.get()) / 100) ** 2) >= 18.6:
        textBoxResult.configure(text="ปกติ :)")
    elif (float(textBoxWeight.get()) / (float(textBoxHigh.get()) / 100) ** 2) <= 18.5:
        textBoxResult.configure(text="ผอมเกินไป :(")

MainWindow = Tk()
labelHigh = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHigh.grid(row=0, column=0)
textBoxHigh = Entry(MainWindow)
textBoxHigh.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
CalculateButton = Button(MainWindow,width=10, height=3, text="BMI", fg="yellow", bg="Blue")
CalculateButton.bind('<Button-1>', leftClickButton)
CalculateButton.grid(row=3, column=0)
textBoxCalculate = Label(MainWindow, text="ผลลัพธ์")
textBoxCalculate.grid(row=2, column=1)
textBoxResult = Label(MainWindow, text="Fat Rate")
textBoxResult.grid(row=3, column=1)

MainWindow.mainloop()