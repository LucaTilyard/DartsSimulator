from src.player import *
import matplotlib.pyplot as plt
from src.methods import *
from src.dartboard_plot import plot_dartboard
from src.dartboard import Dartboard

luke_littler = Player(25)
board = Dartboard()

board.plot()

i = 0
score = 501
while i < 3:
    if score <= 170 and score!= 169 and score != 168 and score != 166 and score != 165 and score != 163 and score != 162 and score != 159:
        checkout = luke_littler.checkout(score)
        print(checkout)
        luke_littler.aim(checkout[0][0], checkout[0][1])
        throw = luke_littler.throw()
        polar = cartesian_to_polar(throw[0], throw[1])
        dartScore = board.calculate_value(polar[0], polar[1])
        plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o',zorder=2)

    else:
        luke_littler.aim(20, "Treble")
        print("Aiming for 20 Treble")
        throw = luke_littler.throw()
        polar = cartesian_to_polar(throw[0], throw[1])
        dartScore = board.calculate_value(polar[0], polar[1])
        plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o',zorder=2)

    score -= dartScore
    if score == 0:
        print("Checkout!")
        break
    i += 1
print(f"Remaining Score: {score}")
plt.show()



