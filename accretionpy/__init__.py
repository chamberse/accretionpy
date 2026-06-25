import os

__version__ = "1.0.0"

# set Python env variable to keep track of example data dir
accretionpy_dir = os.path.dirname(__file__)
DATADIR = os.path.join(accretionpy_dir, "example_data/")

# Detect a valid CUDA environment
try:
    import pycuda.driver as cuda
    import pycuda.autoinit
    from pycuda.compiler import SourceModule

    cuda_ext = True
except:
    cuda_ext = False

try:
    from . import _kepler

    cext = True
except ImportError:
    cext = False

