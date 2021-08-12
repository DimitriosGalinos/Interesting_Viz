# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:19:48 2020

@author: mitsel
"""
# Import packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

with open("Dracula.txt", "r") as file:
    dracula_text = file.read().replace('\n', ' ')
dracula_text = dracula_text.replace("  ", ' ')

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");
    
import numpy as np
from PIL import Image
# Import image to np.array
mask = np.array(Image.open('bat4.png'))
# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, 
                      background_color='maroon', colormap='Greys', 
                      collocations=False, stopwords = STOPWORDS, 
                      mask=mask).generate(dracula_text)
# Plot
plot_cloud(wordcloud)