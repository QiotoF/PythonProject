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
    tk.Label(window_new, text='Новая запись в базе данных').grid(row=0, columnspan=2)
    tk.Label(window_new, text='Имя:').grid(row=1, column=0)
    tk.Label(window_new, text='Дата выхода:').grid(row=2, column=0)
    tk.Label(window_new, text='Конфигурация памяти:').grid(row=3, column=0)
    tk.Label(window_new, text='Энергопотребление').grid(row=4, column=0)
    tk.Label(window_new, text='Far Cry 5, FPS').grid(row=5, column=0)
    tk.Label(window_new, text='Fallout 4, FPS').grid(row=6, column=0)
    tk.Label(window_new, text='The Witcher 3, FPS').grid(row=7, column=0)
    tk.Label(window_new, text='3DMark Cloud Gate').grid(row=8, column=0)
    tk.Label(window_new, text='3DMark Fire Strike').grid(row=9, column=0)
    tk.Label(window_new, text='Средняя цена, руб.').grid(row=10, column=0)
        
    entry_name = tk.Entry(window_new)
    entry_name.grid(row=1, column=1)        
    entry_date = tk.Entry(window_new)
    entry_date.grid(row=2, column=1)        
    entry_memory = tk.Entry(window_new)
    entry_memory.grid(row=3, column=1)
    entry_power = tk.Entry(window_new)
    entry_power.grid(row=4, column=1)
    entry_farcry5 = tk.Entry(window_new)
    entry_farcry5.grid(row=5, column=1)
    entry_fallout4 = tk.Entry(window_new)
    entry_fallout4.grid(row=6, column=1)
    entry_thewitcher3 = tk.Entry(window_new)
    entry_thewitcher3.grid(row=7, column=1)
    entry_cloudgate = tk.Entry(window_new)
    entry_cloudgate.grid(row=8, column=1)
    entry_firestrike = tk.Entry(window_new)
    entry_firestrike.grid(row=9, column=1)
    entry_price = tk.Entry(window_new)
    entry_price.grid(row=10, column=1)
        
    tk.Button(window_new, text='Добавить').grid(row=11, columnspan=2)
    
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