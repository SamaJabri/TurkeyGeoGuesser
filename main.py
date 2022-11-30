import turtle
import functions
import variables


# Window configs
variables.gameWindow.bgcolor("light blue")
variables.gameWindow.title("Turkey Geo Guess")
variables.gameWindow.setup(width = 1200, height = 700, startx = 0, starty = 0)
variables.gameWindow.bgpic(variables.unnamedMapPath)

# Starting game window: enter name
playerName = variables.gameWindow.textinput("Turkey Geo Guesser",
                                  "Welcome to Turkey Geo Guesser, \n"
                                  "Test your knowledge on Turkish provinces. \n\n"
                                  "Features: \n"
                                  "1) Keeping track with your score\n"
                                  "2) Supports non-turkish keyboards (letters)\n"
                                  "3) Exclusive cheatsheet (Don't use it, challenge yourself)\n\n"
                                  "Please enter your name to start playing")

# Starting game: show map and username
variables.name.up()
variables.name.goto(-500, 300)
variables.name.write("Welcome " + playerName + "!", move = True, font = ("Verdana", 14, "bold"))

# Show score and buttons
functions.renderCorrect(variables.correctGuesses)
functions.renderPlayButton()
functions.renderCheatSheetButton()

# On window click event for button simulation
variables.gameWindow.onclick(functions.detectClick)

turtle.done()
