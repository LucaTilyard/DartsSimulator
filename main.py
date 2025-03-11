from player import *
import matplotlib.pyplot as plt
from src.methods import *

luke_the_fluke_shittler = Player(4)

print(luke_the_fluke_shittler.Throw(100))

# Dartboard Score Sections (Angles)
angles = np.linspace(1/20*np.pi, 2 * np.pi+1/20*np.pi, 21)

#Generate all angles for a smooth plotting
all_angles = np.linspace(0, 2 * np.pi, 1000)

# Rings (Dartboard Circles)
radii = [0.028, 0.071, 0.582, 0.629, 0.953, 1.0] 

# Create a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Draw the circular dartboard rings
for r in radii:
    ax.plot(all_angles, [r] * len(all_angles), color='black')

# Draw the radial lines for 20 segments
for angle in angles:
    ax.plot([angle, angle], [0, 1], color='black')

# Remove axes
#ax.set_xticklabels([])
#ax.set_yticklabels([])
#ax.set_yticks([])
#ax.set_frame_on(False)

"""
# Load the image
image = plt.imread('src/dartboard.png')

# Create a figure and axis
fig, ax = plt.subplots()

# Display the image
ax.imshow(image, extent=[-1.345, 1.345, -1.345, 1.345])

plt.xlim(-1.345, 1.345)
plt.ylim(-1.345, 1.345)"
"""

# ax.spines['left'].set_color('none')
# ax.spines['bottom'].set_color('none')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#plt.xticks([])
#plt.yticks([])

i = 0
score = 0
while i < 3:
    throw = luke_the_fluke_shittler.Throw(1)
    polar = ConvertToPolar(throw[0], throw[1])
    dartScore = CalculateValue(polar[0], polar[1])
    print(dartScore)
    plt.scatter(polar[0], polar[1], s=3, c='red', marker='o')
    score += dartScore
    i += 1
print(f"Total Score: {score}")
plt.show()

