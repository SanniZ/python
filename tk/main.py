#!/usr/bin/python
# _*_ coding:utf-8 -*-
# author: Byng,Zeng

from Tkinter import *

def add_func():
	en_result.settext('123')

def main():
	app = Tk()
	app.title('Hello, Python Tkinter!')
	app.geometry('640x480')
	app.resizable(width=False, height=False)

	frm_num1 = Frame(app)
	Label(frm_num1, text='Number1:', bg="pink").pack(side=LEFT)
	en_num1 = Entry(frm_num1, textvariable=Variable()).pack(side=RIGHT)
	frm_num1.pack(side=TOP)

	frm_num2 = Frame(app)
	Label(frm_num2, text='Number2:', bg="green").pack(side=LEFT)
	en_num2 = Entry(frm_num2, textvariable=Variable()).pack(side=RIGHT)
	frm_num2.pack(side=TOP)

	frm_option = Frame(app)
	Label(frm_option, text='Result:', bg="green").pack(side=LEFT)
	en_result = Entry(frm_option, textvariable=Variable()).pack(side=RIGHT)
	frm_option.pack(side=TOP)

	frm3 = Frame(app)
	Button(frm3, text='OK', width=8, command=add_func).pack(side=LEFT)
	Button(frm3, text='Exit', width=8, command=app.quit).pack(side=RIGHT)
	frm3.pack(side=TOP)

	app.mainloop()


if __name__ == '__main__':
	main()
