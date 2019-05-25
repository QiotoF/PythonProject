# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:56:35 2019

@author: QiotoF
"""

import sys

import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import IntVar

sys.path.append('../Library/')


def open_new_window():
    def new_entry():
        keys = ['Название', 'Дата выхода', 'Конфигурация памяти, ГБ', 'Энергопотребление, Вт', 'Far Cry 5, FPS',
                'Fallout 4, FPS', 'The Witcher 3, FPS', '3DMark Cloud Gate', '3DMark Fire Strike',
                'Средняя цена, ₽', 'Архитектура', 'NVIDIA SLI', 'RTX', 'Базовая тактовая частота, МГц']
        values = [
            entry_name.get(),
            entry_date.get(),
            entry_memory.get(),
            entry_power.get(),
            entry_farcry5.get(),
            entry_fallout4.get(),
            entry_thewitcher3.get(),
            entry_cloudgate.get(),
            entry_firestrike.get(),
            entry_price.get(),
            entry_arch.get(),
            entry_sli.get(),
            entry_rtx.get(),
            entry_freq.get()
        ]
        entry = dict(zip([x for x in keys], [y for y in values]))
        df.loc[(entry['Название'], int(entry['Конфигурация памяти, ГБ'])), list(df.columns)] = [entry[x] for x in df.columns]
        change_database()
        window_new.destroy()

    window_new = tk.Toplevel(window)
    tk.Label(window_new, text='Новая запись в базе данных').grid(row=0, columnspan=2)
    tk.Label(window_new, text='Имя:').grid(row=1, column=0)
    tk.Label(window_new, text='Дата выхода:').grid(row=2, column=0)
    tk.Label(window_new, text='Конфигурация памяти, ГБ:').grid(row=3, column=0)
    tk.Label(window_new, text='Энергопотребление').grid(row=4, column=0)
    tk.Label(window_new, text='Far Cry 5, FPS').grid(row=5, column=0)
    tk.Label(window_new, text='Fallout 4, FPS').grid(row=6, column=0)
    tk.Label(window_new, text='The Witcher 3, FPS').grid(row=7, column=0)
    tk.Label(window_new, text='3DMark Cloud Gate').grid(row=8, column=0)
    tk.Label(window_new, text='3DMark Fire Strike').grid(row=9, column=0)
    tk.Label(window_new, text='Средняя цена, руб.').grid(row=10, column=0)
    tk.Label(window_new, text='Архитектура').grid(row=11, column=0)
    tk.Label(window_new, text='NVIDIA SLI').grid(row=12, column=0)
    tk.Label(window_new, text='RTX').grid(row=13, column=0)
    tk.Label(window_new, text='Базовая тактовая частота').grid(row=14, column=0)

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
    entry_arch = tk.Entry(window_new)
    entry_arch.grid(row=11, column=1)
    entry_sli = tk.Entry(window_new)
    entry_sli.grid(row=12, column=1)
    entry_rtx = tk.Entry(window_new)
    entry_rtx.grid(row=13, column=1)
    entry_freq = tk.Entry(window_new)
    entry_freq.grid(row=14, column=1)
    tk.Button(window_new, text='Добавить', command=new_entry).grid(row=15, columnspan=2)


def make_list(df):
    if selected_database.get() == 2:
        col = ('Название', 'Архитектура')
        s = list(set([(x, y) for x, y in zip(df['Название'], df['Архитектура'])]))
    elif selected_database.get() == 3:
        col = ('Название', 'NVIDIA SLI')
        s = list(set([(x, y) for x, y in zip(df['Название'], df['NVIDIA SLI'])]))
    elif selected_database.get() == 4:
        col = ('Название', 'RTX')
        s = list(set([(x, y) for x, y in zip(df['Название'], df['RTX'])]))
    elif selected_database.get() == 5:
        col = ('Название', 'Базовая тактовая частота, МГц')
        s = list(set([(x, y) for x, y in zip(df['Название'], df['Базовая тактовая частота, МГц'])]))
    else:
        col = [
            'Название', 'Дата выхода', 'Конфигурация памяти, ГБ', 'Энергопотребление, Вт', 'Far Cry 5, FPS',
            'Fallout 4, FPS',
            'The Witcher 3, FPS', '3DMark Cloud Gate', '3DMark Fire Strike', 'Средняя цена, ₽']
        s = list(
            [[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10] for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 in zip(df[col[0]],
                                                                                                          df[col[1]],
                                                                                                          df[col[2]],
                                                                                                          df[col[3]],
                                                                                                          df[col[4]],
                                                                                                          df[col[5]],
                                                                                                          df[col[6]],
                                                                                                          df[col[7]],
                                                                                                          df[col[8]],
                                                                                                          df[col[9]])])
    return col, s


def change_database(*args):
    global tree
    tree.destroy()
    arg = make_list(df)
    tree = new_tree(arg[0], arg[1])
    tree.pack()
    window.update()

def new_tree(col, l):
    tree = ttk.Treeview(window, columns=col, show='headings')
    for x in col:
        tree.heading(x, text=x)
    for x in l:
        tree.insert("", "end", x, values=x)
    return tree


def delete_entries():
    global df
    entries = tree.selection()
    if selected_database.get() == 1:
        for x in entries:
            if '{' in x:
                y = x.split('}')
                k1 = y[0][1:]
                x2 = y[1].split(' ')
                k2 = int(float(x2[2]))
            else:
                y = x.split(' ')
                k1 = y[0]
                k2 = y[2]
            print(k1, k2)
            df = df.drop((k1, int(k2)))
    else:
        for x in entries:
            if '{' in x:
                key = x.split('}')[0][1:]

            else:
                key = x.split(' ')[0]
            for index in df.index:
                if df.loc[index]['Название'] == key:
                    df = df.drop(index)
    change_database()


df = pd.read_csv('../Data/bd.csv')
df.index = ([(x, y) for x, y in zip(df['Название'], df['Конфигурация памяти, ГБ'])])
df.index = pd.MultiIndex.from_tuples(df.index)
OPTIONS = [0, 1, 2, 3, 4, 5]
window = tk.Tk()
tree = ttk.Treeview(window, show='headings')
tree.pack()
btn_new = tk.Button(window, text='New', command=open_new_window)
btn_new.pack()
btn_delete = tk.Button(window, text='Delete', command=delete_entries)
btn_delete.pack()
selected_database = IntVar(window)
selected_database.set(OPTIONS[1])
options_menu = ttk.OptionMenu(window, selected_database, *OPTIONS)
options_menu.pack()
selected_database.trace('w', change_database)
change_database()

window.mainloop()
