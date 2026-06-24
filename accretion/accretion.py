"""this code uses user input and Eq 1 from Kummer (2025) to determine what
 kind of BBH accretion will occur in a given system."""

import numpy as np


with open('initial_conditions.txt', 'r') as file:
    mstar, mbh1, mbh2, aout, eout, ain, ein = file.read().splitlines()

qout = mstar / (mbh1 + mbh2)

#unit conversions
#mstar = mstari * 1.989*10**30
#mbh1 = mbh1i * 1.989*10**30
#mbh2 = mbh2i * 1.989*10**30
#aout = aouti * 6.957*10**8
#ain = aini * 6.957*10**8

rmin = 0.425 * aout * (1 - eout)*((1/qout)*(1+1/qout))

aapo = ain * (1 + ein)

if aapo > rmin:
    print(f"{aapo:e} is greater than {rmin:e}")
    print("Ballistic accretion will occur in this system.")

if rmin > aapo:
    print(f"{aapo:e} is less than {rmin:e}")
    print("A circumbinary disk will form in this system.")
else:
    print("Error")

# eventually add plot with projected accretion path
# use more robust calculations with modules and functions

