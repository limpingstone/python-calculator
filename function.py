#!/usr/bin/env python3
#
# function.py - By Steven Chen Hao Nyeo 
# The collection of function objects for the python calculator
# Last Modified: December 24, 2018

from operand import *
import math

class Function(Variable): 
	def __init__ (self, operand):
		self.operand = operand
	
class Polynomial(Function):
	def __init__ (self, operand, power):  
		super().__init__ (operand)
		self.power = power
		
	def __str__ (self):
		return "(" + str(self.operand) + "^" + str(self.power) + ")"
		
	def get_value(self, x): 
		return self.operand.get_value(x) ** self.power
		
	def derivative(self):
		return BinaryOp(BinaryOp(Number(self.power), '*', Polynomial(self.operand, self.power - 1)), '*', self.operand.derivative())
	
	def equals(self, operand):
		if isinstance(operand, Variable):
			return str(self) == str(operand)
		return False
	
class Sin(Function):
	def __init__ (self, operand):  
		super().__init__ (operand)
		
	def __str__ (self):
		return "sin[" + str(self.operand) + "]"
		
	def get_value(self, x): 
		return math.sin(self.operand.get_value(x))
		
	def derivative(self):
		return BinaryOp(Cos(self.operand), "*", self.operand.derivative())
	
	def equals(self, operand):
		if isinstance(operand, Variable):
			return str(self) == str(operand)
		return False
	
class Cos(Function):
	def __init__ (self, operand):  
		super().__init__ (operand)
		
	def __str__ (self):
		return "cos[" + str(self.operand) + "]"
		
	def get_value(self, x): 
		return math.cos(self.operand.get_value(x))
		
	def derivative(self):
		return BinaryOp(BinaryOp(Number(-1), '*', Sin(self.operand)), '*', self.operand.derivative())
	
	def equals(self, operand):
		if isinstance(operand, Variable):
			return str(self) == str(operand)
		return False
	
class Exp(Function):
	def __init__ (self, operand):  
		super().__init__ (operand)
		
	def __str__ (self):
		return "exp[" + str(self.operand) + "]"
		
	def get_value(self, x): 
		return math.exp(self.operand.get_value(x))
		
	def derivative(self):
		return BinaryOp(Exp(self.operand), '*', self.operand.derivative())
	
	def equals(self, operand):
		if isinstance(operand, Variable):
			return str(self) == str(operand)
		return False