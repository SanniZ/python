#!/usr/bin/python

import wx  
  
class MyFrame(wx.Frame):  
  
    def __init__(self, parent=None, id=-1, title=''):  
        wx.Frame.__init__(self, parent, id, title,  
                          size=(410, 335))  
        self.panel = wx.Panel(self)  
        self.bt_load = wx.Button(self.panel, label='Open')  
        self.bt_save = wx.Button(self.panel, label='Save')  
        self.filename = wx.TextCtrl(self.panel)  
        self.contents = wx.TextCtrl(self.panel,  
                                    style=wx.TE_MULTILINE | wx.HSCROLL)  
        self.hbox = wx.BoxSizer()  
        self.hbox.Add(self.filename, proportion=1, flag=wx.EXPAND)  
        self.hbox.Add(self.bt_load, flag=wx.LEFT, border=5)  
        self.hbox.Add(self.bt_save, flag=wx.LEFT, border=5)  
  
        self.vbox = wx.BoxSizer(wx.VERTICAL)  
        self.vbox.Add(self.hbox, flag=wx.EXPAND | wx.ALL, border=5)  
        self.vbox.Add(self.contents, proportion=1,  
                      flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,  
                      border=5)  
        self.panel.SetSizer(self.vbox)  
  
if __name__ == "__main__":  
    app = wx.App()  
    MyFrame(None, title='Simple Editor').Show()  
    app.MainLoop() 
