from tkinter import messagebox
import variables
import provinces


# Helping functions
def renderAnswer(x, y, turtleType, value, label = "", extra = ''):
    turtleType.goto(x, y)
    turtleType.write(label + " ", move = True, font = ("Verdana", 10, "normal"))
    turtleType.write(str(value) + extra)


def renderButton(button, label, startX, startY, width, height, labelOffset):
    button.penup()
    button.begin_fill()
    button.goto(startX, startY)
    button.goto(startX + width, startY)
    button.goto(startX + width, startY + height)
    button.goto(startX, startY + height)
    button.goto(startX, startY)
    button.end_fill()
    button.goto(startX + 15, startY + labelOffset)
    button.fillcolor("black")
    button.pencolor("white")
    button.write(label, font=("Verdana", 10, "bold"))


# Render correct answer component on screen
def renderCorrect(value):
    if value == 81:
        messagebox.showinfo("Game ended", "Thank you for playing!")
        variables.gameWindow.bye()
    renderAnswer(0, 300, variables.correct, value, "Correct: ", " / " + str(81))


# Analyze and show results of user answer
def analyzeAnswer(answer):
    isGuessed = False
    isFound = False

    if answer.upper() in variables.guessed:
        isGuessed = True
        messagebox.showwarning("Warning", "Already entered, Try another province")

    for prov, coordinates in provinces.provinces.items():
        if (answer.upper() == prov.upper()) & (not isGuessed):
            isFound = True
            global correctGuesses
            variables.correctGuesses = variables.correctGuesses + 1
            variables.guessed.append(prov.upper())

            variables.correct.clear()
            renderCorrect(variables.correctGuesses)
            renderAnswer(coordinates[0], coordinates[1], variables.province, answer)
            break

    if (not isGuessed) & (not isFound):
        messagebox.showerror("Warning", "No such province, please try again")


# Render game buttons
def renderPlayButton():
    renderButton(variables.playButton, "Guess", 300, -300, 70, -30, -23)


def renderCheatSheetButton():
    renderButton(variables.cheatSheetButton, "Cheatsheet", 400, -300, 110, -30, -23)


def detectClick(x, y):
    # Guess button
    if 300 <= x <= 370 and -330 <= y <= -300:
        playerGuess = variables.gameWindow.textinput("Guessing...", "Please enter a province name in Turkey")
        analyzeAnswer(playerGuess)

    # Cheatsheet: open - close buttons
    elif 400 <= x <= 510:
        if -330 <= y <= -300:
            variables.gameWindow.bgpic(variables.namedMapPath)

            variables.playButton.clear()
            variables.cheatSheetButton.clear()

            renderButton(variables.closeCheatSheetButton, "Close Cheatsheet", 400, 300, 150, 30, 7)
        else:
            variables.gameWindow.bgpic(variables.unnamedMapPath)
            variables.closeCheatSheetButton.clear()
            renderPlayButton()
            renderCheatSheetButton()
