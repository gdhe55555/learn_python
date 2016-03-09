#!/usr/bin/env python
    
import sys

import wx

print sys.path

print wx.__version__

app = wx.App()

frame = wx.Frame(None, -1, title = "Hello world",
        pos=(300, 400), size=(200,150))
frame.Show()

app.MainLoop()
