# Importing required libraries.
from tkinter import *
import tkinter.messagebox
## import pygame.mixer

def read_depots(depots_file):
    depots=[]
    depots_f=open(depots_file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

# Creates the event handler that defines what happens when clicking 'Save'
def save():
    try:
        # Appending the text to the end of the file...
        depots_file = open("deliveries.txt", "a")
        ## Saving the data entered into fields...
        depots_file.write("Depot:\n")
        depots_file.write("%s\n" % depot.get())
        depots_file.write("Description:\n")
        depots_file.write("%s\n" % description.get())
        depots_file.write("Address:\n")
        depots_file.write("%s\n" % address.get("1.0", END))
        ## Clearing the data entered into fields...
        ## depot.set(None)
        description.delete(0, END)
        address.delete("1.0",END)
    except Exception as exceptionHandler1:
        tkinter.messagebox.showerror("Error!", "Can't write to the file %s" % exceptionHandler1)

def quit():
    sys.exit()


# Create the GUI application window.
app = Tk()
app.title("Head-Ex Deliveries")
app.geometry('500x750+500+500')

lab = Label(app, text = 'Depot:', pady = 10)
lab.pack()
depot = StringVar()
## Setting radiobuttons to be unselected; by default they are all selected
depot.set(None)

# replacing the following radio button code with a OptionMenu
# Radiobutton(app, text = "Cambridge, MA", variable = depot, value = "Cambridge, MA").pack(padx = 10, pady = 10, anchor = S)
# Radiobutton(app, text = "Cambridge, UK", variable = depot, value = "Cambridge, UK").pack(padx = 10, pady = 10, anchor = S)
# Radiobutton(app, text = "Seattle, WA", variable = depot, value = "Seattle, WA").pack(padx = 10, pady = 10, anchor = S)
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()


lab1 = Label(app,text = 'Description:')
lab1.pack()
description = Entry(app)
description.pack(padx = 10, pady = 10)
##lab1.pack(side = 'left')
lab2 = Label(app, text = 'Address:')
lab2.pack()
address = Text(app)
address.pack(padx = 10, pady = 10)
##lab2.pack(side = 'right')

# Create each of the buttons and connect them to their relevant event handler.
b1 = Button(app, text = "Save", width = 10, command = save)
b1.pack(padx = 10, pady = 10)
b2 = Button(app, text = "Quit", width = 10, command = quit)
b2.pack(padx = 10, pady = 10)



# Start tkinter’s main event loop.
app.mainloop()



## insert text in an Entry field
## my_entry_field.insert(0, "banana ")
## index position 0,1,2,3, etc get overwritten when doing this

## delete all text in an Entry field
## my_entry_field.delete(0, END)

## insert text in a Text field
## my_large_field.get("1.0", END)
## 1 is the row 0 is the column
## Note: unlike Entry, you cannot just use get(), must specify start and end points

## this will clear the field
## my_large_field.delete("1.0", END)

## this will insert the text at the start of the field
## my_large_field.insert("1.0", "Some text")
