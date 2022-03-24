#!/usr/bin/env python3

from distutils.core import setup

setup(name='GaPP',
      version='1.0',
      description='Gaussian Processes in Python',
      author='Marina Seikel',
      author_email='marina@jorrit.de',
      url='http://www.acgc.uct.ac.za/~seikel/GAPP/index.html',
      packages=['gapp', 'gapp.covfunctions'],
     )
