# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:06:53 2017

@author: yuqing.wang1
"""
import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt


filename = 'C:\Users\yuqing.wang1\Desktop\datingTestSet2.txt'
fr = open(filename,'r')
numberOfLines = len(fr.readlines())         #get the number of lines in the file
returnMat = np.zeros((numberOfLines,3))        #prepare matrix to return
classLabelVector = []                       #prepare labels return   
#print numberOfLines
index = 0
fr = open(filename)
for line in fr.readlines():
    line = line.strip()
   # print line
    listFromLine = line.split('\t')
    returnMat[index,:] = listFromLine[0:3]
    classLabelVector.append(int(listFromLine[-1]))
    index += 1
#print returnMat,classLabelVector
dataSet= returnMat
minVals = dataSet.min(0)
maxVals = dataSet.max(0)
ranges = maxVals - minVals
normDataSet = np.zeros(np.shape(dataSet))
#print normDataSet
m = dataSet.shape[0] #rownumber
dataSetSize = m
print m
#print dataSet.shape
normDataSet = dataSet - np.tile(minVals, (m,1))
normDataSet = normDataSet/np.tile(ranges, (m,1))   #element wise divide
#print minVals,ranges,normDataSet
hoRatio = 0.50      #hold out 10%
numTestVecs = int(m*hoRatio)
normMat = normDataSet    
#print numTestVecs,normMat 
errorCount = 0.0



fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(returnMat[:,1], returnMat[:,2], 15.0*np.array(classLabelVector), 15.0*np.array(classLabelVector))
ax.axis([-2,25,-0.2,2.0])
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()



def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #行数
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    print diffMat
    sqDiffMat = diffMat**2
    print sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1)
    print "sqDis" ,sqDistances
    distances = sqDistances**0.5
    print "dis" ,distances
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
    

    
for i in range(numTestVecs):
    print i    
    classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],classLabelVector[numTestVecs:m],3)
    print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classLabelVector[i])
    if (classifierResult != classLabelVector[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print errorCount
































