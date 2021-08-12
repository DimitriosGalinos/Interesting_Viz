# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:59:55 2020

@author: mitsel
"""

import json
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

with open('EmojiOnlyModel.json') as json_file:
    data = json.load(json_file)

big_list = []
for idx, sub in enumerate(data, start = 0): 
    big_list.append(list(sub.values())) 

feat_list = [item[0] for item in big_list]
emoji_list = [item[2] for item in big_list]

pca = PCA(n_components=2)
my2D = pca.fit_transform(feat_list)

x = my2D[:,0]
y = my2D[:,1]
plt.scatter(x, y)

old_list = [item[2] for item in big_list]
intermediate_emoj = []

for xx in range(len(emoji_list)):
    if '-' in  emoji_list[xx]:
        g =  emoji_list[xx].split('-')
        emoji_list[xx] = int(g[0], 16)
        intermediate_emoj.append(emoji_list[xx])
        old_list[xx] = '#'+g[0]+'60' 
        emoji_list[xx]=chr(emoji_list[xx])
    else:
        emoji_list[xx] = int(emoji_list[xx], 16)
        old_list[xx] = '#'+old_list[xx]+'60'
        intermediate_emoj.append(emoji_list[xx])
        emoji_list[xx]=chr(emoji_list[xx])


import pandas as pd

df = pd.DataFrame(np.transpose(np.array([x,y, emoji_list, intermediate_emoj])),  
                  columns=["1st Principal Component", 
                           "2nd Principal Component",
                           "emojis",
                           "int values"])

color=np.add(x,y)

data2 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")