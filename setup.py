from setuptools import setup, find_packages

# Bare minimum setup to install and run it without using Docker container.
setup(name='notebook',
      description='hjkim assignment for Monolith AI',
      version='0.0.1',
      package_dir={'': '.'},
      packages=find_packages('.')
      )
