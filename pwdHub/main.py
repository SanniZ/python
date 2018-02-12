#!/usr/bin/python
# _*_ coding: utf-8 _*_

# __author__ = 'Byng,Zeng'
# __Date__ == '2018/02/11'

from Tkinter import *
import sqlite3

class PwdHub(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.createWidgets()
	
	def createWidgets(self):
		frmRoot = Frame()
		# options
		frmOps = Frame(frmRoot)
		self.radOps = Variable()
		Radiobutton(frmOps, variable=self.radOps, text='Show',   value=1).grid(row=0, column=0, padx=8)
		Radiobutton(frmOps, variable=self.radOps, text='Insert', value=2).grid(row=0, column=1, padx=8)
		Radiobutton(frmOps, variable=self.radOps, text='Update', value=3).grid(row=0, column=2, padx=8)
		Radiobutton(frmOps, variable=self.radOps, text='Delete', value=4).grid(row=0, column=3, padx=8)
		Button(frmOps, text='Run', command=self.onBtnRun, width=8).grid(row=0, column=4, padx=54)
		frmOps.pack(fill=X)
		# Enter Text
		frmTxt = Frame(frmRoot)
		Label(frmTxt, text='URL:').grid(row=0, column=0, sticky=W)
		self.enURL = Variable()
		Entry(frmTxt, textvariable=self.enURL, width=22).grid(row=0, column=1)
		Label(frmTxt, text='Type:').grid(row=0, column=2, sticky=W)
		self.enType = Variable()
		Entry(frmTxt, textvariable=self.enType, width=22).grid(row=0, column=3)
		Label(frmTxt, text='UserID:').grid(row=1, column=0, sticky=W)
		self.enUsrID = Variable()
		Entry(frmTxt, textvariable=self.enUsrID, width=22).grid(row=1, column=1)
		Label(frmTxt, text='Password:').grid(row=1, column=2)
		self.enPwd = Variable()
		Entry(frmTxt, textvariable=self.enPwd, width=22).grid(row=1, column=3)
		frmTxt.pack(fill=X)
		# Data
		frmData = Frame(frmRoot)
		Label(frmData, text='Data:').grid(row=0, column=0, sticky=W)
		self.txtData = Text(frmData)
		self.txtData.grid(row=1, column=0)
		self.txtData.config(state=DISABLED, width=64)
		frmData.pack()
		frmRoot.pack()

	def onBtnRun(self):
		ops = self.radOps.get()
		if ops == 1:
			self.show_data()
		elif ops == 2:
			self.insert_data()
		elif ops == 3:
			self.update_password()
		elif ops == 4:
			self.delele_data()
		else:
			Message(self.master, text='Please select your option!').pack()


	def sql_exec(self, sql, data):
		conn = sqlite3.connect('pwdHub.db')
		cur = conn.cursor()
		cur.execute(sql, data)
		cur.close()
		conn.commit()
		conn.close()

	def get_data_one(self, row):
		conn = sqlite3.connect('pwdHub.db')
		cur = conn.cursor()
		sql = '''Select * From pwdHub'''
		cur.execute(sql)
		data = cur.fetchone()
		cur.close()
		conn.commit()
		conn.close()
		return data

	def get_data_all(self):
		conn = sqlite3.connect('pwdHub.db')
		cur = conn.cursor()
		sql = '''Select * From pwdHub'''
		cur.execute(sql)
		data = cur.fetchall()
		cur.close()
		conn.commit()
		conn.close()
		return data

	def insert_data(self):
		sql = '''Insert into pwdHub (URL, Type, UserID, Password) Values (?,?,?,?)'''
		data = (self.enURL.get(), self.enType.get(), self.enUsrID.get(), self.enPwd.get())
		self.sql_exec(sql,data)

	def update_password(self):
		sql = '''Update pwdHub set Password=? Where URL=? and Type=? and UserID=?'''
		data = (self.enPwd.get(), self.enURL.get(), self.enType.get(), self.enUsrID.get())
		self.sql_exec(sql,data)

	def show_data(self):
		data = self.get_data_all()
		if len(data):
			self.txtData.config(state=NORMAL)
			for i in range(len(data)):
				self.txtData.insert(END, data[i])
				self.txtData.insert(END, '\n')
		self.txtData.config(state=DISABLED)

	def delele_data(self):
		sql = '''Delete From pwdHub Where URL=? and Type=? and UserID=?'''
		data = (self.enURL.get(), self.enType.get(), self.enUsrID.get())
		self.sql_exec(sql,data)

if __name__ == '__main__':
	root = Tk()
	root.title('Password Hub')
	root.geometry('480x480')
	root.resizable(width=False, height=False)
	PwdHub(root)
	root.mainloop()
