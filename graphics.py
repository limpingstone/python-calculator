#!/usr/bin/env python3
#
# graphics.py
# The graphics interface for the calculator
# Created: December 25, 2018

import wx
from operand import *
from function import *

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
		
		# Setup the layout of GUI
		self.createSandbox(panel)
		self.createBasicOperands(panel)
		self.createBinaryOp(panel)
		self.createFunction(panel)
		self.createResultField(panel)
		self.createCalculatorButton(panel)

	# The function that adds a number object to the sandbox list
	def onclick_numberButton(self, event):
		if (self.numberField.GetLineLength(0) != 0):
			self.sandbox_items.append(Number(self.numberField.GetLineText(0)))
			print(event.GetEventObject().GetLabel() + ": " + self.numberField.GetLineText(0) + " --- Length of list = " + str(len(self.sandbox_items)))
			self.appendToSandbox(self.numberField.GetLineText(0))
			self.numberField.Clear()
		
	# The function that adds a variable to the sandbox list 
	def onclick_variableButton(self, event):
		self.sandbox_items.append(Variable())
		print(event.GetEventObject().GetLabel() + " --- Length of list = " + str(len(self.sandbox_items)))
		self.appendToSandbox("x")
	
	# The function that clears the sandbox when the clear button is clicked
	def onclick_clearSandboxButton(self, event):
		self.sandbox.SetValue("")
		self.sandbox_items = []
	
	# The function that toggles between the four elementary arithmatic operators 
	# PLUS(+) = 0; SUB(-) = 1; MULT(*) = 2; DIV(/) = 3
	def onclick_operatorButton(self, event):
		self.operator_choice = (self.operator_choice + 1) % 4
		if (self.operator_choice == 0): 
			self.operatorButton.SetLabel("+")
		elif (self.operator_choice == 1): 
			self.operatorButton.SetLabel("-")
		elif (self.operator_choice == 2): 
			self.operatorButton.SetLabel("*")
		elif (self.operator_choice == 3): 
			self.operatorButton.SetLabel("/")
	
	# The function that generates binary operand objects when clicked
	def onclick_binaryOpButton(self, event):
		# If one of the operand is left blank, the generate button will not validate
		# If both the operands are correctly filled, the button will create the binary operand object with the appropriate operator 
		if (self.leftOperandField.GetLineLength(0) != 0 and self.rightOperandField.GetLineLength(0) != 0):
			left = self.sandbox_items[int(self.leftOperandField.GetLineText(0)) - 1]
			right = self.sandbox_items[int(self.rightOperandField.GetLineText(0)) - 1]
			if (self.operator_choice == 0): 
				operator = '+'
			elif (self.operator_choice == 1): 
				operator = '-'
			elif (self.operator_choice == 2): 
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
	
	# The function that generates polynomial objects when clicked
	def onclick_polyButton(self, event):
		# If either the base or the power was left blank, the button will not validate
		# If both the base and power are filled in correctly, the button will generate a polynomial object 
		if (self.baseField.GetLineLength(0) != 0 and self.powerField.GetLineLength(0) != 0):
			base = self.sandbox_items[int(self.baseField.GetLineText(0)) - 1]
			power = int(self.powerField.GetLineText(0))
			
			# Append the new polynomial object to the list and display it in the sandbox
			newPolynomial = Polynomial(base, power)
			self.sandbox_items.append(newPolynomial)
			self.appendToSandbox(str(newPolynomial))
			print("Generated new polynomial object: " + str(newPolynomial) + " --- Length of list = " + str(len(self.sandbox_items)))
			
			# Clear the base and power after the polynomial object is generated 
			self.baseField.Clear()
			self.powerField.Clear()
	
	# The function that toggles between different functions
	# sine = 0; cosine = 1; exponential = 2
	def onclick_functionChoiceButton(self, event):
		self.operator_choice = (self.operator_choice + 1) % 3
		if (self.operator_choice == 0): 
			self.functionChoiceButton.SetLabel("sin")
		elif (self.operator_choice == 1): 
			self.functionChoiceButton.SetLabel("cos")
		elif (self.operator_choice == 2): 
			self.functionChoiceButton.SetLabel("exp")
	
	# The function that generates trigonometric or exponential function objects when clicked
	def onclick_functionButton(self, event):
		if (self.functionField.GetLineLength(0) != 0):
			function_operand = self.sandbox_items[int(self.functionField.GetLineText(0)) - 1]
			if (self.operator_choice == 0): 
				expression = Sin(function_operand)
			elif (self.operator_choice == 1): 
				expression = Cos(function_operand)
			elif (self.operator_choice == 2): 
				expression = Exp(function_operand)
				
			# Append the new function object to the list and display it in the sandbox
			function_expression = expression
			self.sandbox_items.append(function_expression)
			self.appendToSandbox(str(function_expression))
			print("Generated new function object: " + str(function_expression) + " --- Length of list = " + str(len(self.sandbox_items)))
			
			# Clear the field after the function object is generated 
			self.functionField.Clear()
	
	# The function that creates the sandbox with the clear button
	def createSandbox(self, panel):
		stringSandbox = wx.StaticText(panel, label = "Sandbox", pos = (450, self.row_1_y - 20))
		self.sandbox = wx.TextCtrl(panel, pos = (450, self.row_1_y), size = (170, 190), style = wx.TE_LEFT | wx.TE_MULTILINE) 
		self.clearSandboxButton = wx.Button(panel, label ="Clear Sandbox", pos = (450, self.row_4_y), size = (170, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_clearSandboxButton, self.clearSandboxButton)
	
	# The helper method that iterates the list of operands and displays the list in the sandbox 
	def appendToSandbox(self, item_string):
		self.sandbox.SetValue(self.sandbox.GetValue() + "[" + str(len(self.sandbox_items)) + "] " + item_string + "\n")
	
	# The function that creates the buttons for generating number and variable objects 
	def createBasicOperands(self, panel):
		stringBasicOperands = wx.StaticText(panel, label = "Basic Operands", pos = (20, self.row_1_y - 20))
		
		# The button for creating a number object with a value entered in the field
		self.numberField = wx.TextCtrl(panel, pos = (20, self.row_1_y), size = (130, self.element_height), style = wx.TE_RIGHT) 
		self.numberButton = wx.Button(panel, label ="Generate Number", pos = (160, self.row_1_y), size = (130, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_numberButton, self.numberButton)
		
		# The button for creating a variable object 
		self.variableButton = wx.Button(panel, label ="Generate Variable", pos = (300, self.row_1_y), size = (130, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_variableButton, self.variableButton)
		
	# The function that creates the buttons for generating binary operand objects 
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
	
	# The function that creates the buttons for generating function objects
	def createFunction(self, panel):
		stringFunction = wx.StaticText(panel, label = "Functions (Input an integer for power)", pos = (20, self.row_3_y - 20))
		
		# The fields required to create a polynomial 
		# Note that the first field takes an index for the base and the second field takes an integer for the power 
		self.baseField = wx.TextCtrl(panel, pos = (20, self.row_3_y), size = (210, self.element_height), style = wx.TE_RIGHT) 
		self.polyCaret = wx.StaticText(panel, label = "^", pos = (240, self.row_3_y))
		self.powerField = wx.TextCtrl(panel, pos = (260, self.row_3_y), size = (80, self.element_height), style = wx.TE_RIGHT) 
		self.polyButton = wx.Button(panel, label ="Generate", pos = (350, self.row_3_y), size = (80, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_polyButton, self.polyButton)
		
		# The button to toggle through different functions
		self.functionChoiceButton = wx.Button(panel, label ="sin", pos = (20, self.row_4_y), size = (80, self.element_height))
		self.function_choice = 0
		self.Bind(wx.EVT_BUTTON, self.onclick_functionChoiceButton, self.functionChoiceButton)
		
		# GUI Layout for functions
		self.leftParenthesis = wx.StaticText(panel, label = "(", pos = (115, self.row_4_y + 8))
		self.functionField = wx.TextCtrl(panel, pos = (130, self.row_4_y), size = (190, self.element_height), style = wx.TE_RIGHT) 
		self.rightParenthesis = wx.StaticText(panel, label = ")", pos = (330, self.row_4_y + 8))
		
		# The button for generating function objects
		self.functionButton = wx.Button(panel, label ="Generate", pos = (350, self.row_4_y), size = (80, self.element_height))
		self.Bind(wx.EVT_BUTTON, self.onclick_functionButton, self.functionButton)
		
	# The function that creates the field to print the results
	def createResultField(self, panel):
		stringFunction = wx.StaticText(panel, label = "Result", pos = (20, self.row_5_y - 20))
		self.resultField = wx.TextCtrl(panel, pos = (20, self.row_5_y), size = (410, 150), style = wx.TE_RIGHT | wx.TE_MULTILINE ) 
		
	# The function that creates the button for basic calculator functionality
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
