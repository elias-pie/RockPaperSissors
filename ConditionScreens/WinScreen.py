# Please dont touch me, i need to move back a directory
import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import importlib


from PyUI.PageElements import *
from PyUI.Screen import Screen
from PyUI.Window import Window

# DEBUG
DEBUG_COMPONENT = False
if DEBUG_COMPONENT == True:
    import ComputerPlayer
    computer = ComputerPlayer.ComputerEngine() 
    computer.chooseComputer()

last_mtime = os.path.getmtime(__file__)

class ConditionScreen(Screen):
    def __init__(self, window, computerPlayer):  # Add Computer Player When Done!
        super().__init__(window, (30, 0, 90))
        self.state = {
            "goTo": False,
            "locked": False
        }
        self.computerChoice = False
        if computerPlayer == 1:
            self.computerChoice = "Rock"
        if computerPlayer == 2:
            self.computerChoice = "Paper"
        if computerPlayer == 3:
            self.computerChoice = "Sissors"

        self.elements = [
            Label((50, 90), 50, 50, "You Win!", 20, (0,255,0)),
            Label((50, 30), 50, 50, ("Computer Chose: "+str(self.computerChoice)), 20, (255,200,0)), # Replace dummy w/  screen.computerChoice
            PlayAgain() 
        ]
        print('WhatTheScreenSaw '+self.computerChoice) # I dont know why it will sometimes that it recieved 2 answers, and it appears to be ALWAYS sissors. But it works as intended right now so im not going to touch this and let it do its thing.

class PlayAgain(Button):
    def __init__(self):
        super().__init__((50, 20), 30, 10, "Play Again", (255, 255,255), (0,0,0))

    def onClick(self, screen):
        screen.state["goTo"] = "PlayGame"

# For Debug Purposes
if DEBUG_COMPONENT == True:
    window = Window("GUI - RPS - DEBUG (WinScreen.py)", (0,255,0)) 
    screen = ConditionScreen(window, computer)
    while True:
        window.checkForInput(screen) 
        window.checkForHover(screen)
        window.update(screen)
