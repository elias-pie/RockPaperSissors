import random
class ComputerEngine():
    def __init__(self):
        self.state = {
            "selected": False
        }
        self.idStorage = {
                "Rock": {
                    "ID": 1,
                },

                "Paper": {
                    "ID": 2,
                },

                "Sissors": {
                    "ID": 3,
                }
            },

    def chooseComputer(self):
        randomized = random.randint(1,3)
        if randomized == 1:
            return 1 # Rock
        elif randomized == 2:
            return 2 # Paper
        elif randomized == 3: 
            return 3 # Sissors
