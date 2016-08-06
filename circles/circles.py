from sklearn import mixture
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy import signal



def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

np.set_printoptions(threshold=np.inf)

with open('dataset4.txt') as f:
    
	r, c = [ int(i) for i in f.readline().strip().split() ]
	X = []
	P =np.empty((r,c,3))
	I = np.empty((r,c))
	#vbgmm = mixture.VBGMM(n_components=13, random_state=1, alpha=20, n_iter=5)
	#dpgmm = mixture.DPGMM(n_components=15, covariance_type='full',n_iter=5)		
	for i in xrange(0, r):
            pixels = f.readline().strip().split()
            for j in xrange(0,c):
                    pixel = map(int,pixels[j].strip().split(","))
                    P[i,j,0] = pixel[0]
                    P[i,j,1] = pixel[1]
                    P[i,j,2] = pixel[2]
                    X.append(pixel)
	
	P = rgb2gray(P)
	
	plt.imshow(P)	
	plt.show()
	
	# Segment image using K means with k greater than max number of clusters (20)
	#X = np.array(X)
        
	labels = KMeans(n_clusters=2, random_state=1).fit_predict(X)	
        for i in xrange(0, r):	
            for j in xrange(0,c):
                I[i,j] = labels[i*c+j]
        #remove background
        
        plt.imshow(I)
        plt.show()
        
        
	#Apply sobel filter to find edges
#	sx = ndimage.sobel(P, axis=0, mode='constant')
#	sy = ndimage.sobel(P, axis=1, mode='constant')
#	sob = np.hypot(sx, sy)
#        
#	scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],[-10+0j, 0+ 0j, +10 +0j], [ -3+3j, 0+10j,  +3 +3j]])
#	grad = signal.convolve2d(sob, scharr, boundary='symm', mode='same')	
        

	# save only the edge points positions
        #grad[c] = 0
#        grad[grad!=0]=1
#        grad = np.abs(grad)
#        
#        Z =[]
#        for i in xrange(0, r):	
#            for j in xrange(0,c):
#                if(grad[i,j]!=0):
#                    Z.append([i,j])
#         
#        Z = np.array(Z)   
#        
#        plt.plot(Z[:,0],Z[:,1],'x')
#        plt.show()
#                        
#        plt.imshow(grad)
#        plt.show()
#	
	
	
	
	
	
	
	