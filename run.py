from PyUI.Window import Window
import time
##import the custom screens you made---
from Selection import PlayScreen
from ComputerPlayer import ComputerEngine
## My Screens
from StartScreen import ConditionScreen as StartScreen
from ConditionScreens.WinScreen import ConditionScreen as WinScreen
from ConditionScreens.TieScreen import ConditionScreen as TieScreen
from ConditionScreens.LooseScreen import ConditionScreen as LooseScreen
from ErrorScreen import ConditionScreen as ErrorScreen
##-------------------------------------

#     "Rock": {
#         "ID": 1,
#         "Selected": 0,
#     },
#     "Paper": {
#         "ID": 2,
#         "Selected": 0,
#     },
#     "Sissors": {
#         "ID": 3,
#         "Selected": 0,
#     }
# },



window = Window("GUI - RPS", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
playScreen = PlayScreen(window)
startScreen = StartScreen(window)
error = ErrorScreen(window)
##-----------------------------------

screen = startScreen ##set screen to be the starting screen



Data = {
    "TieCount": 0,
    "WinCount": 0,
    "LooseCount": 0,
    "screen": startScreen,
    "roundComplete": False
}

# Arthritis Exists
def gameTie(Data):
     Data["TieCount"] += 1
     Data["screen"] = TieScreen(window, ComputerChoice)
     Data["roundComplete"] = True

def gameWin(Data):
     Data["WinCount"] += 1
     Data["screen"] = WinScreen(window, ComputerChoice)
     Data["roundComplete"] = True

def gameLoose(Data):
     Data["LooseCount"] += 1
     Data["screen"] = LooseScreen(window, ComputerChoice)
     Data["roundComplete"] = True

def runComputer():
    computerPlayer = ComputerEngine()
    ComputerChoice = computerPlayer.chooseComputer()
    return computerPlayer, ComputerChoice
execCount = 0
computerPlayer, ComputerChoice = runComputer()
while True: ##Game loop
    screen = Data["screen"]


    # I Find things simpler if I put the logic IN the run.py instead of the Selection.py file
    # Sure it may be longer, but is a whole heck of a lot easier to debug


    if screen.state.get("goTo") == "PlayGame":
        Data["screen"] = PlayScreen(window)
        screen.state['goTo'] = 'idle'

    if screen.state.get('locked') == True:
        execCount += 1
        #ComputerChoice = computerPlayer.chooseComputer()  # why did I add this here? that caused 2 days of issues XP
        playerChoice = screen.state.get("selected")
        print('==============================================')
        print('Execution Count '+str(execCount))
        print("cosen")
        print('CompChoice'+str(ComputerChoice))
        print('PlayerChoice'+str(playerChoice))
        if playerChoice == None:
            Data["screen"] = error

        # Tie Conditions
        if ComputerChoice == 1 and playerChoice == 1:
            gameTie(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()
        if ComputerChoice == 2 and playerChoice == 2:
            gameTie(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        if ComputerChoice == 3 and playerChoice == 3:
            gameTie(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        # Rock beats sissors
        if ComputerChoice == 1 and playerChoice == 3:
            gameLoose(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        if ComputerChoice == 3 and playerChoice == 1:
            gameWin(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        # Paper Beats Rock
        if ComputerChoice == 2 and playerChoice == 1:
            gameLoose(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        if ComputerChoice == 1 and playerChoice == 2:
            gameWin(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        # Sissors beat paper
        if ComputerChoice == 3 and playerChoice == 2:
            gameLoose(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

        if ComputerChoice == 2 and playerChoice == 3:
            gameWin(Data)
            print('execCheck')
            computerPlayer, ComputerChoice = runComputer()

    if Data["roundComplete"] == True:
        if screen.state.get("playAgain") == True:
            Data["screen"] == playScreen
            playScreen.state["selected"] = False

    ##----------------------------------------------------
    window.checkForInput(screen) #checks for inputs on the screen # For some reason, idk where, but this needs to be used with the fork by elias-pie (https://github.com/elias-pie/PyUI), I tried commenting it out. It crashed second it launched
    window.checkForHover(screen) #checks for hover on the screen
    window.update(screen) #updates the window to reflect the new screen