#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on: 2019-01-02

@author: Byng Zeng
"""

from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename

class WebImageCrawlerWindow(object):

    HELP_MENU = (
        '==================================',
        '    Template help',
        '==================================',
        'option: -x xxx',
        '  -x xxx: xxxx',
    )

    def __init__(self, name=None):
        self._name = name
        self._wm = dict()

    def menu_file_open(self):
        print('menu file open')
        f = askopenfilename()
        enPath = self._wm['enPath']
        enPath.insert(0, f)

    def menu_file_exit(self):
        print('menu file exit')

    def menu_about_about(self):
        print('menu about about')

    def create_menu(self, root):
        menubar = Menu(root)

        file_menu = Menu(menubar, tearoff = 0)
        file_menu.add_command(label = 'Open', command=self.menu_file_open)
        file_menu.add_command(label = 'Exit', command=self.menu_file_exit)

        about_menu = Menu(menubar, tearoff = 0)
        about_menu.add_command(label = 'About', command=self.menu_about_about)

        menubar.add_cascade(label = 'File', menu = file_menu)
        menubar.add_cascade(label = 'About', menu = about_menu)
        root['menu'] = menubar

    def on_bnPath_click(self):
        print('get path: %s' % self._wm['enPath'].get())

    def create_main_window_frames(self, root):
        Path = Frame(root)
        Path.pack(side = TOP, fill=X)

        Hdr = Frame(root)
        Hdr.pack(side = TOP, fill=X)

        Fs = Frame(root)
        Fs.pack(side = TOP, fill=X)

        FsList = Frame(Fs)
        FsList.pack(side = LEFT, expand = 1, fill=X)
        SbY = Frame(Fs)
        SbY.pack(side = RIGHT, fill=Y)

        SbX = Frame(root)
        SbX.pack(side = TOP, fill = X)

        self._wm['frmPath'] = Path
        self._wm['frmHdr'] = Hdr
        self._wm['frmFs'] = Fs
        self._wm['frmFsList'] = FsList
        self._wm['frmSbX'] = SbX
        self._wm['frmSbY'] = SbY

    def create_path_widgets(self):
        frm = self._wm['frmPath']
        lbPath = Label(frm, text = 'Path:')
        lbPath.pack(side = LEFT, expand=1, fill=X)
        enPath = Entry(frm, width = 78)
        enPath.pack(side = LEFT, expand=1, fill=X)
        bnPath = Button(frm, text = 'Run', command = self.on_bnPath_click)
        bnPath.pack(side = LEFT, expand=1, fill=X)

        self._wm['lbPath'] = lbPath
        self._wm['enPath'] = enPath
        self._wm['bnPath'] = bnPath

    def create_header_widgets(self):
        frm = self._wm['frmHdr']
        #self.chkFsSelAll = Checkbutton(frm, justify=LEFT)
        self.lbFsURL = Label(frm, text = 'URL', width = 32)
        self.lbFsState = Label(frm, text = 'State', width = 8)
        self.lbFsOutput = Label(frm, text = 'Output', width = 32)
        #self.chkFsSelAll.pack(side = LEFT, expand =1, fill = X)
        self.lbFsURL.pack(side = LEFT, expand =1, fill=X)
        self.lbFsState.pack(side = LEFT, expand =1, fill=X)
        self.lbFsOutput.pack(side = LEFT, expand =1, fill=X)


    def create_file_list_widgets(self):
        frmFsList = self._wm['frmFsList']
        lbFs = Listbox(frmFsList, height = 38)
        lbFs.pack(side = LEFT, expand = 1, fill = X)
        frmSbY = self._wm['frmSbY']
        sbY = Scrollbar(frmSbY)
        sbY.pack(side = TOP, expand = 1, fill=Y)
        frmSbX = self._wm['frmSbX']
        sbX = Scrollbar(frmSbX, orient = HORIZONTAL)
        sbX.pack(side = TOP, expand = 1, fill=X)

        self._wm['lbFs'] = lbFs
        self._wm['sbY'] = sbY
        self._wm['sbX'] = sbX

    def create_main_window(self, root):
        # create frames for main window.
        self.create_main_window_frames(root)
        # create path widgets.
        self.create_path_widgets()
        # create header of file list.
        self.create_header_widgets()
        # create file list widghts
        self.create_file_list_widgets()

    def add_file_info(self, url, state, output):
        lbfs = self._wm['lbFs']
        lbfs.insert(END, '%s%s%s' % (url.ljust(64), state.ljust(12), output.ljust(64)))
        #ChkList = Checkbutton(lbfs, text = '%s%s%s' % (url.ljust(64), state.ljust(12), output.ljust(64)))
        #ChkList = Checkbutton(lbfs, text = '%s%s%s' % (url, state, output))
        #ChkList.pack(side = TOP, expand = 1, fill = X)


    def update_file_list_scrollbar(self):
        pass

    def update_file_list(self):
        lbfs = self._wm['lbFs']
        sbY = self._wm['sbY']
        sbX = self._wm['sbX']
        for index in range(100):
            self.add_file_info('https://www.toutiao.com/a1245%d.html' % (1000+index),
                               'Waitting', '/home/yingbin/Dowloads/Pstatp/')
            #lbfs.insert(END, index)
        lbfs['yscrollcommand'] = sbY.set
        sbY['command'] = lbfs.yview
        lbfs['xscrollcommand'] = sbX.set
        sbX['command'] = lbfs.xview
        #self.update_file_list_scrollbar()

    def main(self):
        top = Tk()
        self._wm['top'] = top
        top.title('WebImageCrawler')
        top.geometry('800x640')

        top.resizable(0, 0)
        self.create_menu(top)

        self.create_main_window(top)

        self.update_file_list()

        top.mainloop()

if __name__ == '__main__':
    wm = WebImageCrawlerWindow()
    wm.main()