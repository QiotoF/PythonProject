# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:53:30 2019

@author: QiotoF
"""
import pickle


def write_to_binary(dataframe, filename):
    outfile = open(filename, 'wb')
    pickle.dump(dataframe, outfile)
    outfile.close()


def read_from_binary(filename):
    infile = open(filename, 'rb')
    dataframe = pickle.load(infile)
    infile.close()
    return dataframe
