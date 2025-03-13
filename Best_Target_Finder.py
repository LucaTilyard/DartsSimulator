from player import *
import matplotlib.pyplot as plt
from src.methods import *
from Dartboardplot import *
import numpy as np



score = 0
records = []
records_per_ability = []
player = Player(1)

for skill in range(1, 200):
    player.change_skill(skill)
    for multi in ["Single", "Double", "Treble"]:
        for target_number in range(21):
            i = 0
            while i < 1000:
                player.Aim(target_number, multi)
                throw = player.Throw()
                polar = ConvertToPolar(throw[0], throw[1])
                dartScore = CalculateValue(polar[0], polar[1])
                score += dartScore
                i += 1
            records.append([score/1000, target_number, multi])
            #print(f"500 dart average: {score/1000}")
            score = 0
        records.sort(reverse=True)
    print(skill)
    records_per_ability.append([f"skill level: {skill}",records])
    records = []
print(records_per_ability)

with open('data.txt', 'w') as f:
    for line in records_per_ability:
        f.write(f"{line}\n")