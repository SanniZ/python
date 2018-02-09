#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__author__ = 'Byng Zeng'

from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, World!')
		self.helloLabel.pack()
		self.cancelButton = Button(self, text='Cancel', command=self.quit)
		self.cancelButton.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title("Hello, World!")
app.mainloop()
