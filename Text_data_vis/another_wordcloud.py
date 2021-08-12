# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:19:48 2020

@author: mitsel
"""
# Import packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

with open("My_Thesis_edit.txt", "r") as file:
    dracula_text = file.read().replace('\n', ' ')
dracula_text = dracula_text.replace("  ", ' ')
dracula_text = dracula_text.replace("\t", ' ')
dracula_text = dracula_text.replace("\n", ' ')

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(100, 80))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");
    
import numpy as np
from PIL import Image
# Import image to np.array
mask = np.array(Image.open('16.png'))
# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, 
                      background_color='white', colormap='nipy_spectral', 
                      #color_func=lambda *args, **kwargs: "black",
                      collocations=False, stopwords = STOPWORDS, 
                      mask=mask).generate(dracula_text)
# Plot
plot_cloud(wordcloud)
"""
from matplotlib.colors import ListedColormap

a = 0.5

# Get the colormap colors, multiply them with the factor "a", and create new colormap
my_cmap = plt.cm.gist_yarg(np.arange(plt.cm.gist_yarg.N))
my_cmap[:,0:3] *= a 
my_cmap = ListedColormap(my_cmap)

# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, 
                      background_color='white', colormap=my_cmap, 
                      #color_func=lambda *args, **kwargs: "black",
                      collocations=False, stopwords = STOPWORDS, 
                      mask=mask).generate(dracula_text)
# Plot
plot_cloud(wordcloud)
"""