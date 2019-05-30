# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:56:35 2019

@author: QiotoF
"""

import sys

import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from tkinter import IntVar

sys.path.append('../Library/')


def sortby(tree, col, descending):
    def sortSecond(val):
        return val[1]

    def change_numeric(data):
        return [(int(x[0]), x[1]) for x in data]

    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    if data[0][0].isdigit():
        data = change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))


def open_edit_window():
    global df

    def edit_entry():
        if selected_database.get() == 1:
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
            df.loc[(entry['Название'], int(entry['Конфигурация памяти, ГБ'])), list(df.columns)] = [entry[x] for x in
                                                                                                    df.columns]
        elif selected_database.get() == 2:
            values = [entry_name.get(), entry_arch.get()]
            for index in df.index:
                if df.loc[index]['Название'] == key:
                    df.loc[index, 'Архитектура'] = values[1]
        elif selected_database.get() == 3:
            values = [entry_name.get(), entry_sli.get()]
            for index in df.index:
                if df.loc[index]['Название'] == key:
                    df.loc[index, 'NVIDIA SLI'] = values[1]
        elif selected_database.get() == 4:
            # keys = ['Название', 'Архитектура']
            values = [entry_name.get(), entry_rtx.get()]
            for index in df.index:
                if df.loc[index]['Название'] == key:
                    df.loc[index, 'RTX'] = values[1]
        elif selected_database.get() == 5:
            # keys = ['Название', 'Архитектура']
            values = [entry_name.get(), entry_freq.get()]
            for index in df.index:
                if df.loc[index]['Название'] == key:
                    df.loc[index, 'Базовая тактовая частота, МГц'] = values[1]

        update_table()
        window_edit.destroy()

    entry = tree.focus()
    window_edit = tk.Toplevel(window)

    if selected_database.get() == 1:
        if '{' in entry:
            y = entry.split('}')
            k1 = y[0][1:]
            x2 = y[1].split(' ')
            k2 = int(float(x2[2]))
        else:
            y = entry.split(' ')
            k1 = y[0]
            k2 = y[2]
        key = (k1, int(k2))
        tk.Label(window_edit, text='Новая запись в базе данных').grid(row=0, columnspan=2)
        tk.Label(window_edit, text='Имя:').grid(row=1, column=0)
        tk.Label(window_edit, text='Дата выхода:').grid(row=2, column=0)
        tk.Label(window_edit, text='Конфигурация памяти, ГБ:').grid(row=3, column=0)
        tk.Label(window_edit, text='Энергопотребление').grid(row=4, column=0)
        tk.Label(window_edit, text='Far Cry 5, FPS').grid(row=5, column=0)
        tk.Label(window_edit, text='Fallout 4, FPS').grid(row=6, column=0)
        tk.Label(window_edit, text='The Witcher 3, FPS').grid(row=7, column=0)
        tk.Label(window_edit, text='3DMark Cloud Gate').grid(row=8, column=0)
        tk.Label(window_edit, text='3DMark Fire Strike').grid(row=9, column=0)
        tk.Label(window_edit, text='Средняя цена, руб.').grid(row=10, column=0)
        tk.Label(window_edit, text='Архитектура').grid(row=11, column=0)
        tk.Label(window_edit, text='NVIDIA SLI').grid(row=12, column=0)
        tk.Label(window_edit, text='RTX').grid(row=13, column=0)
        tk.Label(window_edit, text='Базовая тактовая частота').grid(row=14, column=0)

        entry_name = tk.Entry(window_edit)
        entry_name.insert(0, df.loc[key]['Название'])
        entry_name.grid(row=1, column=1)
        entry_date = tk.Entry(window_edit)
        entry_date.insert(0, df.loc[key]['Дата выхода'])
        entry_date.grid(row=2, column=1)
        entry_memory = tk.Entry(window_edit)
        entry_memory.insert(0, df.loc[key]['Конфигурация памяти, ГБ'])
        entry_memory.grid(row=3, column=1)
        entry_power = tk.Entry(window_edit)
        entry_power.insert(0, df.loc[key]['Энергопотребление, Вт'])
        entry_power.grid(row=4, column=1)
        entry_farcry5 = tk.Entry(window_edit)
        entry_farcry5.insert(0, df.loc[key]['Far Cry 5, FPS'])
        entry_farcry5.grid(row=5, column=1)
        entry_fallout4 = tk.Entry(window_edit)
        entry_fallout4.insert(0, df.loc[key]['Fallout 4, FPS'])
        entry_fallout4.grid(row=6, column=1)
        entry_thewitcher3 = tk.Entry(window_edit)
        entry_thewitcher3.insert(0, df.loc[key]['The Witcher 3, FPS'])
        entry_thewitcher3.grid(row=7, column=1)
        entry_cloudgate = tk.Entry(window_edit)
        entry_cloudgate.insert(0, df.loc[key]['3DMark Cloud Gate'])
        entry_cloudgate.grid(row=8, column=1)
        entry_firestrike = tk.Entry(window_edit)
        entry_firestrike.insert(0, df.loc[key]['3DMark Fire Strike'])
        entry_firestrike.grid(row=9, column=1)
        entry_price = tk.Entry(window_edit)
        entry_price.insert(0, df.loc[key]['Средняя цена, ₽'])
        entry_price.grid(row=10, column=1)
        entry_arch = tk.Entry(window_edit)
        entry_arch.insert(0, df.loc[key]['Архитектура'])
        entry_arch.grid(row=11, column=1)
        entry_sli = tk.Entry(window_edit)
        entry_sli.insert(0, df.loc[key]['NVIDIA SLI'])
        entry_sli.grid(row=12, column=1)
        entry_rtx = tk.Entry(window_edit)
        entry_rtx.insert(0, df.loc[key]['RTX'])
        entry_rtx.grid(row=13, column=1)
        entry_freq = tk.Entry(window_edit)
        entry_freq.insert(0, df.loc[key]['Базовая тактовая частота, МГц'])
        entry_freq.grid(row=14, column=1)
        tk.Button(window_edit, text='Ok', command=edit_entry).grid(row=15, columnspan=2)
    else:
        if '{' in entry:
            key = entry.split('}')[0][1:]
        else:
            key = entry.split(' ')[0]
        for index in df.index:
            if df.loc[index]['Название'] == key:
                name = df.loc[index]['Название']
                arch = df.loc[index]['Архитектура']
                sli = df.loc[index]['NVIDIA SLI']
                rtx = df.loc[index]['RTX']
                freq = df.loc[index]['Базовая тактовая частота, МГц']
        if selected_database.get() == 2:
            tk.Label(window_edit, text='Имя:').grid(row=1, column=0)
            tk.Label(window_edit, text='Архитектура').grid(row=2, column=0)
            entry_name = tk.Entry(window_edit)
            entry_name.insert(0, name)
            entry_name.grid(row=1, column=1)
            entry_arch = tk.Entry(window_edit)
            entry_arch.insert(0, arch)
            entry_arch.grid(row=2, column=1)
            tk.Button(window_edit, text='Ok', command=edit_entry).grid(row=3, columnspan=2)
        elif selected_database.get() == 3:
            tk.Label(window_edit, text='Имя:').grid(row=1, column=0)
            tk.Label(window_edit, text='NVIDIA SLI').grid(row=2, column=0)
            entry_name = tk.Entry(window_edit)
            entry_name.insert(0, name)
            entry_name.grid(row=1, column=1)
            entry_sli = tk.Entry(window_edit)
            entry_sli.insert(0, sli)
            entry_sli.grid(row=2, column=1)
            tk.Button(window_edit, text='Ok', command=edit_entry).grid(row=3, columnspan=2)
        elif selected_database.get() == 4:
            tk.Label(window_edit, text='Имя:').grid(row=1, column=0)
            tk.Label(window_edit, text='RTX').grid(row=2, column=0)
            entry_name = tk.Entry(window_edit)
            entry_name.insert(0, name)
            entry_name.grid(row=1, column=1)
            entry_rtx = tk.Entry(window_edit)
            entry_rtx.insert(0, rtx)
            entry_rtx.grid(row=2, column=1)
            tk.Button(window_edit, text='Ok', command=edit_entry).grid(row=3, columnspan=2)
        elif selected_database.get() == 5:
            tk.Label(window_edit, text='Имя:').grid(row=1, column=0)
            tk.Label(window_edit, text='Базовая тактовая частота, МГц').grid(row=2, column=0)
            entry_name = tk.Entry(window_edit)
            entry_name.insert(0, name)
            entry_name.grid(row=1, column=1)
            entry_freq = tk.Entry(window_edit)
            entry_freq.insert(0, freq)
            entry_freq.grid(row=2, column=1)
            tk.Button(window_edit, text='Ok', command=edit_entry).grid(row=3, columnspan=2)


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
        df.loc[(entry['Название'], int(entry['Конфигурация памяти, ГБ'])), list(df.columns)] = [entry[x] for x in
                                                                                                df.columns]
        update_table()
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


def update_table(*args):
    global tree
    tree.destroy()
    arg = make_list(df)
    tree = new_tree(arg[0], arg[1])
    tree.grid(row=1, columnspan=4)


def new_tree(col, l):
    tree = ttk.Treeview(window, columns=col, show='headings')
    for x in col:
        tree.column(x, width=int(tkFont.Font().measure(x) / 1.2))
        tree.heading(x, text=x, command=lambda c=x: sortby(tree, c, 0))
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
    update_table()


df = pd.read_csv('../Data/bd.csv')
df.index = ([(x, y) for x, y in zip(df['Название'], df['Конфигурация памяти, ГБ'])])
df.index = pd.MultiIndex.from_tuples(df.index)
OPTIONS = [0, 1, 2, 3, 4, 5]

window = tk.Tk()

canvas = tk.Canvas(window, height=100, width=100)
background_image = tk.PhotoImage(file='../Graphics/background.png')
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.grid(row=0, column=0, columnspan=2)

btn_new = tk.Button(window, text='New', command=open_new_window, activebackground='#76b900', activeforeground='#1A1918',
                    bg='#1A1918', fg='#76b900', font=('Roboto', 12, 'bold'))
btn_new.grid(row=0, column=0, sticky='WN', padx=5, pady=5)
btn_delete = tk.Button(window, text='Delete', command=delete_entries, activebackground='#76b900',
                       activeforeground='#1A1918',
                       bg='#1A1918', fg='#76b900', font=('Roboto', 12, 'bold'))
btn_delete.grid(row=0, column=1, sticky='WN', pady=5)
#btn_edit = tk.Button(window, text='Edit', command=open_edit_window)
#btn_edit.grid(row=0, column=5)

frame = tk.Frame(window, height=1, width=1200)
frame.grid(column=3)

tree = ttk.Treeview(window, show='headings')
vsb = ttk.Scrollbar(orient="vertical",
                    command=tree.yview)
hsb = ttk.Scrollbar(orient="horizontal",
                    command=tree.xview)
tree.configure(yscrollcommand=vsb.set,
               xscrollcommand=hsb.set)
vsb.grid(row=1, column=5)
hsb.grid(row=2, columnspan=10)
tree.grid(row=1, column=0, columnspan=30)
# tree.pack()

selected_database = IntVar(window)
selected_database.set(OPTIONS[1])
options_menu = ttk.OptionMenu(window, selected_database, *OPTIONS)
#options_menu.grid(row=0, column=5)
selected_database.trace('w', update_table)
update_table()

window.mainloop()
