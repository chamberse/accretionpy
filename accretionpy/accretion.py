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
import matplotlib.pyplot as plt

def read_file():    
    """
    Docstring here
    """
    initial_conditions = {}

    with open('initial_conditions.txt', 'r') as file:
        for line in file:
            #line = [int(line.strip()) for line in file if line.strip()]
            if not line.strip() or line.startswith("#"):
                continue
            if '=' in line:
                # Split at the first '=' sign
                key, value = line.split("=", 1)
        
            # Strip whitespace and save to dictionary
            initial_conditions[key.strip()] = float(value.strip())

    return initial_conditions

def read_variables(initial_conditions):
    mstar = initial_conditions['mstar']
    mbh1 = initial_conditions['mbh1']
    mbh2 = initial_conditions['mbh2']
    aout = initial_conditions['aout']
    eout = initial_conditions['eout']
    ein = initial_conditions['ein']

    #allows in to be 0 or None in text file
    ain = initial_conditions.get('ain', None) 

    return mstar, mbh1, mbh2, aout, eout, ain, ein

def calculate_rmin(mstar, mbh1, mbh2, aout, eout):
    """
    Docstring here
    """

    qout = mstar / (mbh1 + mbh2)    

    if qout < 1:
        rmin = 0.425 * aout * (1 - eout)*((qout)*(1+qout))
    else:
        rmin = 0.425 * aout * (1 - eout)*((1/qout)*(1+1/qout))

    return qout, rmin

def calculate_aapo(ain, ein, rmin):
    """
    Docstring here
    """
    if ain is None or ain == 0:
        aapo = None
        ain_crit = rmin + 1
    else:
        aapo = ain * (1 + ein)
        ain_crit = rmin + 1

    return aapo, ain_crit

def determine_accretion_type(aapo, rmin, ain_crit):
    """
    
    """
    if aapo is None:
        print(f"The minimum inner binary separation (ain) needed to achieve ballistic accretion is {ain_crit:.2f} Rsun.")
        return

    if aapo > rmin:
        print("Ballistic accretion will occur in this system.")
        print(f"The minimum separation to acheive ballistic accretion is {ain_crit:.2f} Rsun.")
    else:
        print("A circumbinary disk will form in this system.")
        print(f"The minimum separation to acheive ballistic accretion is {ain_crit:.2f} Rsun.")

def interactive_plot():
    """
    
    """

def main():
    initial_conditions = read_file()
    mstar, mbh1, mbh2, aout, eout, ain, ein = read_variables(initial_conditions)
    qout, rmin = calculate_rmin(mstar, mbh1, mbh2, aout, eout)
    aapo, ain_crit = calculate_aapo(ain, ein, rmin)
    output = determine_accretion_type(aapo, rmin, ain_crit)

    return output


if __name__ == "__main__":
    main()


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
#add variable names in example initial conditions file.
#treat masses as objects and make code class based?
#make interactive visualization with sliders



