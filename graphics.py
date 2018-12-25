#!/usr/bin/env python3
#
# graphics.py
# The graphics interface for the calculator
# Last Modified: December 24, 2018

import wx

class CalculatorFrame(wx.Frame):
	
	def __init__(self, parent, title):
		
		wx.Frame.__init__(self, parent, title = title, size = (840, 360), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		panel = wx.Panel(self)
		
		# Create the text field and the calculate button for the calculator
		self.createTextField(panel)
		self.createCalculateButton(panel)
		
		# Create the sandbox to temporarily store operands
		self.createSandbox(panel)
		
		# Create the buttons for number input on the first row 
		self.createNumberButton(panel)
		
		# Create the basic operators and functions on the second row
		self.second_row_x = 170
		self.createBinaryOpButton(panel)
		self.createFunctionButton(panel)
		
		# Create the button to take derivatives and backspace functionality on the third row
		self.third_row_x = 260
		self.createDerivativeButton(panel)
		self.createClearButton(panel)

	def createTextField(self, panel):
		self.textField = wx.TextCtrl(panel, pos = (20, 20), size = (590, 70), style = wx.TE_RIGHT | wx.TE_MULTILINE ) 
		
	def createCalculateButton(self, panel):
		self.buttonCalculate = wx.Button(panel, label ="Calculate", pos = (630, 20), size = (190, 70))
		
	def createSandbox(self, panel):
		stringSandBox = wx.StaticText(panel, label = "Sandbox", pos = (630, 110))
		self.textField = wx.TextCtrl(panel, pos = (630, 130), size = (190, 200), style = wx.TE_RIGHT | wx.TE_MULTILINE ) 
	
	def createNumberButton(self, panel):
		self.numberButtonList = []
		for i in range(10):
			self.numberButtonList.append(wx.Button(panel, label = str(i), pos = (20 + 60 * i, 100), size = (50, 50)))
	
	def createBinaryOpButton(self, panel):
		stringBinaryOp = wx.StaticText(panel, label = "Binary Operators", pos = (20, self.second_row_x))
		self.buttonPlus = wx.Button(panel, label ="+", pos = (20, self.second_row_x + 20), size = (65, 50))
		self.buttonSub = wx.Button(panel, label = "-", pos = (95, self.second_row_x + 20), size = (65, 50))
		self.buttonMult = wx.Button(panel, label = "*", pos = (170, self.second_row_x + 20), size = (65, 50))
		self.buttonDiv = wx.Button(panel, label = "/", pos = (245, self.second_row_x + 20), size = (65, 50))
		
	def createFunctionButton(self, panel):
		stringFunction = wx.StaticText(panel, label = "Functions", pos = (320, self.second_row_x))
		self.buttonPoly = wx.Button(panel, label = "x^n", pos = (320, self.second_row_x + 20), size = (65, 50))
		self.buttonSin = wx.Button(panel, label = "sin", pos = (395, self.second_row_x + 20), size = (65, 50))
		self.buttonCos = wx.Button(panel, label = "cos", pos = (470, self.second_row_x + 20), size = (65, 50))
		self.buttonExp = wx.Button(panel, label = "exp", pos = (545, self.second_row_x + 20), size = (65, 50))
	
	def createDerivativeButton(self, panel):
		stringDerivative = wx.StaticText(panel, label = "Derivative", pos = (20, self.third_row_x))
		self.buttonDerivative = wx.Button(panel, label = "X", pos = (20, self.third_row_x + 20), size = (65, 50))
		self.buttonDerivative = wx.Button(panel, label = "Take Derivative", pos = (95, self.third_row_x + 20), size = (215, 50))
		
	def createClearButton(self, panel): 
		stringDerivative = wx.StaticText(panel, label = "Clear", pos = (320, self.third_row_x))
		self.buttonC = wx.Button(panel, label = "C", pos = (320, self.third_row_x + 20), size = (140, 50))
		self.buttonCE = wx.Button(panel, label = "CE", pos = (470, self.third_row_x + 20), size = (140, 50))
	
if __name__ == '__main__':
	app = wx.App()
	frame = CalculatorFrame(None, title = "Python calculator")
	frame.Show()
	app.MainLoop()
