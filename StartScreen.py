# Please dont touch me, i need to move back a directory
import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import importlib


from PyUI.PageElements import *
from PyUI.Screen import Screen
from PyUI.Window import Window
DEBUG_COMPONENT = False

last_mtime = os.path.getmtime(__file__)

class ConditionScreen(Screen):
    def __init__(self, window):  # Add Computer Player When Done!
        super().__init__(window, (25, 25, 0))
        self.state = {
            "goTo": False,
            "locked": False
        }


    def elementsToDisplay(self):
        self.elements = [
            Label((50, 90), 50, 50, "Ready to Play?!!", 20, (0,255,0)),
            PlayAgain() 
        ]

class PlayAgain(Button):
    def __init__(self):
        super().__init__((50, 20), 30, 10, "Lets Go!", (255, 255,255), (0,0,0))

    def onClick(self, screen):
        screen.state["goTo"] = "PlayGame"

# For Debug Purposes
if DEBUG_COMPONENT == True:
    window = Window("GUI - RPS - DEBUG (StartScreen.py)", (0,255,0)) 
    screen = ConditionScreen(window)
    while True:
        window.checkForInput(screen) 
        window.checkForHover(screen)
        window.update(screen)
