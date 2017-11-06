# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:10:20 2017

@author: yuqing.wang1
"""
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)   
data=np.random.normal(size=(1000,4),loc=0,scale=1)   
print data
labels=['A','B','C','D']   

plt.scatter(data[:,0], data[:,1])
plt.show()