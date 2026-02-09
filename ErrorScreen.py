from PyUI.PageElements import *
from PyUI.Screen import Screen
from PyUI.Window import Window

class ConditionScreen(Screen):
    def __init__(self, window):  # Add Computer Player When Done!
        super().__init__(window, (255, 0, 0))
        self.state = {
            "goTo": False,
            "locked": False
        }
        self.elements = [
            Label((50, 90), 50, 50, "An Error Occured!", 20, (255,255,255)),
            Label((50, 70), 50, 50, "Player Choice = None", 20, (255,255,255)),
            QuitButton(),


        ]
        
class QuitButton(Button):
    def __init__(self):
        super().__init__((50, 20), 30, 10, "Quit Application", (255, 255,255), (0,0,0))

    def onClick(self, screen):
        quit()