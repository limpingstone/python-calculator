#!/usr/bin/env python3
#
# operand.py - By Steven Chen Hao Nyeo 
# The basic operands for the calculator 
# Created: December 24, 2018

from abc import ABC, abstractmethod
from enum import Enum

class Operator(Enum):
	PLUS = '+'
	SUB = '-'
	MULT = '*'
	DIV = '/'

# The collection of all operands 
class Operand(ABC): 
	pass
		
# The class for generating number objects 
class Number(Operand): 
	def __init__ (self, value):  
		self.value = value
		
	def __str__ (self):
		return str(self.value)
		
	def get_expression(self): 
		return Number(self.value)
		
	def get_value(self, x): 
		return self.value
		
	def derivative(self):
		return Number(0)
	
	def equals(self, operand):
		if (isinstance(operand, Number)):
			return operand.get_value() == self.get_value()
		return False

# The class for generating variable objects 
class Variable(Operand): 
	def __str__ (self):
		return "x"
		
	def get_expression(self): 
		raise ValueError("Action not supported")
	
	def get_value(self, x): 
		return x
		
	def derivative(self):
		return Number(1)
	
	def equals(self, operand):
		return isinstance(operand, Variable)
	
# The class for generating binary operand objects 
class BinaryOp(Variable): 
	def __init__ (self, left_input, operator, right_input):
		self.left_operand = left_input
		self.operator = operator
		self.right_operand = right_input
	
	def __str__ (self):
		return "(" + str(self.left_operand) + str(self.operator) + str(self.right_operand) + ")"
	
	# Plugs in a number value for the binary operand
	def get_value(self, x): 
		if (self.operator == Operator.PLUS.value):
			return int(self.left_operand.get_value(x)) + int(self.right_operand.get_value(x))
		elif (self.operator == Operator.SUB.value):
			return int(self.left_operand.get_value(x)) - int(self.right_operand.get_value(x))
		elif (self.operator == Operator.MULT.value):
			return int(self.left_operand.get_value(x)) * int(self.right_operand.get_value(x))
		elif (self.operator == Operator.DIV.value):
			return int(self.left_operand.get_value(x)) / int(self.right_operand.get_value(x))
	
	# Takes the derivative of the binary operand - chain rule is implemented
	def derivative(self):
		if (self.operator == Operator.PLUS.value):
			return BinaryOp(self.left_operand.derivative(), '+', self.right_operand.derivative())
		elif (self.operator == Operator.SUB.value):
			return BinaryOp(self.left_operand.derivative(), '-', self.right_operand.derivative())
		elif (self.operator == Operator.MULT.value):
			return BinaryOp(
				BinaryOp(self.left_operand.derivative(), '*', self.right_operand), '+',
				BinaryOp(self.left_operand, '*', self.right_operand.derivative()))
		elif (self.operator == Operator.DIV.value):
			return BinaryOp(BinaryOp(
				BinaryOp(self.left_operand.derivative(), '*', self.right_operand), '-',
				BinaryOp(self.left_operand, '*', self.right_operand.derivative())), '/', 
				BinaryOp(self.right_operand, '*', self.right_operand))
	
	def equals(self, operand):
		if isinstance(operand, Variable):
			return str(self) == str(operand)
		return False
			