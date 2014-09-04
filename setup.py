"""Distribution for vimdoc."""
from distutils.core import setup

setup(
    name='vimdoc',
    version='0.4.1',
    description='Generate vim helpfiles',
    author='Nate Soares',
    author_email='nate@so8r.es',
    packages=[
        'vimdoc',
    ],
    scripts=[
        'scripts/vimdoc',
    ])
