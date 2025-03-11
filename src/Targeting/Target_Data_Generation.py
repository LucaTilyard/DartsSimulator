import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# All target points can be generated in cartesian
# coordinates by calculating in polar then converting.

thetas = np.linspace(-np.pi, np.pi, 21)
# This produces two points that are the same for opposite 6, these need to be manuly changed after the be the bull locations.

TargetingValues = pd.DataFrame(np.arange(126).reshape(21, 6), columns=['SingleX','SingleY', 'DoubleX','DoubleY', 'TrebleX', 'TrebleY'])

# Generate Treble locations
# all thetas with r = 21/34.
index = 0
for theta in thetas:
    TargetingValues.at[index, 'TrebleX'] = (21.0/34) * np.cos(theta)
    TargetingValues.at[index, 'TrebleY'] = (21.0/34) * np.sin(theta)
    index += 1

# Generate Double locations
# all thetas with r = 83/85.
index = 0
for theta in thetas:
    TargetingValues.at[index, 'DoubleX'] = (83.0/85) * np.cos(theta)
    TargetingValues.at[index, 'DoubleY'] = (83.0/85) * np.sin(theta)
    index += 1

# Generate single locations
# all thetas with r = 269/340.
index = 0
for theta in thetas:
    TargetingValues.at[index, 'SingleX'] = (269.0/340) * np.cos(theta)
    TargetingValues.at[index, 'SingleY'] = (269.0/340) * np.sin(theta)
    index += 1

# Manualy chnage duplicated value to be Bull and outer Bull
TargetingValues.at[0, 'SingleX'] = (287.0/3400)* np.cos(np.pi/2)
TargetingValues.at[0, 'SingleY'] = (287.0/3400) * np.sin(np.pi/2)
TargetingValues.at[index, 'DoubleX'] = 0
TargetingValues.at[index, 'DoubleY'] = 0
TargetingValues.at[index, 'TrebleX'] = 0
TargetingValues.at[index, 'TrebleY'] = 0

# Export Data To File
TargetingValues.to_csv('TargetingData.csv', index=False)

