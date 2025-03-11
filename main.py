from player import *
import matplotlib.pyplot as plt
from src.methods import *

luke_the_fluke_shittler = Player(21)

angles = np.linspace(1/20*np.pi, 2*np.pi+1/20*np.pi, 21)

print(luke_the_fluke_shittler.Throw(100))

# Load the image
image = plt.imread('src/dartboard.png')

# Create a figure and axis
fig, ax = plt.subplots()

# Display the image
ax.imshow(image, extent=[-1.345, 1.345, -1.345, 1.345])

for angle in angles:
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], color='black')

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
    luke_the_fluke_shittler.Aim(18, "Single")
    throw = luke_the_fluke_shittler.Throw(1)
    polar = ConvertToPolar(throw[0], throw[1])
    dartScore = CalculateValue(polar[0], polar[1])
    print(dartScore)
    plt.scatter(throw[0], throw[1], s=3, c='yellow', marker='o')
    score += dartScore
    i += 1
print(f"Total Score: {score}")
plt.show()

