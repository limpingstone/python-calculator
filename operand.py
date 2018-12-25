#!/usr/bin/env python3
#
# operand.py - By Steven Chen Hao Nyeo 
# The basic operands for the calculator 
# Last Modified: December 24, 2018

from abc import ABC, abstractmethod
from enum import Enum

class Operator(Enum):
	PLUS = '+'
	SUB = '-'
	MULT = '*'
	DIV = '/'

class Operand(ABC): 
	pass
		
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
	
class BinaryOp(Variable): 
	def __init__ (self, left_input, operator, right_input):
		self.left_operand = left_input
		self.operator = operator
		self.right_operand = right_input
	
	def __str__ (self):
		return "(" + str(self.left_operand) + str(self.operator) + str(self.right_operand) + ")"
	
	def get_value(self, x): 
		if (self.operator == Operator.PLUS.value):
			return self.left_operand.get_value(x) + self.right_operand.get_value(x)
		elif (self.operator == Operator.SUB.value):
			return self.left_operand.get_value(x) - self.right_operand.get_value(x)
		elif (self.operator == Operator.MULT.value):
			return self.left_operand.get_value(x) * self.right_operand.get_value(x)
		elif (self.operator == Operator.DIV.value):
			return self.left_operand.get_value(x) / self.right_operand.get_value(x)
		
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
			