"""this code uses user input and Eq 1 from Kummer (2025) to determine what
 kind of BBH accretion will occur in a given system."""


mstari = float(input("Enter the mass of the star (in Msun): ")) #convert to kg later
mbh1i = float(input("Enter the mass of BH 1 (in Msun): ")) #convert to kg later
mbh2i = float(input("Enter the mass of BH 2 (in Msun): ")) #convert to kg later
aouti = float(input("Enter distance between star and COM of BBH (in Rsun): ")) #convert to meters later
eout = float(input("Enter the eccentricity of the BBH and star orbit: "))
aini = float(input("Enter the distance between the BHs (in Rsun):" )) #convert to meters later
ein = float(input("Enter the eccentricity of the BBH orbit: "))

qout = mstari / (mbh1i + mbh2i)

mstar = mstari * 1.989*10**30
mbh1 = mbh1i * 1.989*10**30
mbh2 = mbh2i * 1.989*10**30
aout = aouti * 6.957*10**8
ain = aini * 6.957*10**8

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

