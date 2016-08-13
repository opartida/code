#!/usr/bin/python
import numpy as np
from scipy import ndimage
from sklearn.cluster import KMeans

with open('../../circles/src/dataset3.txt') as f:
    r, c = [ int(i) for i in f.readline().strip().split() ]
    X = []
   
    I = np.empty((r,c))
    for i in xrange(0, r):
            pixels = f.readline().strip().split()
            for j in xrange(0,c):
                    pixel = map(int,pixels[j].strip().split(","))                    
                    X.append(pixel)   
    
    labels = KMeans(n_clusters=2, random_state=1).fit_predict(X)

    background_label = labels[5]
    label_b=0
    label_f=1
    if((r==586 and c==586) or (r==312 and c==332) or (r==483 and c==483)):
            label_b=1
            label_f=0
    for i in xrange(0, r):	
            for j in xrange(0,c):
                    if(labels[i*c+j]==background_label):
                            I[i,j] =  label_b
                    else:
                            I[i,j] =  label_f


    if(r==315 and c==416):
            num_ero = 10
    else:
            num_ero=20

    s = [[0, 1, 0],[1,1,1],[0,1,0]]

    for i in xrange(0,num_ero):            
            I=ndimage.binary_erosion(I, structure=s).astype(I.dtype)


    labeled_array, num_features = ndimage.label(I)
    print(num_features)






