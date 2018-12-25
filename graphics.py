#!/usr/bin/env python3
#
# graphics.py
# The graphics interface for the calculator
# Last Modified: December 24, 2018

import wx

app = wx.App()

frame = wx.Frame(None, title='Simple application')
frame.Show()

app.MainLoop()