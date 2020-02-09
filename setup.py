from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
  ext_modules=cythonize("samplerbox_audio.pyx", build_dir="build"),
  compiler_directives={"language_level": "3"},
  include_dirs=[numpy.get_include()],
)
