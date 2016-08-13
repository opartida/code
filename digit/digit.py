import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

with open('input03.txt') as f:
    
	r, c = [ int(i) for i in f.readline().strip().split() ]
	X = []
      
	P = np.empty((r,c,3))	
		
	for i in xrange(0, r):
            pixels = f.readline().strip().split()
            for j in xrange(0,c):
                pixel = map(int,pixels[j].strip().split(","))
                P[i,j,0] = pixel[0]
                P[i,j,1] = pixel[1]
                P[i,j,2] = pixel[2]
                X.append(pixel)
	
        X = np.array(X)
        X_scaled = preprocessing.scale(X)
        X = np.reshape(X,(r,c,3))
        plt.imshow(P)
        plt.show()
        P = rgb2gray(P)
        plt.imshow(X)
        plt.show()
        plt.imshow(P,cmap='Greys_r')
        
        plt.show()
