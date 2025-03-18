import numpy as np
import pandas as pd

# This Data should not be kept here but for the moment it will do
TargetingValues = pd.read_csv('src/Targeting/TargetingData.csv')
BoardOrder = [13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10,6]

# This array exists so when the number your aiming for is used as the index it will return the index of its location in the data frame
NumberToIndex = [0, 15, 8, 6, 13, 17, 11, 4, 2, 19, 10, 1, 18, 12, 20, 9, 3, 7, 14, 5, 16]

class Player:
    """
       A class to represent a dart player.

       This class provides methods to initialize a player with a certain skill level,
       simulate a dart throw, aim at a specific target, and determine checkout strategies
       based on the current score.

       Attributes
       ----------
       skill : float
           The skill level of the player, affecting the accuracy of throws.
       average : float
           The average score of the player.
       targeting : list
           The target coordinates (x, y) for the player's throw.

       Methods
       -------
       __str__():
           Returns a string representation of the player.
       throw():
           Simulates a dart throw based on the player's skill level.
       aim(number, multiplier):
           Sets the target coordinates for the player's throw based on the desired number and multiplier.
       checkout(score):
           Determines the best checkout strategy for the given score.
    """

    def __init__(self, skill):
        """
            Initializes the Player class with a given skill level.

            Parameters
            ----------
            skill : float
                The skill level of the player. Higher values indicate better accuracy.

            Returns
            -------
            None
        """
        self.skill = skill
        self.average = 0
        self.targeting = [0,0]

    def __str__(self):
        return f"Player of skill level: {self.skill}"

    def throw(self):
        """
            Simulates a dart throw based on the player's skill level.

            The throw is modeled as a normal distribution centered around the target coordinates,
            with a standard deviation inversely proportional to the player's skill level.

            Returns
            -------
            numpy.ndarray
                The coordinates (x, y) of the dart throw.
        """
        x = np.random.normal(self.targeting[0],(1/self.skill))
        y = np.random.normal(self.targeting[1],(1/self.skill))
        return np.array([x,y])

    def aim(self, number, multiplier):
        """
            Sets the target coordinates for the player's throw based on the desired number and multiplier.

            Parameters
            ----------
            number : int
                The number the player is aiming for.
            multiplier : str
                The multiplier for the target ('Single', 'Double', 'Treble').

            Raises
            ------
            ValueError
                If the multiplier is not 'Single', 'Double', or 'Treble'.

            Returns
            -------
            None
        """
        if multiplier not in ["Single", "Double", "Treble"]:
            raise ValueError("Multiplier must be either 'Single', 'Double', 'Treble'")

        self.targeting[0] = TargetingValues.at[NumberToIndex[number], f'{multiplier}X']
        self.targeting[1] = TargetingValues.at[NumberToIndex[number], f'{multiplier}Y']

    def checkout(self, score):
        """
            Determines the best checkout strategy for the given score.

            Parameters
            ----------
            score : int
                The current score of the player.

            Returns
            -------
            list or None
                A list of tuples representing the best checkout strategy, or None if no checkout is possible.
        """

        #No checkout or bust
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
            return [doubles[score]]

        # 2 darts checkouts
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