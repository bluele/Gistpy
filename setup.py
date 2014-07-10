#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import dirname, abspath, join, isfile
import platform

cwd = abspath(dirname(__file__))
version = platform.python_version()
install_requires = ['restkit']
if version < '2.7.0':
    install_requires.append('argparse')

def read_file(filename):
    path = join(cwd, filename)
    if isfile(path):
        return open(path).read()


setup(
    name="Gistpy",
    version="0.2.1",
    description="Command line client for gist.",
    long_description=read_file("README.rst"),
    license="MIT",
    author="Jun Kimura",
    author_email="jksmphone@gmail.com",
    url="https://github.com/bluele/Gistpy",
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Topic :: System :: Shells',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    keywords="cli client gist github sourcecode",
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            'gistpy = gistpy:main'
    },
    zip_safe=True)

