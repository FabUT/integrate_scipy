# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:09:42 2021

@author: ftholin
"""


from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl



def exponential_decay(t, y): return -0.5 * y


def chimie_CO2(t, y):
    k=1.0e8
    return [ -k*y[0]**2+k*y[0]*y[1] , 
             -k*y[2]*y[1]-k*y[0]*y[1],
             k*y[0]**2-k*y[1]*y[2],
             k*y[1]*y[2],
             k*y[0]*y[1]
             ]

# RK45, RK23, DOP853, Radau, BDF, LSODA

t0=1.0e-5
tf=1.0e-3
Nout=30

sol = solve_ivp(fun=chimie_CO2, 
                t_span=[t0,tf], 
                y0=[0.2,0.2,0.2,0.2,0.2], 
                method='LSODA',
                t_eval=np.geomspace(t0,tf,Nout) )




#t_eval=np.geompace(t0,tf,Nout)
#t_eval=np.linspace(t0,tf,Nout)
#t_eval=np.logspace(t0, tf, Nout, endpoint=True, base=10.0)
#print(sol.t)

#[ 0.          0.11487653  1.26364188  3.06061781  4.81611105  6.57445806
#  8.33328988 10.        ]

#print(sol.y)


#[[2.         1.88836035 1.06327177 0.43319312 0.18017253 0.07483045
#  0.03107158 0.01350781]
# [4.         3.7767207  2.12654355 0.86638624 0.36034507 0.14966091
#  0.06214316 0.02701561]
# [8.         7.5534414  4.25308709 1.73277247 0.72069014 0.29932181
#  0.12428631 0.05403123]]