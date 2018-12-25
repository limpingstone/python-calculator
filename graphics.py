#!/usr/bin/env python3
#
# graphics.py
# The graphics interface for the calculator
# Last Modified: December 25, 2018

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
		
		# Create the buttons for number input and the object generating button on the first row 
		self.createNumberButton(panel)
		
		# Create the basic operators and functions on the second row
		self.second_row_x = 170
		self.createBinaryOpButton(panel)
		self.createFunctionButton(panel)
		
		# Create the button to take derivatives and backspace functionality on the third row
		self.third_row_x = 260
		self.createDerivativeButton(panel)
		self.createClearButton(panel)

	def onclick(self, event):
		print(event.GetEventObject().GetLabel())
		self.notGenerated = True
		
	def onclick_number(self, event):
		print(event.GetEventObject().GetLabel())
		self.sandbox.SetValue(self.sandbox.GetValue() + event.GetEventObject().GetLabel())
		self.notGenerated = True
		
	def onclick_generate(self, event):
		print(event.GetEventObject().GetLabel())
		if (self.notGenerated):
			self.sandbox.SetValue(self.sandbox.GetValue() + "\n")
		self.notGenerated = False
		
	def onclick_binaryOp(self, event):
		self.sandbox.SetValue(self.sandbox.GetValue() + "{ } " + event.GetEventObject().GetLabel() + " { }")
		self.notGenerated = True
	
	def onclick_poly(self, event):
		self.sandbox.SetValue(self.sandbox.GetValue() + "{ }^?")
		self.notGenerated = True
	
	def onclick_function(self, event):
		self.sandbox.SetValue(self.sandbox.GetValue() + event.GetEventObject().GetLabel() + "({ })")
		self.notGenerated = True
	
	def onclick_clearSandbox(self, event):
		self.sandbox.SetValue("")
		self.notGenerated = True
		
	def createTextField(self, panel):
		self.textField = wx.TextCtrl(panel, pos = (20, 20), size = (590, 70), style = wx.TE_RIGHT | wx.TE_MULTILINE ) 
		
	def createCalculateButton(self, panel):
		self.buttonCalculate = wx.Button(panel, label ="Calculate", pos = (630, 20), size = (190, 70))
		
	def createSandbox(self, panel):
		stringSandbox = wx.StaticText(panel, label = "Sandbox", pos = (630, 110))
		self.sandbox = wx.TextCtrl(panel, pos = (630, 130), size = (190, 200), style = wx.TE_RIGHT | wx.TE_MULTILINE | wx.TE_READONLY) 
	
	def createNumberButton(self, panel):
		self.numberButtonList = []
		for i in range(10):
			self.numberButtonList.append(wx.Button(panel, label = str(i), pos = (20 + 50 * i, 110), size = (40, 40)))
			self.Bind(wx.EVT_BUTTON, self.onclick_number, self.numberButtonList[i])
		self.generateNumberObjButton = wx.Button(panel, label ="Generate", pos = (520, 110), size = (90, 40))
		self.Bind(wx.EVT_BUTTON, self.onclick_generate, self.generateNumberObjButton)
	
	def createBinaryOpButton(self, panel):
		stringBinaryOp = wx.StaticText(panel, label = "Binary Operators", pos = (20, self.second_row_x))
		self.buttonPlus = wx.Button(panel, label ="+", pos = (20, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_binaryOp, self.buttonPlus)
		self.buttonSub = wx.Button(panel, label = "-", pos = (95, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_binaryOp, self.buttonSub)
		self.buttonMult = wx.Button(panel, label = "*", pos = (170, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_binaryOp, self.buttonMult)
		self.buttonDiv = wx.Button(panel, label = "/", pos = (245, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_binaryOp, self.buttonDiv)
		
	def createFunctionButton(self, panel):
		stringFunction = wx.StaticText(panel, label = "Functions", pos = (320, self.second_row_x))
		self.buttonPoly = wx.Button(panel, label = "x^n", pos = (320, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_poly, self.buttonPoly)
		self.buttonSin = wx.Button(panel, label = "sin", pos = (395, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_function, self.buttonSin)
		self.buttonCos = wx.Button(panel, label = "cos", pos = (470, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_function, self.buttonCos)
		self.buttonExp = wx.Button(panel, label = "exp", pos = (545, self.second_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_function, self.buttonExp)
	
	def createDerivativeButton(self, panel):
		stringDerivative = wx.StaticText(panel, label = "Derivative", pos = (20, self.third_row_x))
		self.buttonVariable = wx.Button(panel, label = "X", pos = (20, self.third_row_x + 20), size = (65, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick, self.buttonVariable)
		self.buttonDerivative = wx.Button(panel, label = "Take Derivative", pos = (95, self.third_row_x + 20), size = (215, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick, self.buttonDerivative)
		
	def createClearButton(self, panel): 
		stringDerivative = wx.StaticText(panel, label = "Clear", pos = (320, self.third_row_x))
		self.buttonC = wx.Button(panel, label = "C", pos = (320, self.third_row_x + 20), size = (70, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick, self.buttonC)
		self.buttonCE = wx.Button(panel, label = "CE", pos = (400, self.third_row_x + 20), size = (70, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick, self.buttonCE)
		self.buttonClearSandbox = wx.Button(panel, label = "Clear Sandbox", pos = (480, self.third_row_x + 20), size = (130, 50))
		self.Bind(wx.EVT_BUTTON, self.onclick_clearSandbox, self.buttonClearSandbox)
	
if __name__ == '__main__':
	app = wx.App()
	frame = CalculatorFrame(None, title = "Python calculator")
	frame.Show()
	app.MainLoop()
