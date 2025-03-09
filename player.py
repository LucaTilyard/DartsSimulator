import numpy as np

class Player:
    def __init__(self, skill):
        self.skill = skill
        self.average = 0

    def __str__(self):
        return f"Player of skill level: {self.skill}"

    def Throw(self, target):
         x = np.random.normal(0,(1/self.skill))
         y = np.random.normal((21/34),(1/self.skill))
         return np.array([x,y])
