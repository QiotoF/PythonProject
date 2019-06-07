# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:56:51 2019

@author: QiotoF
"""
import numpy as np
from tkinter.messagebox import showinfo


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
    file = open('../Output/output.txt', 'w')
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
    showinfo("Успешно!", "Отчёт сохранён в папке Output!")
