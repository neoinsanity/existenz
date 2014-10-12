"""The setuptools setup file."""
from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()

setup(
    name='existenz',
    version='0.0.3a',
    author='Raul Gonzalez',
    author_email='mindbender@gmail.com',
    url='https://github.com/neoinsanity/existenz',
    license='Apache License 2.0',
    description='an existing individual',
    long_description=long_description,
    packages=['existenz', ],
    install_requires=[
        'cognate==0.0.1',
        'decorator==3.4.0',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Life',
        'Topic :: Software Development',
    ]
)
