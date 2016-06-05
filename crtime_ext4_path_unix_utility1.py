#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
.. module:: crtime_ext4_path_unix_utility1
   :platform: Unix
   :synopsis: Class that provides creeation time information for a file on Unix platform on ext4 filesystem.

.. moduleauthor:: František Brožka

Class that provides creeation time information for a file on Unix platform on ext4 filesystem.

"""

u"""
    Copyright 2016 František Brožka

    This file is part of RecordDirInfo.

    RecordDirInfo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RecordDirInfo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with RecordDirInfo.  If not, see <http://www.gnu.org/licenses/>.

"""

import subprocess

import crtime_ext4_path

class CrtimeExt4PathUnixUtility1(crtime_ext4_path.CrtimeExt4Path):
	
	def __init__(self):
		try:
			self.CLIUtility = "getcrtime"
			subprocess.check_output(["which", self.CLIUtility], stderr=subprocess.PIPE)
		except subprocess.CalledProcessError:
			self.CLIUtility = "ffgetcrtime"
			subprocess.check_output(["which", self.CLIUtility], stderr=subprocess.PIPE)
	
	def getCreationTime(self, path):
		return subprocess.check_output([self.CLIUtility, path], stderr=subprocess.PIPE).rstrip('\r\n')
