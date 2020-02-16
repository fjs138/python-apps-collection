# Importing required libraries.
from tkinter import *
import pygame.mixer

# Create the two even handlers that set the IntVar and play the appropriate sound.
def play_correct_sound():
    num_good.set(num_good.get()+1)
    correct_s.play()

def play_wrong_sound():
    num_bad.set(num_bad.get()+1)
    wrong_s.play()

# Create the GUI application window.
app = Tk()
app.title("TVN Game Show GUI")
app.geometry('300x110+200+100')

# Initialize the sound system
sounds = pygame.mixer
sounds.init()

# Load in the required sound effects
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

# Create two IntVars: one to count the number of correct answers and another
# to count the number of wrong answers.
num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)

# Display a friendly message that tells the host what to do.
lab = Label(app, text = 'When you are ready, click on the buttons!', height = 3)
# Be sure to PACK your widgets.
lab.pack()

# Create two labels to hold each counter and connect the labels
#  to the relevant IntVars

lab1 = Label(app,textvariable = num_good)
lab1.pack(side = 'left')
lab2 = Label(app, textvariable = num_bad)
lab2.pack(side = 'right')

# Create each of the buttons and connect them to their relevant event handler.
b1 = Button(app, text = "Correct!", width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)
b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

# Start tkinter’s main event loop.
app.mainloop()