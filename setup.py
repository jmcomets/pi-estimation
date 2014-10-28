from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name='Estimate Pi by the Monte Carlo method.',
      ext_modules=cythonize('estimate.pyx', include_path=[numpy.get_include()]))
