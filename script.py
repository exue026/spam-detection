#!/usr/bin/env python

import os
import sys

os.chdir('raw_data')
files = os.listdir(os.getcwd())
for file in files:
    if os.path.isdir(file):
        os.chdir(file)
        counter = 1
        for file in os.listdir(os.getcwd()):
            os.rename(file, str(counter) + '.txt')
            counter += 1
        os.chdir('..')