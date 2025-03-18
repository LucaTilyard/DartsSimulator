from player import *
import matplotlib.pyplot as plt
from src.methods import *
from Dartboardplot import plot_dartboard

luke_the_fluke_shittler = Player(25)

plot_dartboard()

i = 0
score = 1000000
while i < 1000:
    if score <= 170 and score!= 169 and score != 168 and score != 166 and score != 165 and score != 163 and score != 162 and score != 159:
        checkout = luke_the_fluke_shittler.Checkout(score)
        print(checkout)
        luke_the_fluke_shittler.Aim(checkout[0][0] , checkout[0][1])
        throw = luke_the_fluke_shittler.Throw()
        polar = ConvertToPolar(throw[0], throw[1])
        dartScore = CalculateValue(polar[0], polar[1])
        plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o',zorder=2)

    else:
        luke_the_fluke_shittler.Aim(20 , "Treble")
        print("Aiming for 20 Treble")
        throw = luke_the_fluke_shittler.Throw()
        polar = ConvertToPolar(throw[0], throw[1])
        dartScore = CalculateValue(polar[0], polar[1])
        plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o',zorder=2)

    score -= dartScore
    if score == 0:
        print("Checkout!")
        break
    i += 1
print(f"Remaining Score: {score}")
plt.show()



