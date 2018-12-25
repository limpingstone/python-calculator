#!/usr/bin/env python3
#
# operator.py - By Steven Chen Hao Nyeo 
# The four operators for computing operations 
# Last Modified: December 24, 2018

from enum import Enum

class Operator(Enum):
	PLUS('+')
	SUB('-')
	MULT('*')
	DIV('/')
	MOD('%')
	
	def __init__ (self, op):
		self.op = op
	
	def __str__ (self):
		return op