import numpy as np
from numpy.f2py.auxfuncs import throw_error

angels = np.linspace(1/20*np.pi, 2*np.pi+1/20*np.pi, 20)

def ConvertToPolar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    if theta < 0:
        theta = np.pi + theta

    return r, theta

def CalculateValue(r, theta):
    Multiplier = 1
    BoardOrder = [13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10,6]

    # Within board.
    if r > 1:
        return 0

    # Bullseye.
    if r < 61/850:
        return 50

    # Outer Bullseye.
    if r < 16/85:
        return 25

    # Triple.
    if r < (107/170) and r > (99/170):
        Multiplier = 3

    # Double.
    if r < (81/85) and r > 1:
        Multiplier = 2

    # Calculate unmultiplied score
    i = 0
    for i in range(20):
        if theta < angels[i+1] and theta > angels[i]:
            return Multiplier * BoardOrder[i]
        i += 1


