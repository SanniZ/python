#!/usr/bin/python
# _*_ coding:utf-8 -*-
# author: Byng,Zeng

from Tkinter import *

import MainWindow

def main():
	app = Tk()
	app.title('User')
	app.geometry('256x96')
	app.resizable(width=False, height=False)
	MainWindow.MainWindow(app)
	app.mainloop()


if __name__ == '__main__':
	main()
