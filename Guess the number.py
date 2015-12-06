# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# initialize global variables used in your code
number_to_guess = 0
count = 0

# define helper function to initial game
def init():
    range100()
    
# define event handlers for control panel    
def range100():
    # button that changes range to range [0,100) and restarts
    global number_to_guess
    global count
    count = 7
    number_to_guess = random.randrange(0, 99)
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is: ", count
    print
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global number_to_guess
    global count
    count = 10
    number_to_guess = random.randrange(0, 999)
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is: ", count
    print
    
def get_input(guess):
    global number_to_guess
    global count
    guess = int(guess)
    print "Guess was ", guess
    count = count - 1
    print "Number of remaining guesses is: ", count
    # main game logic goes here	
    if(count > 0):
        if(guess == number_to_guess):
            print "Correct!"
        elif(guess > number_to_guess):
            print "Lower!"
        else:
            print "Higher!"
        print
    else:
        print
        init()

    
# create frame
frame = simplegui.create_frame("Guess the number game!!!", 200, 200)

# register event handlers for control elements
frame.add_button("Range is from [0, 100)", range100, 200)
frame.add_button("Range is from [0, 1000)", range1000, 200)
frame.add_button("Restar the game, range is from [0, 100)", init, 200)
frame.add_input("Enter a guess", get_input, 200)

init()

# start frame
frame.start()

