.. accretionpy documentation master file, created by
   sphinx-quickstart on Wed Jun 24 11:15:28 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``accretionpy`` Documentation
==============================

``accretionpy`` allows users to determine the initial conditions that result in different types of accretion
around a binary black hole.
This package is based off of equation 1 in
`Kummer et al. (2025) <https://www.aanda.org/articles/aa/full_html/2025/01/aa52108-24/aa52108-24.html>`_

| The current types of accretion in this package are:
| 1. Ballistic accretion (common envelope type)
| 2. Circumbinary disk (CBD) accretion

Getting Started
+++++++++++++++++++

To get started using ``accretionpy``, either
clone the repository from `GitHub <https://github.com/chamberse/accretionpy>`_:

``$ git clone https://github.com/chamberse/accretionpy``

or pip install it:

``$ pip install accretionpy``

Open the ``initial_conditions.txt`` file in the text editor of your choice and add your inputs for each variable. 
Variable definitions can be found below as well as a visual in :ref:`Figure 1 <figure1>`.

To run the package, run:

``$ python /accretionpy/accretionpy/accretion.py``

accretionpy requires a set of already determined values for a 3-body system:

| **mstar** is the mass of the star in solar masses.

| **mbh1** and **mbh2** are the masses of the respective black holes in the system in solar masses. 
    
| **NOTE: The current version of accretionpy only supports equal mass black holes, so mbh1 should equal mbh2.**

| **aout** is the distance between the center of mass of the star and the center of mass of the BBH in solar radii.         
   accretionpy assumes this value is set so that the radius of the star is equal to its Roche Lobe.

| **eout** is the eccentricity of the star-BBH orbit.

| **ain** is an optional input that describes the separation between the black holes in solar radii. If this is not entered, the critical
   separation to achieve ballistic accretion will be calculated and displayed. 

| **ein** is the eccentricity of the BBH orbit.

.. figure:: /_static/figure1.png
   :alt: Visual depiction of each system variable.
   :align: center
   :width: 80%
   :name: figure1

   Figure 1: Visualization of the definition of each variable used in the accretionpy calculations.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and Tables
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

