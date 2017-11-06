# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 09:57:36 2017

@author: yuqing.wang1
"""
#from numpy import *
#import matplotlib
#import matplotlib.pyplot as plt
#
#n = 1000 #number of points to create
#xcord0 = []
#ycord0 = []
#xcord1 = []
#ycord1 = []
#markers =[]
#colors =[]
#fw = open('testSet.txt','w')
#for i in range(n):
#    [r0,r1] = random.standard_normal(2)
#    fFlyer = r0 + 9.0
#    tats = 1.0*r1 + fFlyer + 0
#    xcord0.append(fFlyer)
#    ycord0.append(tats)
#    fw.write("%f\t%f\n" % (fFlyer, tats)) #split('/t')
#
#fw.close()
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(xcord0,ycord0, marker='^', s=90)
#plt.xlabel('hours of direct sunlight')
#plt.ylabel('liters of water')
#plt.show()

from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return mat(datArr)
    
    
dataMat = loadDataSet(r'D:\python-------------------------------------------\testSet.txt')
#print "getdataMat",dataMat[0:10,0],dataMat[0:10,0].flatten().A[0]

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
 #   print "mean",meanVals 
    meanRemoved = dataMat - meanVals #remove mean
    print meanRemoved
    
    covMat = cov(meanRemoved, rowvar=0)
    print covMat
    
    eigVals,eigVects = linalg.eig(mat(covMat))
    print "eigVals,eigVects",eigVals,eigVects
    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
    lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[0:10,0].flatten().A[0], dataMat[0:10,1].flatten().A[0], marker='^', s=90)
    ax.scatter(dataMat[0:10,0].flatten().A[0], dataMat[0:10,1].flatten().A[0], marker='o', s=90)
    #ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0], marker='o', s=50, c='red')
    plt.show()    
    return lowDDataMat, reconMat

pca(dataMat[0:10,:],1)