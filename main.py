from player import *
import matplotlib.pyplot as plt
from src.methods import *

luke_the_fluke_shittler = Player(10)

# Load the image
image = plt.imread('src/dartboard.png')

# Create a figure and axis
fig, ax = plt.subplots()

# Display the image
ax.imshow(image, extent=[-1.345, 1.345, -1.345, 1.345])


plt.xlim(-1.345, 1.345)
plt.ylim(-1.345, 1.345)

# ax.spines['left'].set_color('none')
# ax.spines['bottom'].set_color('none')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#plt.xticks([])
#plt.yticks([])

i = 0
score = 0
while i < 3:
    luke_the_fluke_shittler.Aim(20, "Treble")
    throw = luke_the_fluke_shittler.Throw()
    polar = ConvertToPolar(throw[0], throw[1])
    dartScore = CalculateValue(polar[0], polar[1]
    plt.scatter(throw[0], throw[1], s=3, c='yellow', marker='o')

    score += dartScore
    i += 1
print(f"Total Score: {score}")
plt.show()

