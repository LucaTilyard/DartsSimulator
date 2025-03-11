import numpy as np
import pandas as pd

# This Data should not be kept here but for the moment it will do
TargetingValues = pd.read_csv('src/Targeting/TargetingData.csv')
BoardOrder = [13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10,6]

# This array exists so when the number your aiming for in used as the index it will return the index of its location in the data frame
NumberToIndex = [0, 15, 8, 6, 13, 17, 11, 4, 2, 19, 10, 1, 18, 12, 20, 9, 3, 7, 14, 5, 16]

class Player:
    def __init__(self, skill):
        self.skill = skill
        self.average = 0
        self.targeting = [0,0]

    def __str__(self):
        return f"Player of skill level: {self.skill}"

    def Throw(self, target):
         x = np.random.normal(self.targeting[0],(1/self.skill))
         y = np.random.normal(self.targeting[1],(1/self.skill))
         return np.array([x,y])

    def Aim(self, Number, Multiplier):
        if Multiplier not in ["Single", "Double", "Treble"]:
            raise ValueError("Multiplier must be either 'Single', 'Double', 'Treble'")

        # It's late, i'm tired, ive no clue why + 1 fixes this but it does so ill check it out another time. Must be sthm to do with indexs starting at 0
        self.targeting[0] = TargetingValues.at[NumberToIndex[Number]-1, f'{Multiplier}X']
        self.targeting[1] = TargetingValues.at[NumberToIndex[Number]-1, f'{Multiplier}Y']
