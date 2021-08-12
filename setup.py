import os
from setuptools import setup

DIR=os.path.dirname(__file__)

setup(
    name='film_info',
    version='1.1.1',
    description='finds any film on imdb.com and returns some info about it',
    long_description=open(os.path.join(DIR, 'README.md')).read(),
    author='8harifi',
    author_email='8harifi@gmail.com',
    url='https://github.com/8harifi/film_info',
    py_modules=['film_info'],
    entry_points={
        'console_scripts':
        ['film_info=film_info:main'],
    })
