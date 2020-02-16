from tkinter import *
# Create tkinter application called "app"
app = Tk()
# Give the app window a name
app.title("Your tkinter application")
# Provide window coordinates and size values
app.geometry('450x100+200+100')
# Add a button to the window with text and a width value.
b1 = Button(app, text = "Click me!", width = 10)
# Actually link the button to the existing window
# Side values: left, right, top, bottom
# b1.pack(side = 'left')
b1.pack()
b2 = Button(app, text = "Right", width = 10)
b2.pack(side = "right")
# Start the tkinter event loop
app.mainloop()