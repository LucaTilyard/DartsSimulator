import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# All target points can be generated in cartesian
# coordinates by calculating in polar then converting
TargetingValues = pd.read_csv('TargetingData.csv')

# Create a figure and axis
fig, ax = plt.subplots()

# Load the image
image = plt.imread('../dartboard.png')

# Display the image
ax.imshow(image, extent=[-1.345, 1.345, -1.345, 1.345])

plt.xlim(-1.345, 1.345)
plt.ylim(-1.345, 1.345)

ax.scatter(TargetingValues['DoubleX'], TargetingValues['DoubleY'], color='yellow')
ax.scatter(TargetingValues['TrebleX'], TargetingValues['TrebleY'], color='blue')
ax.scatter(TargetingValues['SingleX'], TargetingValues['SingleY'], color='red')

plt.show()

print(TargetingValues)