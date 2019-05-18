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


# import databin

class MainWindow:
    def __init__(self, master, df):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.df = df
        self.btn_new = tk.Button(self.frame, text='New', command=self.open_new_window)
        self.btn_new.pack()
        self.tree = ttk.Treeview(self.frame, columns=tuple(self.df.columns), show='headings')

        self.selected_database = IntVar(self.frame)
        self.selected_database.set(OPTIONS[0])
        self.options_menu = ttk.OptionMenu(self.frame, self.selected_database, *OPTIONS)
        self.options_menu.pack()
        self.selected_database.trace('w', self.change_database)

        for x in df.columns:
            self.tree.heading(x, text=x)
        for index, row in df.iterrows():
            self.tree.insert("", "end", index, values=list(row))
        self.tree.pack()
        self.frame.pack()

    def open_new_window(self):
        self.window_new = tk.Toplevel(self.master)
        self.new_window = NewWindow(self.window_new, self)

    def change_database(self, *args):
        self.tree.destroy()
        self.df = dataframes[self.selected_database.get() - 1]
        self.tree = self.new_tree(self.df)
        self.tree.pack()

    def new_tree(self, df):
        tree = ttk.Treeview(self.frame, columns=tuple(df.columns), show='headings')
        for x in df.columns:
            tree.heading(x, text=x)
        for index, row in df.iterrows():
            tree.insert("", "end", index, values=list(row))
        return tree
    
    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        for x in self.df.columns:
            self.tree.heading(x, text=x)
        for index, row in self.df.iterrows():
            self.tree.insert("", "end", index, values=list(row))


class NewWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.main_window = main_window
        
        tk.Label(self.frame, text='Новая запись в базе данных').grid(row=0, columnspan=2)
        tk.Label(self.frame, text='Имя:').grid(row=1, column=0)
        tk.Label(self.frame, text='Дата выхода:').grid(row=2, column=0)
        tk.Label(self.frame, text='Конфигурация памяти:').grid(row=3, column=0)
        tk.Label(self.frame, text='Энергопотребление').grid(row=4, column=0)
        tk.Label(self.frame, text='Far Cry 5, FPS').grid(row=5, column=0)
        tk.Label(self.frame, text='Fallout 4, FPS').grid(row=6, column=0)
        tk.Label(self.frame, text='The Witcher 3, FPS').grid(row=7, column=0)
        tk.Label(self.frame, text='3DMark Cloud Gate').grid(row=8, column=0)
        tk.Label(self.frame, text='3DMark Fire Strike').grid(row=9, column=0)
        tk.Label(self.frame, text='Средняя цена, руб.').grid(row=10, column=0)
        
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=1, column=1)        
        self.entry_date = tk.Entry(self.frame)
        self.entry_date.grid(row=2, column=1)        
        self.entry_memory = tk.Entry(self.frame)
        self.entry_memory.grid(row=3, column=1)
        self.entry_power = tk.Entry(self.frame)
        self.entry_power.grid(row=4, column=1)
        self.entry_farcry5 = tk.Entry(self.frame)
        self.entry_farcry5.grid(row=5, column=1)
        self.entry_fallout4 = tk.Entry(self.frame)
        self.entry_fallout4.grid(row=6, column=1)
        self.entry_thewitcher3 = tk.Entry(self.frame)
        self.entry_thewitcher3.grid(row=7, column=1)
        self.entry_cloudgate = tk.Entry(self.frame)
        self.entry_cloudgate.grid(row=8, column=1)
        self.entry_firestrike = tk.Entry(self.frame)
        self.entry_firestrike.grid(row=9, column=1)
        self.entry_price = tk.Entry(self.frame)
        self.entry_price.grid(row=10, column=1)
        
        tk.Button(self.frame, text='Добавить', command=self.new_entry).grid(row=11, columnspan=2)
        self.frame.pack()

    def new_entry(self):
        key = (self.entry_name.get(), self.entry_memory.get())
        value = (
                self.entry_name.get(),
                self.entry_date.get(),
                self.entry_memory.get(),
                self.entry_power.get(),
                self.entry_farcry5.get(),
                self.entry_fallout4.get(),
                self.entry_thewitcher3.get(),
                self.entry_cloudgate.get(),
                self.entry_firestrike.get(),
                self.entry_price.get()
                )
        self.main_window.df.index = pd.MultiIndex.from_tuples(self.main_window.df.index)
        self.main_window.df.loc[('df', 'fd'), ['Название', 'Дата выхода', 'Конфигурация памяти', 'Энергопотребление, Вт', 'Far Cry 5, FPS', 'Fallout 4, FPS', 'The Witcher 3, FPS', '3DMark Cloud Gate', '3DMark Fire Strike', 'Средняя цена, ₽']] = ('f', 'f', 'f', 0, 0, 0, 0, 0, 1, 0)
        self.main_window.update_table()


# dataframe = databin.read_from_binary('../Data/data')
df1 = pd.read_csv('../Data/bd1.csv')
df1.index = ([(x, y) for x, y in zip(df1['Название'], df1['Конфигурация памяти'])])
df2 = pd.read_csv('../Data/bd2.csv')
df2.index = (x for x in df2['Название'])
df3 = pd.read_csv('../Data/bd3.csv')
df3.index = (x for x in df3['Название'])
df4 = pd.read_csv('../Data/bd4.csv')
df4.index = (x for x in df4['Название'])
df5 = pd.read_csv('../Data/bd5.csv')
df5.index = (x for x in df5['Название'])

OPTIONS = [1, 2, 3, 4, 5]

dataframes = [df1, df2, df3, df4, df5]


# def change_database(*args):
#    global tree
#    tree.destroy()
#    tree = new_tree(dataframes[selected_database.get() - 1])
#    tree.pack()

def new_entry(name):
    print(name)


# window_new = tk.Tk()
# tk.Label(window_new, text='Новая запись в базе данных').grid(row=0, columnspan=2)
# tk.Label(window_new, text='Имя:').grid(row=1, column=0)
# entry_name = tk.Entry(window_new).grid(row=1, column=1)
# tk.Label(window_new, text='Дата выхода:').grid(row=2, column=0)
# entry_date = tk.Entry(window_new).grid(row=2, column=1)
# tk.Label(window_new, text='Конфигурация памяти:').grid(row=3, column=0)
# entry_memory = tk.Entry(window_new).grid(row=3, column=1)
# tk.Button(window_new, text='Добавить', command=new_entry).grid(row=4, columnspan=2)

def open_new_window():
    window_new.mainloop()


# window = tk.Tk()
#
# btn_new = tk.Button(window, text='New', command=open_new_window).pack()
#
# selected_database = IntVar(window)
# selected_database.set(OPTIONS[0])
# options_menu = ttk.OptionMenu(window, selected_database, *OPTIONS)
# options_menu.pack()
# selected_database.trace('w', change_database)

# tree = ttk.Treeview(window, columns=tuple(df1.columns), show='headings')
# for x in df1.columns:
#    tree.heading(x, text=x)
# for index, row in df1.iterrows():
#    tree.insert("", "end", index, values=list(row))
# tree.pack()


def new_tree(df):
    tree = ttk.Treeview(window, columns=tuple(df.columns), show='headings')
    for x in df.columns:
        tree.heading(x, text=x)
    for index, row in df.iterrows():
        tree.insert("", "end", index, values=list(row))
    return tree


# window.mainloop()

def main():
    root = tk.Tk()
    app = MainWindow(root, df1)
    root.mainloop()


if __name__ == '__main__':
    main()
