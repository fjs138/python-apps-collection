from tkinter import *
import pygame.mixer
from time import sleep

app = Tk()
app.title("Head First Mix")
## app.geometry('250x100+200+100')

mixer = pygame.mixer
mixer.init()

def track_start():
    track.play(loops = -1)

def track_stop():
    track.stop()

def shutdown():
    track = mixer.Sound(sound_file)
    track.stop()
    ## destroys app window
    app.destroy()
    ## exits python app
    ## sys.exit()

def create_gui(app, mixer, sound_file):
    def track_toggle():
        if track_playing.get()==1:
            track.play(loops = -1)
        else:
            track.stop()

    def change_volume(v):
        track.set_volume(volume.get())

    track = mixer.Sound(sound_file)
    track_playing = IntVar()
    track_button = Checkbutton(app, variable = track_playing,\
                               command = track_toggle, text = sound_file)
    track_button.pack(side = LEFT)
    volume = DoubleVar()
    volume.set(track.get_volume())
    volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0,\
                        resolution = 0.1, command = change_volume,\
                         label ="Volume", orient = HORIZONTAL)
    volume_scale.pack(side = RIGHT)




sound_file = "50459_M_RED_Nephlimizer.wav"


create_gui(app,mixer,"50459_M_RED_Nephlimizer.wav")
create_gui(app,mixer,"49119_M_RED_HardBouncer.wav")



'''
track = mixer.Sound("50459_M_RED_Nephlimizer.wav")
print ("Play it LOUD, man!")
track.set_volume(0.9)
sleep(2)
print("Softly does it...")
track.set_volume(0.1)
sleep(2)
track.stop()
'''














'''
start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)
'''
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()