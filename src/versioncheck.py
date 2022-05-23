#!/bin/env python3 

import os

import git



SCRIPTDIR   = os.path.dirname(os.path.realpath(__file__))

REPODIR     ="REPO"
FARMINGDIR  ="farming"

filename_ignored = "ignore"
filename_locked  = "locked"

abs_FARMINGDIR  = os.path.join(SCRIPTDIR , ".." , FARMINGDIR ) 
abs_ignored     = os.path.join(SCRIPTDIR , ".." , FARMINGDIR , filename_ignored)
abs_locked      = os.path.join(SCRIPTDIR , ".." , FARMINGDIR , filename_locked)

ignored = []
locked  = []


def getVersFromPKGBUILD (pkgbuild):
  with open(pkgbuild, 'r') as _PKGBUILD:
    for _line in _PKGBUILD.readlines():
      if _line.upper().startswith("PKGVER") : 
        return _line.split("=")[1].strip(" ").strip("\n")

# Import ignored and locked lists
with open(abs_ignored, 'r') as _file:
  for _line in _file.readlines():
    value = _line.split("#")[0].strip("\n").strip(" ")
    if len(value) > 0 : 
        ignored.append(value)

with open(abs_locked, 'r') as _file:
  for _line in _file.readlines():
    value = _line.split("#")[0].strip("\n")
    if len(value) > 0 : 
        locked.append(value)

# Check for updates in packages
with os.scandir(abs_FARMINGDIR) as farmdir:
  for entry in farmdir:
    if entry.is_dir() and entry.name not in ignored: 
      packagerepo = os.path.realpath(os.path.join(abs_FARMINGDIR , entry.name))
      curvers = getVersFromPKGBUILD(os.path.join(packagerepo , "PKGBUILD"))
      print (curvers)

      # Updates on package-repo need to be done automatically. We just check if the version in PKGBUILD matches the one in the repo










