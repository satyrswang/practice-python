#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:21:04 2017

@author: wyq

"""

import numpy as np
import tensorflow as tf

#1

def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)])



def fizz_buzz_encode(i):
    if   i % 15 == 0: return np.array([0, 0, 0, 1]) # FizzBuzz
    elif i % 5  == 0: return np.array([0, 0, 1, 0]) # Buzz
    elif i % 3  == 0: return np.array([0, 1, 0, 0]) # Fizz
    else:             return np.array([1, 0, 0, 0])

NUM_DIGITS = 10
trX = np.array([binary_encode(i, NUM_DIGITS) for i in range(101, 2 ** NUM_DIGITS)])
trY = np.array([fizz_buzz_encode(i)          for i in range(101, 2 ** NUM_DIGITS)])   


NUM_HIDDEN = 100
    

X = tf.placeholder("float", [None, NUM_DIGITS])
Y = tf.placeholder("float", [None, 4]



def init_weights(shape):
    return tf.Variable(np.random_normal(shape, stddev=0.01))
 
w_h = init_weights([NUM_DIGITS, NUM_HIDDEN])
w_o = init_weights([NUM_HIDDEN, 4]


#import matplotlib.pyplot as plt
#import numpy as np
#import keras
#import tensorflow as tf

#from matplotlib import pyplot as plt
#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
#import time
#
#
#fig = plt.figure()
#ax = Axes3D(fig)
#X = np.arange(-10, 10)
#Y = np.arange(-1, 1)
#
#for W1 in range(0,10):
#    for W2 in range(0,10):
#        for  B in range(0,10):
#            for i in range(0,21):
#                Z = X[i]*W1 + Y[i] *W2 + B
#            
#                ax.plot(X, Y, Z)
#                plt.show()
#                sleep(1000)




#np.random.seed(123)  
#
#from keras.datasets import mnist
#from keras.models import Sequential
#from keras.layers.core import Dense,Dropout,Activation,Flatten
#from keras.utils import np_utils
#from keras.layers.convolutional import Convolution2D,MaxPooling2D

#batch_size =128
#nb_classes =10
#
#img_rows,img_cols = 28,28
#
#(x_train,y_train),(x_test,y_test) =mnist.load_data()
#print x_train.shape
#
#x_train = x_train.reshape(x_train.shape[0],1,img_rows,img_cols) #**
#x_test = x_test.reshape(x_test.shape[0],1,img_rows,img_cols)
#
#x_train  = x_train.astype("float32")  #**
#x_test = x_test.astype("float32") 
