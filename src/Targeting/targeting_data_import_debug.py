import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from src.dartboard import Dartboard

# All target points can be generated in cartesian
# coordinates by calculating in polar then converting
TargetingValues = pd.read_csv('TargetingData.csv')

board = Dartboard()

board.plot()

# This is actually broken at the moment, however have not fixed currently as it is not essential for the project
plt.scatter(TargetingValues['DoubleX'], TargetingValues['DoubleY'], color='yellow')
plt.scatter(TargetingValues['TrebleX'], TargetingValues['TrebleY'], color='blue')
plt.scatter(TargetingValues['SingleX'], TargetingValues['SingleY'], color='red')

plt.show()

print(TargetingValues)