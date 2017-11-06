# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:33:37 2017

@author: yuqing.wang1
"""

import numpy as np
#import random
import matplotlib
import matplotlib.pyplot as plt




def distEclud(vecA, vecB):
    return np.sqrt(sum(np.power(vecA - vecB, 2))) #la.norm(vecA-vecB)

def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
  #  print n,dataSet
    centroids = np.mat(np.zeros((k,n)))
   # print "cen",centroids.shape
    for j in range(n):
      #  print j
      #  print dataSet
        minJ = min(dataSet[:,j]) 
      #  print "min",minJ
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = np.mat(minJ + rangeJ * np.random.rand(k,1))
       # print "centro",centroids,centroids.shape
    return centroids
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]
  #  print m
    clusterAssment =np. mat(np.zeros((m,2)))#create mat to assign data points 
  #  print dataSet                                 #to a centroid, also holds SE of each point
    centroids = randCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = float("inf"); minIndex = -1
            for j in range(k):
                vec[0] = centroids[j,0]
                vec[1] = centroids[j,1]
                distJI = distEclud(vec,dataMat[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
   #     print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = np.mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment





k=6

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat


#d =array([[2,3],[6,8],[4,9],[3.4,6.4],[3,7.8],[9.5,3],[20,4]])
#print randCent(d,2)

dataMat = loadDataSet(r'D:\nnnnnnnnnnnnnnnnnnn\machinelearninginaction\Ch10\testSet.txt')
dataMat = np.array(dataMat)
print dataMat,dataMat.shape



m = np.shape(dataMat)[0]
#print m
clusterAssment = np.mat(np.zeros((m,2)))#create mat to assign data points 
#print clusterAssment     
                             #to a centroid, also holds SE of each point
centroids = randCent(dataMat, k)
clusterChanged = True
#print centroids
#_---------------------以下为kmeans主要内容
vec=[0.0,0.0]
while clusterChanged:
    clusterChanged = False
    for i in range(m):#for each data point assign it to the closest centroid
        minDist = float("inf")  ; minIndex = -1
        for j in range(5):
            vec[0] = centroids[j,0]
            vec[1] = centroids[j,1]
            distJI = distEclud(vec,dataMat[i,:])
        #    print vec
            if distJI < minDist:
                minDist = distJI; minIndex = j
        if clusterAssment[i,0] != minIndex: clusterChanged = True  #停止条件 所有点的centroid不再变化
        clusterAssment[i,:] = minIndex,minDist**2
   # print centroids
    for cent in range(k):#recalculate centroids
        ptsInClust = dataMat[np.nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
  #      print "pts",ptsInClust
        centroids[cent,:] = np.mean(ptsInClust, axis=0) #assign centroid to mean 
  #     print "cen",centroids






m = np.shape(dataMat)[0]
clusterAssment = np.mat(np.zeros((m,2)))
ini = np.mean(dataMat, axis=0).tolist()
centroid0 = np.mean(dataMat, axis=0).tolist()[0]
centList =[centroid0] #create a list with one centroid
centList = np.array(centList)
for j in range(m):#calc initial Error
    clusterAssment[j,1] = distEclud(ini, dataMat[j,:])**2
while (len(centList) < k):
    lowestSSE = float("inf")
    for i in range(len(centList)):
        ptsInCurrCluster = dataMat[np.nonzero(clusterAssment[:,0].A==i)[0],:]#get the data points currently in cluster i
        centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distEclud)
        print i,"pts",ptsInCurrCluster,"cent",centroidMat.shape,centroidMat,splitClustAss.shape
        sseSplit = sum(splitClustAss[:,1])#compare the SSE to the currrent minimum
        sseNotSplit = sum(clusterAssment[np.nonzero(clusterAssment[:,0].A!=i)[0],1])
        print "sseSplit, and notSplit: ",sseSplit,sseNotSplit
        print splitClustAss
        if (sseSplit + sseNotSplit) < lowestSSE:
            bestCentToSplit = i+1#第次的kmeans
            bestNewCents = centroidMat
            bestClustAss = splitClustAss.copy()
            lowestSSE = sseSplit + sseNotSplit
    bestClustAss[np.nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) #change 1 to 3,4, or whatever
    print len(centList)
    bestClustAss[np.nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit
    print 'the bestCentToSplit is: ',bestCentToSplit,"th kmeans"
    print 'the len of bestClustAss is: ', len(bestClustAss)
    centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]#replace a centroid with two best centroids 
    print centList
    centList.append(bestNewCents[1,:].tolist()[0])
    clusterAssment[np.nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss#reassign new clusters, and SSE

    
    
    
    
#def clusterClubs(numClust=5):

#datList = []
#for line in open(r'D:\python-------------------------------------------\kmeans\places.txt').readlines():
#    lineArr = line.split('\t')
#    datList.append([float(lineArr[4]), float(lineArr[3])])
#datMat = np.mat(datList)
#myCentroids, clustAssing = biKmeans(datMat, numClust, distMeas=distSLC)
#fig = plt.figure()
#rect=[0.1,0.1,0.8,0.8]
#scatterMarkers=['s', 'o', '^', '8', 'p', \
#                'd', 'v', 'h', '>', '<']
#axprops = dict(xticks=[], yticks=[])
#ax0=fig.add_axes(rect, label='ax0', **axprops)
#imgP = plt.imread('Portland.png')
#ax0.imshow(imgP)
#ax1=fig.add_axes(rect, label='ax1', frameon=False)
#for i in range(numClust):
#    ptsInCurrCluster = datMat[nonzero(clustAssing[:,0].A==i)[0],:]
#    markerStyle = scatterMarkers[i % len(scatterMarkers)]
#    ax1.scatter(ptsInCurrCluster[:,0].flatten().A[0], ptsInCurrCluster[:,1].flatten().A[0], marker=markerStyle, s=90)
#ax1.scatter(myCentroids[:,0].flatten().A[0], myCentroids[:,1].flatten().A[0], marker='+', s=300)
#plt.show()
      

    


  
