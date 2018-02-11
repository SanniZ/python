#!/usr/bin/python

from Tkinter import *
from tkFont import Font

import RegisterWindow

class MainWindow(Frame):
	def __init__(self, master):
		if master is None:
			win = Tk()
			win.title('Register')
			win.geometry('256x96')
			win.resizable(width=False, height=False)
			master = win
		Frame.__init__(self, master)
		self.master = master
		self.font = Font(self, size=14)
		self.pack(fill=BOTH, expand=True)
		self.createWidget(master)		

	def onBtnSignIn(self):
		print('Sign In Event.', varName.get())

	def onBtnSignOut(self):
		print('Sign Out Event.')

	def onBtnRegister(self):
		RegisterWindow.RegisterWindow(None)

	def createWidget(self, master):
		# create root containner
		frmRoot = Frame(master)
		# create name containner
		frmName = Frame(frmRoot)
		Label(frmName, text='User Name:', bg='pink', justify='left', width=12).pack(side=LEFT)
		global varName
		varName = Variable()
		Entry(frmName, textvariable=varName).pack(side=RIGHT)
		frmName.pack()
		# create password containner
		frmPwd = Frame(frmRoot)
		Label(frmPwd, text='User Password:', bg='pink', justify='left', width=12).pack(side=LEFT)
		Entry(frmPwd, textvariable=Variable()).pack(side=RIGHT)
		frmPwd.pack()
		# create option containner
		frmOpt = Frame(frmRoot)
		Button(frmOpt, text='Sign In', command=self.onBtnSignIn).pack(side=LEFT)
		Button(frmOpt, text='Sign Out', command=self.onBtnSignOut).pack(side=LEFT)
		Button(frmOpt, text='Register', command=self.onBtnRegister).pack(side=RIGHT)
		frmOpt.pack()
		# show root containner
		frmRoot.pack()
