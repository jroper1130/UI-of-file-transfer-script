'''
Python Drill: PyDrill_gui_34_idle
Title: UI for File Transfer project - Python 3.4 - IDLE
Scenario: You recently created a script that will check a folder for new or
modified files, and then copy those new or modified files to another location.
Users are asking for a user interface to make using the script easier and more
versatile. Desired features of the UI:
 Allow the user to browse to and choose a specific folder that will contain the
files to be checked daily.
 Allow the user to browse to and choose a specific folder that will receive the
copied files.
 Allow the user to manually initiate the 'file check' process that is performed by
the script.
You have been asked to create this UI.
Guidelines:
 Use Python 3.4 for this drill.
 Use tkinter to create the UI.
 The layout of the UI is up to you.
 You should use IDLE for this Drill.
Once you create a functioning program that is approved by your instructor,
save it for later use. Do not modify this saved copy during subsequent drills
'''
#drill7
from tkinter import *
from tkinter import filedialog
import tkinter as tk

import File_transfer

root= Tk()


def src_files():
    src_filename =  filedialog.askdirectory()
    return src_filename
def des_files():
    des_filename =  filedialog.askdirectory()
    return des_filename
    
#btn for previous script
btn_ck = tk.Button(text='File Transfer',command= File_transfer.f_transfer).grid(row = 3, column = 3, padx = 5, pady = 5)
#btns for above functions
btn_src = tk.Button(text='Choose file to send out',command= src_files).grid(row = 2, column = 2, padx = 5, pady = 5)
btn_des = tk.Button(text='Choose file to send to',command= des_files).grid(row = 2, column = 4, padx = 5, pady = 5)
               
#just need to turn in

