"""
This code takes in user input in the form of an 'initial_conditions.txt' document and 
uses Eq 1 from Kummer et al. (2025):
    https://www.aanda.org/articles/aa/full_html/2025/01/aa52108-24/aa52108-24.html
to determine if a BBH in a three-body system will exhibit 'ballistic' accretion (BA) or 
accretion through a circumbinary disk (CBD).

Input should consist of an 'initial_conditions.txt' file with variables listed vertically, 
located in the same directory as this file. 

The output is comprised of a given rmin value that is the minimum distance (in Rsun) at which 
the mass stream can approach the accreting binary. 
"""

import numpy as np

with open('initial_conditions.txt', 'r') as file:
    variables = [int(line.strip()) for line in file if line.strip()]
    #mstar, mbh1, mbh2, aout, eout, ain, ein = [int(i) for i in line]
    #print(mstar, mbh1, mbh2, aout, eout, ain, ein)

mstar = variables[0]
mbh1 = variables[1]
mbh2 = variables[2]
aout = variables[3]
eout = variables[4]
ain = variables[5]
ein = variables[6]

qout = mstar / (mbh1 + mbh2)

if qout < 1:
    rmin = 0.425 * aout * (1 - eout)*((qout)*(1+qout))
else:
    rmin = 0.425 * aout * (1 - eout)*((1/qout)*(1+1/qout))

aapo = ain * (1 + ein)

if aapo > rmin:
    print(f"{aapo:.2f} Rsun is greater than {rmin:.2f} Rsun")
    print("Ballistic accretion will occur in this system.")

if rmin > aapo:
    print(f"{aapo:.2f} Rsun is less than {rmin:.2f} Rsun")
    print("A circumbinary disk will form in this system.")

#acirc = (aout*(0.5 - 0.0986*np.log(qout))**4)*(1+qout)
#print(acirc)
#acav = 1.6*acirc
#print(acav)
##since acav / abin = 1.68, solve for abin
#
#abin = acav / 1.68
#print(abin)
#
#if abin != rmin:
#    print(f"binary sparations not equal: {abin:.2f} Rsun and {rmin} Rsun")
#



# eventually add plot with projected accretion path
# use more robust calculations with modules and functions
# calculate the critical value for BA accretion

#given that aapo has to be greater than rmin, solve for critical ain based on this assumption.
#add variable names in example initial conditions file.
#treat masses as objects and make code class based?
#make interactive visualization with sliders



