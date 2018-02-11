#!/usr/bin/python

from Tkinter import *
from tkFont import Font

class RegisterWindow(Frame):
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

	def onBtnOK(self):
		print(user_cfm_pwd.get())
		print(user_pwd.get())

	def createWidget(self, master):
		# root
		frmRoot = Frame(master)
		# user name
		frmName = Frame(frmRoot)
		Label(frmName, text='User Name:', bg='pink', justify='left', width=12).pack(side=LEFT)
		self.en_name = Entry(frmName, textvariable=Variable()).pack(side=RIGHT)
		frmName.pack()
		# user password
		frmPwd = Frame(frmRoot)
		Label(frmPwd, text='User Password:', bg='pink', justify='left', width=12).pack(side=LEFT)
		global user_pwd 
		user_pwd = Variable()
		Entry(frmPwd, textvariable=user_pwd).pack(side=RIGHT)
		frmPwd.pack()
		# comfirm password
		frmPwd = Frame(frmRoot)
		Label(frmPwd, text='Comfirm Password:', bg='pink', justify='left', width=12).pack(side=LEFT)
		global user_cfm_pwd 
		user_cfm_pwd = Variable()
		Entry(frmPwd, textvariable=user_cfm_pwd).pack(side=RIGHT)
		frmPwd.pack()
		# option
		frmOpt = Frame(frmRoot)
		btnOK = Button(frmOpt, text='OK', command=self.onBtnOK).pack(side=LEFT)
		frmOpt.pack()
		# show root containner
		frmRoot.pack()
