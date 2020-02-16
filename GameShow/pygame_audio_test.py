__author__ = 'Frank'

# Just like with other libraries, you import the library you want to use
import pygame.mixer

# Create a "pygame.mixer" object and initialize the sound system.
sounds = pygame.mixer
sounds.init()

# The "wait_finish()" function loops until the channel's "get_busy()"
# method returns False.
def wait_finish(channel):
    # The "get_busy()" method checks to see if the sound is still playing.
    while channel.get_busy():
        # "pass" is a Python construct that does nothing.
        pass


# Load in the sound file you want to play.
s = sounds.Sound("heartbeat.wav")
# The value returned from the "play()" method gets passed to "wait_finish()".
# If I don’t use wait_finish(), then the sounds play "at once"
wait_finish(s.play())
# Identify and play each of the sounds.
s2 = sounds.Sound("buzz.wav")
wait_finish(s2.play())
# Identify and play each of the sounds.
s3 = sounds.Sound("ohno.wav")
wait_finish(s3.play())
# Identify and play each of the sounds.
s4 = sounds.Sound("carhorn.wav")
wait_finish(s4.play())