# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:01:26 2021

@author: mitse
"""
import pandas as pd
import geopandas as gpd

x = pd.read_csv('Full Data World Happines Report - 2018.csv') 
xi = pd.read_csv('Full Data World Happines Report - 2019.csv') 
fdf_2018 = x["Country"].to_frame()
fdf_2018["Happiness score"] = x["Happiness score"]
fdf_2018["Explained by: Healthy life expectancy"] = x["Explained by: Healthy life expectancy"]
fdf_2018["Explained by: GDP per capita"] = x["Explained by: GDP per capita"]
fdf_2018["Explained by: Social support"] = x["Explained by: Social support"]
fdf_2018["Explained by: Generosity"] = x["Explained by: Generosity"]
fdf_2018["Explained by: Perceptions of corruption"] = x["Explained by: Perceptions of corruption"]
fdf_2018["Explained by: Freedom to make life choices"] = x["Explained by: Freedom to make life choices"]
fdf_2019 = xi["Country"].to_frame().dropna()
fdf_2019["Happiness score"] = xi["Happiness score"]
fdf_2019["Explained by: Healthy life expectancy"] = xi["Explained by: Healthy life expectancy"]
fdf_2019["Explained by: GDP per capita"] = xi["Explained by: GDP per capita"]
fdf_2019["Explained by: Social support"] = xi["Explained by: Social support"]
fdf_2019["Explained by: Generosity"] = xi["Explained by: Generosity"]
fdf_2019["Explained by: Perceptions of corruption"] = xi["Explained by: Perceptions of corruption"]
fdf_2019["Explained by: Freedom to make life choices"] = xi["Explained by: Freedom to make life choices"]

fdf_2019.at[37,"Country"] ="Trinidad and Tobago"
fdf_2019.at[57,"Country"] ="North Cyprus"
fdf_2019.at[75,"Country"] = "Hong Kong S.A.R. of China"

my_emoji_scale = ["🥳","😍","😁","🙂","😐","🙁","😰","💩", "☠️"]

counter = 0
emoji = 0
fdf_2019["emoji"]=fdf_2019["Country"]
fdf_2018["emoji"]=fdf_2018["Country"]
fdf_2019["display"]=fdf_2019["Country"]
fdf_2018["display"]=fdf_2018["Country"]
for zz in range(len(fdf_2018)):
    if counter == 17:
        if emoji < 8:
            emoji = emoji+1
        counter = 0
    fdf_2018.at[zz, "emoji"]=my_emoji_scale[emoji]
    fdf_2019.at[zz, "emoji"]=my_emoji_scale[emoji]
    fdf_2018.at[zz, "display"]=str(fdf_2018.at[zz, "Country"])+" | "+str(fdf_2018.at[zz, "Happiness score"])
    fdf_2019.at[zz, "display"]=str(fdf_2019.at[zz, "Country"])+" | "+str(fdf_2019.at[zz, "Happiness score"])
    counter = counter + 1
    
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

reg = LinearRegression().fit(fdf_2018['Happiness score'].to_numpy().reshape(-1, 1), fdf_2018['Explained by: GDP per capita'].to_numpy().reshape(-1, 1))
x_range = np.linspace(fdf_2018['Happiness score'].min(), fdf_2018['Happiness score'].max(), 100)
y_range = reg.predict(x_range.reshape(-1, 1))

fig = go.Figure([go.Scatter(x=fdf_2018['Happiness score'],
                                y=fdf_2018['Explained by: GDP per capita'],
                                mode='markers+text',
                                textposition="bottom center",
                                marker_color=fdf_2018['Happiness score'],
                                text=fdf_2018['Country']),
                go.Scatter(x=x_range, y=y_range, name='prediction')]) # hover text goes here

fig.update_layout(title='GPD per capita / happiness',
                  yaxis_title="GPD per capita contribution",
                  xaxis_title="Happiness score")
fig.show()

import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))

fig.show()

y_range=np.append([], y_range)
cv = fdf_2018.loc[fdf_2018.Country == 'Qatar','Happiness score'].values[0]