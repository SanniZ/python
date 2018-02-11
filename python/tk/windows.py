#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__: Byng,Zeng

from Tkinter import *
from tkFont import Font


try:  
	from ttk import (Button, Scrollbar)
except ImportError:  
	pass

class MyFrame(Frame):  
	def __init__(self, master=None):  
	    Frame.__init__(self, master)  
	    self.window = master  
	    self.pack(fill=BOTH, expand=True)  
	    self.font_en = Font(self, size=14)  
	    self.create_widgets()  

	def create_widgets(self):  
	    self.fm_up = Frame(self)  
	    self.en = Entry(self.fm_up, font=self.font_en)  
	    self.en.pack(side=LEFT, expand=True, fill=X, padx=5, pady=5)  
	    self.loadbutton = Button(self.fm_up, text='Open')  
	    self.savebutton = Button(self.fm_up, text='Save')  
	    self.loadbutton.pack(side=LEFT, pady=5)  
	    self.savebutton.pack(side=LEFT, padx=5)  
	    self.fm_up.pack(fill=X)  

	    self.fm_down = Frame(self)  
	    self.fm_text_scb_ver = Frame(self.fm_down)  
	    self.text = Text(self.fm_text_scb_ver, width=30, height=15)  
	    self.scb_ver = Scrollbar(self.fm_text_scb_ver)  
	    self.text.pack(side=LEFT, fill=BOTH, expand=True, padx=5)  
	    self.scb_ver.pack(side=RIGHT, fill=Y)  
	    self.fm_text_scb_ver.pack(fill=BOTH, expand=True)  
	    self.fm_scb_hor = Frame(self.fm_down)  
	    self.scb_hor = Scrollbar(self.fm_scb_hor, orient=HORIZONTAL)  
	    self.scb_hor.pack(fill=X)  
	    self.fm_scb_hor.pack(fill=X)  
	    self.text.config(xscrollcommand=self.scb_hor.set,  
		             yscrollcommand=self.scb_ver.set)  
	    self.scb_hor.config(command=self.text.xview)  
	    self.scb_ver.config(command=self.text.yview)  
	    self.fm_down.pack(fill=BOTH, expand=True)  

if __name__ == "__main__":  
	window = Tk()  
	window.title('Simple Editor')  
	MyFrame(window)  
	window.mainloop()  
