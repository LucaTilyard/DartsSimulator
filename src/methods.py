import numpy as np
from numpy.f2py.auxfuncs import throw_error

angels = np.linspace(-np.pi-(1/20*np.pi), np.pi+(1/20*np.pi), 22)

def ConvertToPolar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    return r, theta

def CalculateValue(r, theta):
    Multiplier = 1
    BoardOrder = [11, 8, 16, 7, 19, 3, 17, 2, 15, 10, 6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11]

    # Within board.
    if r > 1:
        return 0

    # Bullseye.
    if r < 127/3400:
        return 50

    # Outer Bullseye.
    if r < 8/85:
        return 25

    # Triple.
    if (99 / 170) < r < (107 / 170):
        Multiplier = 3

    # Double.
    if (81 / 85) < r < 1:
        Multiplier = 2

    # Calculate unmultiplied score
    i = 0
    for i in range(21):
        if theta < angels[i+1]:
            return Multiplier * BoardOrder[i]
        i += 1


