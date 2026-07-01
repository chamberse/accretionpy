import numpy as np

qout = 13/(60+60)

acirc = (838 * (0.5 - 0.0986 * np.log(qout)) ** 4) * (1 + qout)
print(f"acirc = {acirc:.2f} Rsun")
acav = 1.6 * acirc
print(f"acav = {acav:.2f} Rsun")
#since acav / abin = 1.68, solve for abin
abin = acav / 1.68
print(f"abin = {abin:.2f} Rsun")
