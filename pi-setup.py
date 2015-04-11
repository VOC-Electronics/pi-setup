#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Martijn van Leeuwen'

# ==============================================================================
#
# pi-setup.py
#
# Details:    Script to configure and install the RPI installation for use
#              in the VOC Electronics presentations and workshops.
#
# Target system:  Raspberry Pi
#
# Descrption:
#
#    * PIBrella support
#    * Python2 and Python3
#    * PIP
#    * Bootup in graphical mode
#    * Scratch
#    * Up to date OS.
# Todo:
#
# ==============================================================================
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Import Libraries

import subprocess
import re
import time
import ConfigParser
import os
import platform
# import sys
# import datetime
#


# ===========================================================================
# Settings, configs, etc
# ===========================================================================
# Set debug output on/off
DEBUG=True
configfile = "./pisetup.cfg"
datestamp = time.strftime("%Y-%m-%d")
timestamp = time.strftime("%H:%M:%S")
monthstamp = time.strftime("%m")
yearstamp = time.strftime("%Y")


class SetupSystem(object):
  FORCE = False
  # ===========================================================================
  # Funcion list:
  # ===========================================================================
  # 
  # Done: 
  # init (Initialises the Class)
  # getPiRevision (Get the Raspberry Pi Revision number of the board)
  # disk_report (Get disk usage)
  # execCmd (Executes the supplied external program and returns the output.)
  #
  # ToDo:
  # CollectApps (Collects the list of installed applications.)
  # CreateMissing (Creates a list of missing apps based on the installed app
  #                list and the supplied apps list from the config file.)
  # InstallMissing (Installs the apps that are showing up in the missinglist.)
  # 
  # ===========================================================================
  def __init__(self, sysname, force):
    """


    :rtype : object
    :param parent:
    """
    self.systemname = sysname
    appsList = []
    installapps = []
    bold = "\033[1m"
    reset = "\033[0;0m"
    self.pirev = self.getPiRevision()

    if force:
      self.FORCE = True
    """ Check if the config file exists"""
    if not os.path.isfile(configfile):
      print " " + bold + "pi-setup.py." + reset
      print " " + bold + "Unable to locate" + configfile + "." + reset
      exit(1)
    else:
      print " " + bold + "pi-setup.py." + reset
      print " " + bold + "Loading" + configfile + "." + reset
      print " " + bold + "Pi board version:" + str(self.pirev) + "." + reset
      self.config = ConfigParser.ConfigParser()
      self.config.read(configfile)
      self.logdir = self.config.get('Main', 'LOGDIR')
      self.pid_file = self.config.get('Main', 'PID')
      self.NetSet = self.config.get('Main', 'IP')

  # noinspection PyPep8Naming
  @staticmethod
  def getPiRevision():
    """Gets the version number of the Raspberry Pi board"""
    # Example of proc info of a Raspberry Pi B v2 (4 Cores)
    # Hardware	: BCM2709
    # Revision	: a01041
    # Serial		: 0000000037f1eaa1
    # Revision list available at: http://elinux.org/RPi_HardwareHistory#Board_Revision_History
    if DEBUG:
      print "Start lookup Pi Revision of the Raspberry Pi we're running on."

    try:
      with open('/proc/cpuinfo', 'r') as infile:
        for line in infile:
          # Match a line of the form "Revision : 0002" while ignoring extra
          # info in front of the revsion (like 1000 when the Pi was over-volted).
          match = re.match('Revision\s+:\s+.*(\w{4})$', line)
          match2 = re.match('Revision\s+:\s+.*(\w{6})$', line)
          if DEBUG:
            print "Matched revision: " + str(match)
          if match and match.group(1) in ['0000', '0002', '0003']:
            # Return revision 1 if revision ends with 0000, 0002 or 0003.
            return 1
          elif match:
            # Assume revision 2 if revision ends with any other 4 chars.
            return 2
        # Couldn't find the revision, assume revision 0 like older code for compatibility.
        print "Unable to find a revision match, using revision 0"
        return 0
    except:
      print "Unable to open /proc/cpuinfo."
      exit(15)
      return 0

  @property
  # noinspection PyPep8Naming
  def disk_report(self):
    """Checks the available disk space in human readable output."""
    if DEBUG:
      print "Collecting available diskspace."

    p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

  # noinspection PyPep8Naming
  def execCmd(self, cmd, params):
    """Executes the supplied command with inherited parameters"""
    if DEBUG:
      print "Executing shell command: " + cmd
    p = subprocess.Popen(cmd, params, shell=true, stdout=subprocess.PIPE)
    return p.stdout.readlines()

  # noinspection PyPep8Naming
  def CollectApps(self):
    """Collects the list of installed applications"""
    if DEBUG:
      print "[*] Start Collecting the list of applications currently installed"

  # noinspection PyPep8Naming
  def CreateMissing(self):
    """Creates a list of missing apps based on the installed app list and the supplied apps list from the config file"""
    if DEBUG:
      print "[*] Buidling file list of missing applications."


if __name__ == '__main__':
  if DEBUG:
    print "[*] Firing up the main call to the main class."
    
  app = SetupSystem("test", False)
