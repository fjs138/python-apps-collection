__author__ = 'Frank Santaguida'
'''
Pseudocode:

Display question for host.
Allow host to respond with 1 or 2 for correct or incorrect.
Based on 1 or 2, play sound effect 1 or 2.
Meanwhile, program keeps running count of how many answers were correct or
incorrect.
Meanwhile, program closes when host responds with 0 at any time.
'''
'''
Pseudocode 2:

(You need to remember how
many questions were asked,
how many were correct,
and how many were wrong.)

number_asked = 0
number_correct = 0
number_wrong = 0

(Begin by asking the
host to make a choice.)

ask the host to press 1 for correct, 2 for incorrect, or 0 to end
while the host response is not 0
    This will run if the question
was answered CORRECTLY)
    if host response was 1
        add 1 to number_asked
        add 1 to number_correct
        play a sound effect
    (This will run if the question
    was answered INCORRECTLY)
    if host response was 2
        add 1 to number_asked
        add 1 to number_wrong
        play a sound effect
    (Ask the host at the end of each loop what
    he wants to do next)
    ask the host to press 1 for correct, 2 for incorrect, or 0 to end

(Finally, display the scores.)
display the value of number_asked, number_correct, number incorrect
ask the host to press 1 for correct, 2 for incorrect, or 0 to end
display the values of number_asked, number_correct and
number_wrong on screen
'''
# Import pygame's mixer module
import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

# Create a mixer object and initialize the pygame sound system
sounds = pygame.mixer
sounds.init()

correct_sound = sounds.Sound("correct.wav")
wrong_sound = sounds.Sound("wrong.wav")

# Prompt for "question master"
prompt = "Press 1 for correct, 2 for wrong, or 0 to quit."

# Number of questions answered in total
number_asked = 0
# Number of questions answered correctly
number_correct = 0
# Number of questions answered incorrectly
number_wrong = 0

# Prompt the host.
choice = input(prompt)
# While the game is not ended...
# event loop
while choice != "0":
    # If the answer is correct, increment counters and play sound
    if choice == "1":
        # X += 1 is the same as X = X + 1
        number_asked += 1
        number_correct += 1
        wait_finish(correct_sound.play())
    # If the answer is incorrect, increment counters and play sound
    if choice == "2":
        number_asked += 1
        number_wrong += 1
        wait_finish(wrong_sound.play())
    choice = input(prompt)

    print("You asked " + str(number_asked) + " questions.")
    print(str(number_correct) + " were correctly answered.")
    print(str(number_wrong) + " were incorrectly answered.")