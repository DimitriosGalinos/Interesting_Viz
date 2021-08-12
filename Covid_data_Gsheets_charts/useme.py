# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:40:08 2020

@author: mitsel
"""
import numpy as np
import pandas as pd

# Reading our data sets
data=pd.read_csv('covid_cases.csv', delimiter = ',', header=None)
data=np.array(data)

march_data = np.empty((0,12))
october_data = np.empty((0,12))

for xx in range(56149):
    if data[xx, 2] == '3':
#        print(data(xx))
        march_data=np.append(march_data, [data[xx]], axis=0)
    elif data[xx, 2] == '10':
        october_data=np.append(october_data, [data[xx]], axis=0)


death_max_march=np.max(march_data[:,5].astype(np.int64))
death_max_october=np.max(october_data[:,5].astype(np.int64))
cases_max_march=np.max(march_data[:,4].astype(np.int64))
cases_max_october=np.max(october_data[:,4].astype(np.int64))


