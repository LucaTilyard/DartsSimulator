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

    def Throw(self):
         x = np.random.normal(self.targeting[0],(1/self.skill))
         y = np.random.normal(self.targeting[1],(1/self.skill))
         return np.array([x,y])

    def Aim(self, Number, Multiplier):
        if Multiplier not in ["Single", "Double", "Treble"]:
            raise ValueError("Multiplier must be either 'Single', 'Double', 'Treble'")

        self.targeting[0] = TargetingValues.at[NumberToIndex[Number], f'{Multiplier}X']
        self.targeting[1] = TargetingValues.at[NumberToIndex[Number], f'{Multiplier}Y']

    def Checkout(self, score):

        #No checkpout or bust
        if score > 170 or score <= 1:
            return None

        #define all doubles
        doubles = {2*i: [i,"Double"] for i in range(1, 21) }
        doubles[50] = [0 , "Double"]

        #define all Singles
        singles = {i: [i,"Single"] for i in range(1, 21)}
        singles[25] = [0 , "Single"]

        # Define trebles
        trebles = {3*i: [i,"Treble"] for i in range(1, 21)}

        #merge them
        possible_shots = {**trebles, **singles,  **doubles}

        # one dart checkouts
        if score in doubles:
            return [doubles[score],0,0]

        # 2 darts cehckouts
        for first in possible_shots:
            remaining = score - first
            if remaining in doubles:
                return [possible_shots[first]]

        # three dart checkouts
        for first in possible_shots:
            for second in possible_shots:
                remaining = score - first - second
                if remaining in doubles:
                    return [possible_shots[first]]