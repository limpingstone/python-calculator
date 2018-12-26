#!/usr/bin/env python3
#
# graphics.py
# The graphics interface for the calculator
# Last Modified: December 25, 2018

import wx
from operand import *

class CalculatorFrame(wx.Frame):
	def __init__(self, parent, title):
		
		# Create frame 
		wx.Frame.__init__(self, parent, title = title, size = (640, 480), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		panel = wx.Panel(self)
		
		# Layouts for the Calculator GUI 
		self.element_height = 30
		self.row_1_y = 30
		self.row_2_y = 120
		self.row_3_y = 180
		self.row_4_y = 230
		self.row_5_y = 310
		
		self.sandbox_items = []
		
		# Setup functions
		self.createSandbox(panel)
		self.createBasicOperands(panel)
		self.createBinaryOp(panel)
		self.createFunction(panel)
		self.createResultField(panel)
		self.createCalculatorButton(panel)

	def onclick_numberButton(self, event):
		if (self.numberField.GetLineLength(0) != 0):
			self.sandbox_items.append(Number(self.numberField.GetLineText(0)))
			print(event.GetEventObject().GetLabel() + ": " + self.numberField.GetLineText(0) + " --- Length of list = " + str(len(self.sandbox_items)))
			self.appendToSandbox(self.numberField.GetLineText(0))
			self.numberField.Clear()
		
	def onclick_variableButton(self, event):
		self.sandbox_items.append(Variable())
		print(event.GetEventObject().GetLabel() + " --- Length of list = " + str(len(self.sandbox_items)))
		self.appendToSandbox("x")
		
	def onclick_clearSandboxButton(self, event):
		self.sandbox.SetValue("")
		self.sandbox_items = []
	
	def onclick_operatorButton(self, event):
		# PLUS = 0, SUB = 1, MULT = 2, DIV = 3
		self.operator_choice = (self.operator_choice + 1) % 4
		if (self.operator_choice == 0): 
			self.operatorButton.SetLabel("+")
		elif (self.operator_choice == 1): 
			self.operatorButton.SetLabel("-")
		elif (self.operator_choice == 2): 
			self.operatorButton.SetLabel("*")
		elif (self.operator_choice == 3): 
			self.operatorButton.SetLabel("/")
		
	def onclick_binaryOpButton(self, event):
		# If one of the operand is left blank, the generate button will not validate
		# If both the operands are correctly filled, the button will create the binary operand object with the appropriate operator 
		if (self.leftOperandField.GetLineLength(0) != 0 and self.rightOperandField.GetLineLength(0) != 0):
			left = self.sandbox_items[int(self.leftOperandField.GetLineText(0)) - 1]
			right = self.sandbox_items[int(self.rightOperandField.GetLineText(0)) - 1]
			if (self.operator_choice == 0): 
				operator = '+'
			elif (self.operator_choice == 1): 
				newBinaryOp = BinaryOp(left, '-', right)
				operator = '-'
			elif (self.operator_choice == 2): 
				newBinaryOp = BinaryOp(left, '*', right)
				operator = '*'
			elif (self.operator_choice == 3): 
				operator = '/'
				
			# Append the new binary operand object to the list and display it in the sandbox
			newBinaryOp = BinaryOp(left, operator, right)
			self.sandbox_items.append(newBinaryOp)
			self.appendToSandbox(str(newBinaryOp))
			print("Generated new binary operand: " + str(newBinaryOp) + " --- Length of list = " + str(len(self.sandbox_items)))

			# Clear the left and right fields after the BinaryOp object is generated 
			self.leftOperandField.Clear()
			self.rightOperandField.Clear()
	
	# The function that creates the sandbox 
	def createSandbox(self, panel):
		stringSandbox = wx.StaticText(panel, label = "Sandbox", pos = (450, self.row_1_y - 20))
		self.sandbox = wx.TextCtrl(panel, pos = (450, self.row_1_y), size = (170, 190), style = wx.TE_LEFT | wx.TE_MULTILINE) 
		self.clearSandboxButton = wx.Button(panel, label ="Clear Sandbox", pos = (450, self.row_4_y), size = (170, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_clearSandboxButton, self.clearSandboxButton)
	
	# The helper method that iterates the list of operands in the sandbox 
	def appendToSandbox(self, item_string):
		self.sandbox.SetValue(self.sandbox.GetValue() + "[" + str(len(self.sandbox_items)) + "] " + item_string + "\n")
	
	def createBasicOperands(self, panel):
		stringBasicOperands = wx.StaticText(panel, label = "Basic Operands", pos = (20, self.row_1_y - 20))
		self.numberField = wx.TextCtrl(panel, pos = (20, self.row_1_y), size = (130, self.element_height), style = wx.TE_RIGHT) 
		self.numberButton = wx.Button(panel, label ="Generate Number", pos = (160, self.row_1_y), size = (130, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_numberButton, self.numberButton)
		
		self.variableButton = wx.Button(panel, label ="Generate Variable", pos = (300, self.row_1_y), size = (130, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_variableButton, self.variableButton)
		
	def createBinaryOp(self, panel):
		
		# Note to the user
		stringIndexNote = wx.StaticText(panel, label = "* For the blanks below, please enter the index in the sandbox", pos = (20, self.row_2_y - 45))
		stringBinaryOp = wx.StaticText(panel, label = "Binary Operators", pos = (20, self.row_2_y - 20))
		
		# Index field for left operand 
		self.leftOperandField = wx.TextCtrl(panel, pos = (20, self.row_2_y), size = (130, self.element_height), style = wx.TE_RIGHT) 
		
		# Button for changing the binary operator
		self.operatorButton = wx.Button(panel, label ="+", pos = (160, self.row_2_y), size = (40, self.element_height))
		self.operator_choice = 0;
		self.Bind(wx.EVT_BUTTON, self.onclick_operatorButton, self.operatorButton)
		
		# Index field for right operand 
		self.rightOperandField = wx.TextCtrl(panel, pos = (210, self.row_2_y), size = (130, self.element_height), style = wx.TE_RIGHT) 
		
		# Button to generate a binary operand object 
		self.binaryOpButton = wx.Button(panel, label ="Generate", pos = (350, self.row_2_y), size = (80, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_binaryOpButton, self.binaryOpButton)
	
	def createFunction(self, panel):
		stringFunction = wx.StaticText(panel, label = "Functions", pos = (20, self.row_3_y - 20))
		self.baseField = wx.TextCtrl(panel, pos = (20, self.row_3_y), size = (210, self.element_height), style = wx.TE_RIGHT) 
		self.polyCaret = wx.StaticText(panel, label = "^", pos = (240, self.row_3_y))
		self.powerField = wx.TextCtrl(panel, pos = (260, self.row_3_y), size = (80, self.element_height), style = wx.TE_RIGHT) 
		self.polyButton = wx.Button(panel, label ="Generate", pos = (350, self.row_3_y), size = (80, self.element_height))
		
		self.functionChoiceButton = wx.Button(panel, label ="sin", pos = (20, self.row_4_y), size = (80, self.element_height))
		self.leftParenthesis = wx.StaticText(panel, label = "(", pos = (115, self.row_4_y + 8))
		self.functionField = wx.TextCtrl(panel, pos = (130, self.row_4_y), size = (190, self.element_height), style = wx.TE_RIGHT) 
		self.rightParenthesis = wx.StaticText(panel, label = ")", pos = (330, self.row_4_y + 8))
		self.functionButton = wx.Button(panel, label ="Generate", pos = (350, self.row_4_y), size = (80, self.element_height))
		
	def createResultField(self, panel):
		stringFunction = wx.StaticText(panel, label = "Result", pos = (20, self.row_5_y - 20))
		self.resultField = wx.TextCtrl(panel, pos = (20, self.row_5_y), size = (410, 150), style = wx.TE_RIGHT | wx.TE_MULTILINE ) 
		
	def createCalculatorButton(self, panel):
		self.CButton = wx.Button(panel, label ="C", pos = (450, self.row_5_y), size = (80, self.element_height))
		self.CEButton = wx.Button(panel, label ="CE", pos = (540, self.row_5_y), size = (80, self.element_height))
		self.valueButton = wx.Button(panel, label ="Value", pos = (450, self.row_5_y + 40), size = (170, self.element_height))
		self.printButton = wx.Button(panel, label ="Print Expression", pos = (450, self.row_5_y + 80), size = (170, self.element_height))
		self.derivativeButton = wx.Button(panel, label ="Take Derivative", pos = (450, self.row_5_y + 120), size = (170, self.element_height))
	
if __name__ == '__main__':
	app = wx.App()
	frame = CalculatorFrame(None, title = "Python Scientific Calculator")
	frame.Show()
	app.MainLoop()
