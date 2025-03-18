from src.player import Player
from src.dartboard import Dartboard
from src.methods import *
import matplotlib.pyplot as plt

player_name = input("Player name: ")
player_skill = float(input("Opponent skill level: "))

# Initialise bot for user to play against
bot = Player(player_skill)
board = Dartboard()

print(f"Game Starts: Player {player_name} vs Bot level {player_skill}")

user_score = 501
bot_score = 501

def round(bot, user_score, bot_score):

    board.plot()
    i = 0
    while i < 3:
        if bot_score <= 170 and bot_score != 169 and bot_score != 168 and bot_score != 166 and bot_score != 165 and bot_score != 163 and bot_score != 162 and bot_score != 159:
            checkout = bot.checkout(bot_score)
            print(checkout)
            bot.aim(checkout[0][0], checkout[0][1])
            throw = bot.throw()
            polar = cartesian_to_polar(throw[0], throw[1])
            dartScore = board.calculate_value(polar[0], polar[1])
            plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o', zorder=2)

        else:
            bot.aim(20, "Treble")
            print("Aiming for 20 Treble")
            throw = bot.throw()
            polar = cartesian_to_polar(throw[0], throw[1])
            dartScore = board.calculate_value(polar[0], polar[1])
            plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o', zorder=2)

        bot_score -= dartScore
        if bot_score == 0:
            print("Sorry you lost")
            break
        i += 1
    print(f"Remaining Score: {bot_score}")
    plt.show()

    return user_score, bot_score


while user_score > 0 and bot_score > 0:
    print(f"Player {player_name} score: {user_score}")
    print(f"Bot score: {bot_score}")
    user_throw = input(f"{player_name} Enter score: ")

    if user_score - int(user_throw) == 0:
        print(f"Congratulations {player_name} you have won the game")
        break

    if user_score - int(user_throw) < 0:
        print("bust !")
        #This is to counteract the subtraction of score that's about to happen
        user_score = user_score - int(user_throw)

    user_score = user_score - int(user_throw)
    user_score, bot_score = round(bot, user_score, bot_score)

# This output need a little bit of work to make it more user friendly. Very cluttered at the moment
# also add checking for legit scores