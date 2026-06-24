import os

__version__ = "1.0.0"

# set Python env variable to keep track of example data dir
accretionpy_dir = os.path.dirname(__file__)
DATADIR = os.path.join(accretionpy_dir, "accretionpy/")
