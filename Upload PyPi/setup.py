# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/
from setuptools import setup

setup(name = 'guess_number_game_jenny',
      version = '0.1',
      description = 'Number guessing',
      packages = ['guess_number_game_jenny'],
      zip_safe = False
      )