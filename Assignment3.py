# Program Name: Assignment3.py 
# Course: IT3883/Section W02
# Student Name: Caitlin Johnson
# Assignment Number: Assignment3
# Due Date: 02/23/ 2025
# Purpose: This program uses a GUI application that takes in value and converts Miles per Gallon into Kilometers per Liter with any final total button
# Youtube.com/brocode, Youtube.com/codemy.com

from tkinter import *

MPG_TO_KML = 0.425143707 #conversion

def convert_mpg_to_kml():
    try:
        
        mpg = float(entry_mpg.get())
        kml = mpg * MPG_TO_KML
        result.config(text=f"{kml:.4f} km/l")
    except ValueError:
        result.config(text="Invalid input")

window = Tk()
window.title("Convert MPG to KML")

#label_1
label = Label(window, text="Enter Miles per Gallon (MPG):")
label.pack()

#user_input
entry_mpg = Entry(window)
entry_mpg.pack()

#label_2
result = Label(window, text="Result: ")
result.pack()


entry_mpg.bind("<KeyRelease>", lambda event: convert_mpg_to_kml())

#window pop-up
window.mainloop()