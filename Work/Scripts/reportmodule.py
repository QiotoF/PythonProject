# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:56:51 2019

@author: QiotoF
"""
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
import pylab as plb
import numpy as np
from params import *
power = 'Энергопотребление, Вт'
arch = 'Архитектура'


def bar_plot(df):
    plt.figure(figsize=(20, 5))
    plb.bar(df.loc[:, 'Название'], df.loc[:, power], align='center', label=power)
    plb.legend()
    plt.ylabel(power)
    plt.savefig(BAR_PLOT_ADDRESS)


def hist_plot(df):
    plt.figure(figsize=(20, 5))
    d = df.loc[:, power]
    d.hist(bins=50)
    plt.ylabel('Количетво')
    plt.xlabel(power)
    plb.savefig(HIST_PLOT_ADDRESS)


def box_plot(df):
    plt.figure(figsize=(20, 5))
    d = df.loc[:, power]
    plt.boxplot(d, notch=True, patch_artist=True)
    plt.ylabel(power)
    plb.savefig(BOX_PLOT_ADDRESS)


def scatter_plot(df):
    area = np.pi * 3
    plt.figure(figsize=(10, 5))
    plt.scatter(df.loc[:, 'Конфигурация памяти, ГБ'], df.loc[:, 'Fallout 4, FPS'], s=area)
    plt.ylabel('Fallout 4, FPS')
    plt.xlabel('Конфигурация памяти, ГБ')
    plb.savefig(SCATTER_PLOT_ADDRESS)


def report(df):
    entries_count = len(df.index)
    memory_avg = round(np.average(df['Конфигурация памяти, ГБ']), 2)
    memory_disp = round(np.var(df['Конфигурация памяти, ГБ']), 2)
    power_avg = round(np.average(df['Энергопотребление, Вт']), 2)
    power_disp = round(np.var(df['Энергопотребление, Вт']), 2)
    farcry5_avg = round(np.average(df['Far Cry 5, FPS']), 2)
    farcry5_disp = round(np.var(df['Far Cry 5, FPS']), 2)
    fallout4_avg = round(np.average(df['Fallout 4, FPS']), 2)
    fallout4_disp = round(np.var(df['Fallout 4, FPS']), 2)
    witcher3_avg = round(np.average(df['The Witcher 3, FPS']), 2)
    witcher3_disp = round(np.var(df['The Witcher 3, FPS']), 2)
    cloudgate_avg = round(np.average(df['3DMark Cloud Gate']), 2)
    cloudgate_disp = round(np.var(df['3DMark Cloud Gate']), 2)
    firestrike_avg = round(np.average(df['3DMark Fire Strike']), 2)
    firestrike_disp = round(np.var(df['3DMark Fire Strike']), 2)
    file = open(TEXT_REPORT_ADDRESS, 'w')
    file.write('Количество записей: ' + str(entries_count) + '\n')
    file.write('Среднее значение памяти: ' + str(memory_avg) + '\n')
    file.write('Дисперсия памяти: ' + str(memory_disp) + '\n')
    file.write('Среднее значение энергопотребления: ' + str(power_avg) + '\n')
    file.write('Дисперсия энергопотребления: ' + str(power_disp) + '\n')
    file.write('Среднее значение FPS в Far Cry 5: ' + str(farcry5_avg) + '\n')
    file.write('Дисперсия FPS в Far Cry 5: ' + str(farcry5_disp) + '\n')
    file.write('Среднее значение FPS в Fallout 4: ' + str(fallout4_avg) + '\n')
    file.write('Дисперсия FPS в Fallout 4: ' + str(fallout4_disp) + '\n')
    file.write('Среднее значение FPS в The Witcher 3: ' + str(witcher3_avg) + '\n')
    file.write('Дисперсия FPS в The Witcher 3: ' + str(witcher3_disp) + '\n')
    file.write('Среднее значение 3DMark Cloud Gate: ' + str(cloudgate_avg) + '\n')
    file.write('Дисперсия 3DMark Cloud Gate: ' + str(cloudgate_disp) + '\n')
    file.write('Среднее значение 3DMark Fire Strike: ' + str(firestrike_avg) + '\n')
    file.write('Дисперсия 3DMark Fire Strike: ' + str(firestrike_disp) + '\n')
    file.close()
    bar_plot(df)
    hist_plot(df)
    box_plot(df)
    scatter_plot(df)
    showinfo("Успешно!", "Отчёт сохранён в папке Output!")


