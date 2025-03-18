import numpy as np
from numpy.f2py.auxfuncs import throw_error

angels = np.linspace(-np.pi-(1/20*np.pi), np.pi+(1/20*np.pi), 22)

def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    return r, theta




