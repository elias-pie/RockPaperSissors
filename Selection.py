from PyUI.PageElements import *
from PyUI.Screen import Screen
from PyUI.Window import Window
DEBUG_COMPONENT = False
hoverAmount = 0

class PlayScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (27, 27, 27))
        self.state = {
            "locked": False,
            "selected": None,
            "Buttons": {
                "Rock": {
                    "ID": 1,
                    "Selected": 0,
                },

                "Paper": {
                    "ID": 2,
                    "Selected": 0,
                },

                "Sissors": {
                    "ID": 3,
                    "Selected": 0,
                }
            },
            "goTo": "active" 
        }

    def elementsToDisplay(self):
        self.elements = [
            RockButton(),
            ScissorsButton(),
            PaperButton(),
            Label((50, 90), 50, 20, "Select One:", 14, (255,255,255), (0,0,0)),
            Image((20, 50), 20, 20, "./assets/stone.png"),
            Image((50, 50), 20, 20, "./assets/scissor.png"),
            Image((80, 50), 20, 20, "./assets/paper.png"),
        ]

class RockButton(Button):
    def __init__(self):
        super().__init__((20, 20), 10, 10, "Rock", (255, 255,255), (0,0,0))

    def onClick(self, screen):
        screen.state["locked"] = True
        screen.state["selected"] = 1
        print('Selected Rock')

class ScissorsButton(Button):
    def __init__(self):
        super().__init__((50, 20), 10, 10, "Scissors", (255, 255,255), (0,0,0))

    def onClick(self, screen):
        screen.state["locked"] = True
        screen.state["selected"] = 3
        print('Selected Sissors')

class PaperButton(Button):
    def __init__(self):
        super().__init__((80, 20), 10, 10, "Paper", (255, 255,255), (0,0,0))
 
    def onClick(self, screen):
        screen.state["locked"] = True
        screen.state["selected"] = 2
        print('Selected Paper')
        print(screen.state["selected"])
        # quit() - WHY WAS THERE A RANDOM QUIT FUNCTION IN HERE?!?!??!

# For Debug Purposes
if DEBUG_COMPONENT == True:
    window = Window("GUI - RPS - DEBUG (Selection.py)", (0,255,0)) 
    screen = PlayScreen(window)
    while True:
        window.checkForInput(screen) 
        window.checkForHover(screen)
        window.update(screen)