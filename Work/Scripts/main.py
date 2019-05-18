# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:56:35 2019

@author: QiotoF
"""

import sys
sys.path.append('../Library/')

import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import IntVar
#import databin

#dataframe = databin.read_from_binary('../Data/data')
df1 = pd.read_csv('../Data/bd1.csv')
df1.index=([(x, y) for x, y in zip(df1['Название'], df1['Конфигурация памяти'])])
df2 = pd.read_csv('../Data/bd2.csv')
df2.index=(x for x in df2['Название'])
df3 = pd.read_csv('../Data/bd3.csv')
df3.index=(x for x in df3['Название'])
df4 = pd.read_csv('../Data/bd4.csv')
df4.index=(x for x in df4['Название'])
df5 = pd.read_csv('../Data/bd5.csv')
df5.index=(x for x in df5['Название'])

OPTIONS = [1, 2, 3, 4, 5] 

dataframes = [df1, df2, df3, df4, df5]



window = tk.Tk()

tree = ttk.Treeview(window, columns=tuple(df1.columns), show='headings')
for x in df1.columns:
    tree.heading(x, text=x)
for index, row in df1.iterrows():
    tree.insert("", "end", index, values=list(row))
tree.pack()

def open_new_window():
    window_new = tk.Toplevel(window)
    
    
btn_new = tk.Button(window, text='New', command=open_new_window)
btn_new.pack()



def change_database(*args):
    global tree
    tree.destroy()
    tree = new_tree(dataframes[selected_database.get() - 1])
    tree.pack()
    
selected_database = IntVar(window)
selected_database.set(OPTIONS[0])
options_menu = ttk.OptionMenu(window, selected_database, *OPTIONS)
options_menu.pack()
selected_database.trace('w', change_database)

def new_tree(df):
    tree = ttk.Treeview(window, columns=tuple(df.columns), show='headings')
    for x in df.columns:
        tree.heading(x, text=x)
    for index, row in df.iterrows():
        tree.insert("", "end", index, values=list(row))
    return tree

window.mainloop()