# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:09:27 2016

@author: maxim
"""

from scipy import misc
#module d’affichage
import matplotlib.pyplot as plt
import numpy as np

image = misc.imread('img/amazon.png')

plt.imshow(image)
plt.axis('off')
plt.show()

def hist(image):
    colors = list()
    # On recupere l'image en profondeur (RGB + transparence => PNG) 
    (x,y,z) = np.shape(image)
    for col in range(z):
        colors.append(dict())
        for i in range(x):
            for j in range(y):
                try:
                    colors[col][image[i,j,col]] += 1
                except:
                    colors[col][image[i,j,col]] = 1
    return colors
    
def get_best_color(histo):
    bestColor = list()
    for colors in histo:
        best = 1
        maxi = 0
        for color in colors.items():
            if color[1] > maxi and color[0] != 0 and color[0] != 255:
                best = color[0]
                maxi = color[1]
        bestColor.append(best)
    return bestColor

histo = hist(image)
print "Meilleure couleur : rgb(", get_best_color(histo), ")"