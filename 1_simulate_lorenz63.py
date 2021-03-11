"""
Created on Fri Jan 29 04:25:27 2021

@author: vborse
"""

from IPython.display import clear_output, display, HTML

import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
import random

from module import lorenz
from module import trajectory




"""Generating set of random points as initial conditions within a defined range"""
#xx = np.random.choice(range(-30,30),100)
#yy = np.random.choice(range(-30,30),100)
#zz = np.random.choice(range(0,30),100)

xx = [  2,  15, -26,   3, -17,   2,  -9,  27,  22, -14, -24,  12,   1,
         5,  22, -12, -28, -15,   5,  28, -26, -29,  21,  -8,  12, -29,
        16,  23,  19,  -9, -18,  25, -14,  25, -20,   4,  24,  -1,  15,
        12, -20, -18,  11, -10, -25,   6, -27,  13,  23,  -5,  20,   3,
        27,  28, -30,  12, -14,  -1,   4, -14,  24,  22, -20, -15,  19,
       -25, -17,  11, -11,  16,  17,  -4, -29,   7,  23, -30,   0,  11,
        10, -18,  26,   6,   8,   0,   0,  27, -25, -21,  25,  28,  24,
         2,  18,   7, -19, -26, -19, -12, -22,   4]
yy = [ 24, -14,  28,   9,  23, -16, -30,  -7, -24,  -4,  25,  21,   5,
         6,  -1, -24,  -5,  -2, -15,  -6, -20,  17, -27, -25, -24, -29,
        10,  -6,  21,  28,  13, -28, -25,  16,  -8,   6,   8, -13, -26,
        22,  17,  28, -30,  -4,   1,  -4, -10,  -9,  19, -17,  27,  28,
        26,  -2, -29,  10, -18,   5,   5,   1,   6,   6,  10, -15,   0,
        -5,  21,   1,   7,   4,  10,  -8, -29,  -5,  14,   0, -11, -23,
        29,   7,   2, -26,  19, -17,   8, -20, -29,   3,  -4,  11,  15,
        21,  11, -15, -27,  15, -19,   0, -27, -14]
zz = [ 7,  7,  9,  6, 13,  4, 27, 19,  1,  6, 17,  7, 25, 22, 26, 14,  4,
       23,  8,  7,  3, 17, 24,  6, 23, 23, 18,  4,  8,  3,  9, 19, 29, 22,
        6,  3, 12, 21, 20,  0, 28,  3, 10,  6,  0,  0, 15, 28,  3,  6,  3,
        9, 26, 25, 11,  1, 27,  5,  7, 25, 24, 17, 15, 26, 17, 19, 24,  3,
        7, 14, 14,  4, 25, 11,  0, 13,  9, 16,  3, 29, 27, 23,  2,  0,  2,
       14,  7, 15, 22,  5, 12, 21, 20, 21,  2, 11, 26,  1,  7, 21]






#--------------------------------------------------------------------------------------------------------------------       
# forming trajectories
pts=trajectory(0.01,10000,99)

with open('pts.npy', 'wb') as h:
    np.save(h, pts)


