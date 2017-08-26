#!/usr/bin/env python

"""
Poynt
-----
The official Poynt Python SDK. Connect to the Poynt API, get/create business
information, and send cloud messages to your terminal app.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('poynt/version.py').read())

setup(
    name='poynt',
    version=__version__,
    description='The official Poynt Python SDK.',
    long_description=__doc__,
    author='Charles Feng',
    author_email='c@poynt.com',
    url='https://poynt.com/developers',
    license='MIT',
    install_requires=['requests', 'cryptography'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
