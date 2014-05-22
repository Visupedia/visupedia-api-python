import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='visupedia',
    version='0.0.1',
    description='Official Visupedia API library client for python',
    author='Gaël Gillard',
    author_email='dev@visupedia.net',
    url='http://visupedia.net',
    license='MIT',
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'visupedia'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
