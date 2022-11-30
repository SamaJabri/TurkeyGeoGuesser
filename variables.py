import turtle


# Maps
unnamedMapPath = './images/unnamed.gif'
namedMapPath = './images/named.gif'

# Turtle configs
turtle.tracer(0, 0)
turtle.hideturtle()

gameWindow = turtle.Screen()
name = turtle.Turtle()
correct = turtle.Turtle()

# User status
correctGuesses = 0
guessed = []
province = turtle.Turtle()

# Buttons
playButton = turtle.Turtle()
cheatSheetButton = turtle.Turtle()
closeCheatSheetButton = turtle.Turtle()