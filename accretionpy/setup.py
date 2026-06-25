from setuptools import setup, Extension
import numpy
from Cython.Build import cythonize


def get_extensions():
    extensions = []
    extensions = cythonize(
        [
            Extension(
                include_dirs=[numpy.get_include()],
            )
        ]
    )
    return extensions


setup(
    ext_modules=get_extensions(),
)
