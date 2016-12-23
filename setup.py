from distutils.core import setup

from setuptools import find_packages

requirements = ["discord.py==0.16.0", "click==6.6", "keyring==10.1"]

setup(name='term-shitter',
      version='0.0',
      description='Posts shit (gifs, images) from imgur to some chat services.',
      author='Karl Johan Krantz',
      author_email='schwomp@gmail.com',
      packages=find_packages(exclude="test"),
      install_requires=requirements,
      entry_points={
          'console_scripts': ['term-shitter = term_shitter.__main__:main']
      }
)