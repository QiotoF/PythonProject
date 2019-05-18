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

data_frames = [df1, df2, df3, df4, df5]


class MainWindow:
    def __init__(self, master):

        self.OPTIONS = [0, 1, 2, 3, 4, 5]

        self.df = df1

        self.master = master
        self.frame = tk.Frame(self.master)
        self.btn_new = tk.Button(self.frame, text='New', command=self.open_new_window)
        self.btn_new.pack()

        self.selected_database = IntVar(self.frame)
        self.selected_database.set(self.OPTIONS[1])
        self.options_menu = ttk.OptionMenu(self.frame, self.selected_database, *self.OPTIONS)
        self.options_menu.pack()
        self.selected_database.trace('w', self.change_database)

        self.tree = self.new_tree(self.df)

        self.tree.pack()
        self.frame.pack()

    def insert_new_entry(self, entry):
        df1.index = pd.MultiIndex.from_tuples(df1.index)
        df1.loc[
            (entry['Название'], entry['Конфигурация памяти']), ['Название', 'Дата выхода', 'Конфигурация памяти',
                                                                'Энергопотребление, Вт',
                                                                'Far Cry 5, FPS',
                                                                'Fallout 4, FPS', 'The Witcher 3, FPS',
                                                                '3DMark Cloud Gate', '3DMark Fire Strike',
                                                                'Средняя цена, ₽']] = (
            entry['Название'], entry['Дата выхода'], entry['Конфигурация памяти'], entry['Энергопотребление, Вт'],
            entry['Far Cry 5, FPS'], entry['Fallout 4, FPS'],
            entry['The Witcher 3, FPS'], entry['3DMark Cloud Gate'],
            entry['3DMark Fire Strike'], entry['Средняя цена, ₽'])
        df2.loc[entry['Название'], ['Название', 'Архитектура']] = (entry['Название'], entry['Архитектура'])
        df3.loc[entry['Название'], ['Название', 'NVIDIA SLI']] = (entry['Название'], entry['NVIDIA SLI'])
        df4.loc[entry['Название'], ['Название', 'RTX']] = (entry['Название'], entry['RTX'])
        df5.loc[entry['Название'], ['Название', 'Базовая тактовая частота, МГц']] = (
            entry['Название'], entry['Базовая тактовая частота, МГц'])
        self.update_table()

    def open_new_window(self):
        self.window_new = tk.Toplevel(self.master)
        self.new_window = NewWindow(self.window_new, self)

    def change_database(self, *args):
        self.tree.destroy()
        self.df = data_frames[self.selected_database.get() - 1]
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
        tk.Label(self.frame, text='Архитектура').grid(row=11, column=0)
        tk.Label(self.frame, text='NVIDIA SLI').grid(row=12, column=0)
        tk.Label(self.frame, text='RTX').grid(row=13, column=0)
        tk.Label(self.frame, text='Базовая тактовая частота, МГц').grid(row=14, column=0)

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
        self.entry_arch = tk.Entry(self.frame)
        self.entry_arch.grid(row=11, column=1)
        self.entry_sli = tk.Entry(self.frame)
        self.entry_sli.grid(row=12, column=1)
        self.entry_rtx = tk.Entry(self.frame)
        self.entry_rtx.grid(row=13, column=1)
        self.entry_freq = tk.Entry(self.frame)
        self.entry_freq.grid(row=14, column=1)

        tk.Button(self.frame, text='Добавить', command=self.new_entry).grid(row=15, columnspan=2)
        self.frame.pack()

    def new_entry(self):
        keys = ['Название', 'Дата выхода', 'Конфигурация памяти', 'Энергопотребление, Вт', 'Far Cry 5, FPS',
                'Fallout 4, FPS', 'The Witcher 3, FPS', '3DMark Cloud Gate', '3DMark Fire Strike',
                'Средняя цена, ₽', 'Архитектура', 'NVIDIA SLI', 'RTX', 'Базовая тактовая частота, МГц']
        values = [
            self.entry_name.get(),
            self.entry_date.get(),
            self.entry_memory.get(),
            self.entry_power.get(),
            self.entry_farcry5.get(),
            self.entry_fallout4.get(),
            self.entry_thewitcher3.get(),
            self.entry_cloudgate.get(),
            self.entry_firestrike.get(),
            self.entry_price.get(),
            self.entry_arch.get(),
            self.entry_sli.get(),
            self.entry_rtx.get(),
            self.entry_freq.get()
        ]
        entry = dict(zip([x for x in keys], [y for y in values]))
        self.main_window.insert_new_entry(entry)
        self.master.destroy()


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
