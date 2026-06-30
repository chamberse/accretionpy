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
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

def read_file():    
    """
    Read in .txt file and read in user input to initial_conditions dictionary. 
    Strip the white space from the file and convert the inputs to floats.
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
    """
    Import variables and their names from the dictionary.

    Since ain is optional, add the None option to it.
    """
    mstar = initial_conditions['mstar']
    mbh1 = initial_conditions['mbh1']
    mbh2 = initial_conditions['mbh2']
    aout = initial_conditions['aout']
    eout = initial_conditions['eout']
    ein = initial_conditions['ein']
    rstar = initial_conditions['rstar']

    #allows in to be 0 or None in text file
    ain = initial_conditions.get('ain', None) 

    return mstar, mbh1, mbh2, aout, eout, ain, ein, rstar

def calculate_rmin(mstar, mbh1, mbh2, aout, eout):
    """
    Use qout, eout, and aout to calculate the minimum distance at which the 
    accreted mass can approach the binary.

    If qout is less than 1, the inverse does not need to be taken. 
    """

    qout = mstar / (mbh1 + mbh2)    

    if qout < 1:
        rmin = 0.425 * aout * (1 - eout)*((qout)*(1+qout))
    else:
        rmin = 0.425 * aout * (1 - eout)*((1/qout)*(1+1/qout))

    return qout, rmin

def calculate_aapo(ain, ein, rmin):
    """
    Use ain and ein to calculate the apocenter distance of the binary. 
    If no ain value give by the user, ain_crit = rmin. 
    """
    if ain is None or ain == 0:
        aapo = None
        ain_crit = rmin
    else:
        aapo = ain * (1 + ein)
        ain_crit = rmin

    return aapo, ain_crit

def determine_accretion_type(aapo, rmin, ain_crit):
    """
    Determine the type of accretion that will be produced by the initial conditions given by the user.
    Accretion will either be ballistic or circumbinary disk. 
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

def interactive_plot(rstar, aout, rmin, aapo, ain_crit):
    """
    create a plot that allows the user to visualize what is going on in the system and how the mass is flowing.

    """

    fig = plt.figure(figsize = (10,6))
    ax = fig.add_subplot(111, projection = '3d')
    theta = np.linspace(0, 2*np.pi, 200)
    #plot star using aout. assume aout is the distance from the stellar core to bbh com
    star_x = -aout
    star_y = 0
    star_z = 0

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = rstar*np.outer(np.cos(u),np.sin(v)) + star_x
    y = rstar*np.outer(np.sin(u),np.sin(v)) + star_y
    z = rstar*np.outer(np.ones(np.size(u)),np.cos(v)) + star_z

    ax.plot_surface(x,y,z,color='orange',alpha=1)
    #mstar = Circle((-200, 200), 90, fill=False, edgecolor='orange', label='mstar')
    #ax.add_patch(mstar)
    #plot rmin mass stream
    x_rmin = rmin * np.cos(theta)
    y_rmin = rmin * np.sin(theta)
    z_rmin = np.full_like(theta, -10)
    ax.plot3D(x_rmin, y_rmin, z_rmin, 'k--', linewidth=1, label=f'r_min ({rmin:.1f} Rsun)')

    # start at star surface
    x0 = star_x + rstar
    y0 = rstar - 150
    z0 = 0

    # end at left side of rmin circle
    x1 = -rmin
    y1 = 0
    z1 = -10

    dx = x1 - x0
    dy = y1 - y0
    dz = z1 - z0

    ax.quiver(
        x0, y0, z0,
        dx, dy, dz,
        color='magenta',
        linewidth=3,
        arrow_length_ratio=0.08
    )

    if aapo is not None:
        #plot max physical reach of binary
        x_aapo = aapo * np.cos(theta)
        y_aapo = aapo * np.sin(theta)
        z_aapo = np.full_like(theta, -10)
        ax.scatter(0, 0, 0, s=100, color='black', label='mbh1')
        ax.scatter(aapo, 0, 0, s=100, color='black', label='mbh2')
        ax.plot3D([0, aapo], [0, 0], [0,0], 'k-', linewidth=1, zorder=1, label='ain, ein')
        #ax.plot(0, 0, 'o', markersize=2, label = 'mbh1')
        #ax.plot(aapo, 0, 'o', markersize=2, zorder=5, label = 'mbh2')
        

        if aapo > rmin:
            line_color = 'green'
            plot_title = 'Accretion State: Ballistic Accretion (a_apo > r_min)'
            #ax.fill_between(theta, rmin, aapo, color='green', alpha=0.1, label='Ballistic Collision Zone')
        else:
            line_color = 'blue'
            plot_title = "Accretion State: Circumbinary Disk (a_apo <= r_min)"
        
        #radius = aapo
        ax.plot3D(x_aapo, y_aapo, z_aapo, '-', color=line_color, linewidth=1, label=f'a_apo ({aapo:.1f} Rsun)')
        #ax.add_patch(p)
        #art3d.pathpatch_2d_to_3d(p, z=-2, zdir='z')

    else:
        #if no ain is given, display plot for ain_crit
        x_crit = ain_crit * np.cos(theta)
        y_crit = ain_crit * np.sin(theta)
        z_crit = np.full_like(theta, -10)
        ax.plot3D(0, 0, -10,'o', markersize=2, label = 'mbh1')
        ax.plot3D(ain_crit, 0, -10, 'o', markersize=2, zorder=5, label = 'mbh2')
        ax.plot3D([0, ain_crit], [0, 0], [-10, -10], 'k-', linewidth=1, zorder=1, label='ain, ein')
        ax.plot3D(x_crit, y_crit, z_crit, 'g-', linewidth=1, label=f'Min separation for BA ({ain_crit:.1f} Rsun)')
        plot_title = "ain_crit"

    

    #plot settings
    #ax.set_aspect('equal')
    ax.set_box_aspect([1,1,1])
    xmin = -aout - rstar
    xmax = max(rmin, aapo if aapo is not None else ain_crit)

    pad = 0.1*(xmax-xmin)

    xmin -= pad
    xmax += pad

    center = (xmin+xmax)/2
    radius = (xmax-xmin)/2

    ax.set_xlim(center-radius, center+radius)
    ax.set_ylim(-radius, radius)
    ax.set_zlim(-radius, radius)


    ax.set_title(plot_title, fontsize=11, fontweight='bold', pad=15)
    ax.set_xlabel(r'Distance ($R_{\odot}$)')
    ax.set_ylabel(r'Distance ($R_{\odot}$)')
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend(bbox_to_anchor=(0.1, 1))
    #plt.tight_layout()
    #plt.margins(0.2)
    plt.show()




def main():
    initial_conditions = read_file()
    mstar, mbh1, mbh2, aout, eout, ain, ein, rstar = read_variables(initial_conditions)
    qout, rmin = calculate_rmin(mstar, mbh1, mbh2, aout, eout)
    aapo, ain_crit = calculate_aapo(ain, ein, rmin)
    output = determine_accretion_type(aapo, rmin, ain_crit)
    interactive_plot(rstar, aout, rmin, aapo, ain_crit)

    return output


if __name__ == "__main__":
    main()
