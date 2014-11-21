!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Martijn van Leeuwen'

# ==============================================================================
##
##  pi-setup.py
##
##  Details:    Script to configure and install the RPI installation for use
##              in the VOC Electronics presentations and workshops.
##
##  Target system:  Raspberry Pi
##
##  Descrption:
##
##    * PIBrella support
##    * Python2 and Python3
##    * PIP
##    * Bootup in graphical mode 
##    * Scratch
##    * Up to date OS.
##
# ==============================================================================
import subprocess
import re
import sys
import time
import datetime
import os
