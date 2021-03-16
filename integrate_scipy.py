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


# Chimie CO2 rapport Saha cinétique p. 16 section 16.4 figure 6
# 5 espèces : O C O2 CO2 CO
#
# 3 reactions :
# O + O  => 02
# C + O2 => C02
# C + O  => CO
# 



def chimie_CO2(t, y):
    k=1.0e8
    return [ -k*y[0]*y[0] - k*y[0]*y[1], 
             -k*y[2]*y[1] - k*y[0]*y[1],
              k*y[0]*y[0] - k*y[1]*y[2],
              k*y[1]*y[2],
              k*y[0]*y[1]]
   
#    return [0,0,0,0,0]
# RK45, RK23, DOP853, Radau, BDF, LSODA

NA=6.0221409e+23

t0=1.0e-8
tf=1.0e-4
Nout=100
#frac0=[NA*0.2,NA*0.2,NA*0.2,NA*0.2,NA*0.2]
#tuple([NA*f for f in frac0])
frac0=[0.2,0.2,0.2,0.2,0.2]

sol = solve_ivp(fun=chimie_CO2, 
                t_span=[t0,tf], 
                y0=frac0, 
                method='Radau',
                t_eval=np.geomspace(t0,tf,Nout),
                first_step=1.0e-9,
                max_step=1.0e-5)




fig, ax = plt.subplots(figsize=(8, 5))#plt.xlim(0, 0.03)

##===================== FONTS ========================= 

plt.rc('font',   size      = 12) # controls default text sizes
plt.rc('axes',   titlesize = 12) # fontsize of the axes title
plt.rc('axes',   labelsize = 12) # fontsize of the x and y labels
plt.rc('xtick',  labelsize = 12) # fontsize of the xtick labels
plt.rc('ytick',  labelsize = 12) # fontsize of the ytick labels
plt.rc('legend', fontsize  = 12) # legend fontsize
plt.rc('figure', titlesize = 12) # fontsize of the figure title

#=== label
ax.set_xlabel('t [ s ]')
ax.set_ylabel('$\chi$ [ V/m ]', color='black')
ax.set_xscale('log')
ax.set_xlim([t0, tf])
ax.set_ylim([0, 1.1])

#ax2 = ax.twinx()
#ax2.set_ylabel('$V$ [ V ]', color = 'red') 
den=sum(sol.y[0:4])

frac=sol.y/den

#frac[0]=sol.y[0]/den
#frac[1]=sol.y[1]/den
#frac[2]=sol.y[2]/den
#frac[3]=sol.y[3]/den
#frac[4]=sol.y[4]/den

sumfrac=sum(frac[0:4])

#=== plots:
#line1,=ax2.plot(1.0e3*x, V, dashes=[2,2],  lw=2, c='red', alpha=1,zorder=2, label='$V_\mathrm{analytic}$')
line1,=ax.plot(sol.t, frac[0], dashes=[3,2],  lw=2, c='black', alpha=1,zorder=2, label='$\chi[{O}]$')
line2,=ax.plot(sol.t, frac[1], dashes=[3,2],  lw=2, c='red', alpha=1,zorder=2, label='$\chi[{C}]$')
line3,=ax.plot(sol.t, frac[2], dashes=[3,2],  lw=2, c='blue', alpha=1,zorder=2, label='$\chi[{O_2}]$')
line4,=ax.plot(sol.t, frac[3], dashes=[3,2],  lw=2, c='orange', alpha=1,zorder=2, label='$\chi[{CO_2}]$')
line5,=ax.plot(sol.t, frac[4], dashes=[3,2],  lw=2, c='green', alpha=1,zorder=2, label='$\chi[{CO}]$')
line6,=ax.plot(sol.t, sumfrac[:], dashes=[3,2],  lw=2, c='grey', alpha=1,zorder=2, label='$\chi[{CO}]$')

plt.legend(handles=[line1,line2,line3,line4,line5,line6],loc='upper center', frameon=False,
          bbox_to_anchor=(0.5, 1.2), shadow=False, ncol=5)





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