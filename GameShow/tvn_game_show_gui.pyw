from tkinter import *

import pygame.mixer

# Waits for sound channel to be clear before triggering next sound
def wait_finish(channel):
    while channel.get_busy():
        pass

# Initialize pygame mixer as sounds
sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

#number_correct = IntVar()
number_correct = 0
#number_wrong = IntVar()
number_wrong = 0


# Create tkinter application called "app"
app = Tk()
# Give the app window a name
app.title("TVN Game Show GUI")
# Provide window coordinates and size values
app.geometry('400x210+300+100')
# Add label text to window
#label = Label(app, text="Welcome to the show!")
#label.pack(padx = 10, pady = 10)

# Application logic
def correct():
    print("Correct!")
    # the global keyword allows adjusting values associated with variables
    # outside of the function
    global number_correct
    #number_asked = number_asked + 1
    number_correct = number_correct + 1
    wait_finish(correct_s.play())

def wrong():
    print("Wrong")
    global number_wrong
    #number_asked = number_asked + 1
    number_wrong = number_wrong + 1
    wait_finish(wrong_s.play())

def summary():
    global number_wrong
    global number_correct
    print(str(number_correct) + " were correctly answered.")
    print(str(number_wrong) + " were incorrectly answered.")

def exitapp():
    summary()
    sys.exit()

lab = Label(app, text='When you are ready, click on the buttons!', height = 3)
lab.pack()#fill=BOTH, expand=False)

lab1 = Label(app, textvariable =  number_correct)
lab1.pack(side = 'left')

lab2 = Label(app, textvariable = number_wrong)
lab2.pack(side = 'right')

# Add a button to the window with text and a width value.
b1 = Button(app, text = "Correct!", width = 10, command = correct)
# Actually link the button to the existing window
# Side values: left, right, top, bottom
# b1.pack(side = 'left')
b1.pack(side = "left",  padx = 10, pady = 10)#, ipadx = 10, ipady = 10, fill=BOTH, expand=False)

b2 = Button(app, text = "Wrong!", width = 10, command = wrong)
b2.pack(side = "right", padx = 10, pady = 10)#, ipadx = 10, ipady = 10, fill=BOTH, expand=False)

b3 = Button(app, text = "Quit", width = 10, command = exitapp)
b3.pack(side = "bottom", padx = 10, pady = 10)#, ipadx = 10, ipady = 10, fill=BOTH, expand=False)

# Start the tkinter event loop
app.mainloop()