from player import *
import matplotlib.pyplot as plt
from src.methods import *

luke_the_fluke_shittler = Player(14)

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
score = 58
while i < 3:
    if score <= 170 and score!= 169 and score != 168 and score != 166 and score != 165 and score != 163 and score != 162 and score != 159:
        checkout = luke_the_fluke_shittler.Checkout(score)
        print(checkout)
        luke_the_fluke_shittler.Aim(checkout[0][0] , checkout[0][1])
        throw = luke_the_fluke_shittler.Throw()
        polar = ConvertToPolar(throw[0], throw[1])
        dartScore = CalculateValue(polar[0], polar[1])
        plt.scatter(throw[0], throw[1], s=3, c='blue', marker='o')

    else:
        luke_the_fluke_shittler.Aim(20 , "Treble")
        print("Aiming for 20 Treble")
        throw = luke_the_fluke_shittler.Throw()
        polar = ConvertToPolar(throw[0], throw[1])
        dartScore = CalculateValue(polar[0], polar[1])
        plt.scatter(throw[0], throw[1], s=3, c='blue', marker='o')

    score -= dartScore
    if score == 0:
        print("Checkout!")
        break
    i += 1
print(f"Remaining Score: {score}")
plt.show()



