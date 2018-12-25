#!/usr/bin/env python3
#
# graphics.py
# The graphics interface for the calculator
# Last Modified: December 24, 2018

import wx

class CalculatorFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title = title, size = (640, 360), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		panel = wx.Panel(self)
		self.createTextField(panel)
		self.createNumberButton(panel)
		stringBinaryOp = wx.StaticText(panel, label = "Binary Operators", pos = (20, 170))
		stringFunction = wx.StaticText(panel, label = "Functions", pos = (320, 170))
		self.createBinaryOpButton(panel)
		self.createFunctionButton(panel)
		stringDerivative = wx.StaticText(panel, label = "Derivative", pos = (20, 260))
		stringDerivative = wx.StaticText(panel, label = "Clear", pos = (320, 260))
		self.createDerivativeButton(panel)
		self.createClearButton(panel)

	def createTextField(self, panel):
		self.textField = wx.TextCtrl(panel, pos = (20, 20), size = (600, 70), style = wx.TE_RIGHT | wx.TE_MULTILINE ) 
	
	def createNumberButton(self, panel):
		self.button0 = wx.Button(panel, label = "0", pos = (20, 100), size = (50, 50))
		self.button1 = wx.Button(panel, label = "1", pos = (80, 100), size = (50, 50))
		self.button2 = wx.Button(panel, label = "2", pos = (140, 100), size = (50, 50))
		self.button3 = wx.Button(panel, label = "3", pos = (200, 100), size = (50, 50))
		self.button4 = wx.Button(panel, label = "4", pos = (260, 100), size = (50, 50))
		self.button5 = wx.Button(panel, label = "5", pos = (320, 100), size = (50, 50))
		self.button6 = wx.Button(panel, label = "6", pos = (380, 100), size = (50, 50))
		self.button7 = wx.Button(panel, label = "7", pos = (440, 100), size = (50, 50))
		self.button8 = wx.Button(panel, label = "8", pos = (500, 100), size = (50, 50))
		self.button9 = wx.Button(panel, label = "9", pos = (560, 100), size = (50, 50))
	
	def createBinaryOpButton(self, panel):
		self.buttonPlus = wx.Button(panel, label =" +", pos = (20, 190), size = (65, 50))
		self.buttonSub = wx.Button(panel, label = "-", pos = (95, 190), size = (65, 50))
		self.buttonMult = wx.Button(panel, label = "*", pos = (170, 190), size = (65, 50))
		self.buttonDiv = wx.Button(panel, label = "/", pos = (245, 190), size = (65, 50))
		
	def createFunctionButton(self, panel):
		self.buttonPoly = wx.Button(panel, label = "x^n", pos = (320, 190), size = (65, 50))
		self.buttonSin = wx.Button(panel, label = "sin", pos = (395, 190), size = (65, 50))
		self.buttonCos = wx.Button(panel, label = "cos", pos = (470, 190), size = (65, 50))
		self.buttonExp = wx.Button(panel, label = "exp", pos = (545, 190), size = (65, 50))
	
	def createDerivativeButton(self, panel):
		self.buttonDerivative = wx.Button(panel, label = "Take Derivative", pos = (20, 280), size = (290, 50))
		
	def createClearButton(self, panel): 
		self.buttonC = wx.Button(panel, label = "C", pos = (320, 280), size = (140, 50))
		self.buttonCE = wx.Button(panel, label = "CE", pos = (470, 280), size = (140, 50))
	
if __name__ == '__main__':
	app = wx.App()
	frame = CalculatorFrame(None, title = "Python calculator")
	frame.Show()
	app.MainLoop()
