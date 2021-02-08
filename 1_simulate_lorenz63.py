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





def lorenz(x, y, z,dt, s=10, r=28, b=8/3):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
       
    Returns:
       dt*x_dot, dt*y_dot, dt*z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    
    return dt*x_dot, dt*y_dot, dt*z_dot


def trajectory(dt,num_steps,ntraj):
    
#    x = np.empty((num_steps + 1) * ntraj)
#    y = np.empty((num_steps + 1) * ntraj)
#    z = np.empty((num_steps + 1) * ntraj)
    x=np.array([])
    y=np.array([])
    z=np.array([])
    pt=[]
    #for n trajectories
    for j in range(ntraj):
        xs = np.empty(num_steps + 1)
        ys = np.empty(num_steps + 1)
        zs = np.empty(num_steps + 1)
        
        # Set initial values
        xs[0], ys[0], zs[0]= (xx[j], yy[j], zz[j])
        #xs[0], ys[0], zs[0] = (1., -1., 2.05)
        
        
        for i in range(num_steps):
           
            
            """
            EULER SCHEME
            
            dt*x_dot, dt*y_dot, dt*z_dot = lorenz(xs[i], ys[i], zs[i])
            xs[i + 1] = xs[i] + dt*x_dot
            ys[i + 1] = ys[i] + dt*y_dot
            zs[i + 1] = zs[i] + dt*z_dot
            """
            # RK 4 SCHEME
            
            
            
            k1_x, k1_y, k1_z = lorenz(xs[i], ys[i], zs[i], dt)
            k2_x, k2_y, k2_z = lorenz(xs[i]+0.5*k1_x, ys[i]+0.5*k1_y, zs[i]+0.5*k1_z, dt)
            k3_x, k3_y, k3_z = lorenz(xs[i]+0.5*k2_x, ys[i]+0.5*k2_y, zs[i]+0.5*k2_z, dt)
            k4_x, k4_y, k4_z = lorenz(xs[i]+k3_x, ys[i]+k3_y, zs[i]+k3_z, dt)
            xs[i + 1] = xs[i] + ((k1_x+2*k2_x+2*k3_x+k4_x) /6.0)
            ys[i + 1] = ys[i] + ((k1_y+2*k2_y+2*k3_y+k4_y) /6.0)
            zs[i + 1] = zs[i] + ((k1_z+2*k2_z+2*k3_z+k4_z) /6.0)
    
         # Saving values for each trajectory        
         x=np.append(x,xs,axis=0)
         y=np.append(y,ys,axis=0)
         z=np.append(z,zs,axis=0)
    
         pt=np.transpose(np.array([x,y,z]))
    
    return pt
    

#        
#--------------------------------------------------------------------------------------------------------------------       
# forming trajectories
pts=trajectory(0.01,10000,99)

with open('pts.npy', 'wb') as h:
    np.save(h, pts)


