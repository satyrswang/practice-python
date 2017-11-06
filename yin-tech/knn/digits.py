# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:18:39 2017

@author: yuqing.wang1
"""

# -*- coding: utf-8 -*-   
      
import os  
import numpy as np
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #行数
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    #print diffMat
    sqDiffMat = diffMat**2
    #print sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1)
    #print "sqDis" ,sqDistances
    distances = sqDistances**0.5
    #print "dis" ,distances
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print root #当前目录路径  
        print dirs #当前路径下所有子目录  
        print files #当前路径下所有非目录子文件
#file_name(r'C:\Users\yuqing.wang1\Desktop\trainingDigits')

def img2vector(filename):
    returnVect =np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect


hwLabels = []
trainingFileList = os.listdir(r'C:\Users\yuqing.wang1\Desktop\trainingDigits')           #load the training set
m = len(trainingFileList)

trainingMat = np.zeros((m,1024))
print trainingFileList,m,trainingMat
for i in range(m):#对每个文件
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]     #take off .txt
    classNumStr = int(fileStr.split('_')[0])
    hwLabels.append(classNumStr)#作为label
    trainingMat[i,:] = img2vector(r'C:\Users\yuqing.wang1\Desktop\trainingDigits/%s' % fileNameStr)
testFileList = os.listdir(r'D:\nnnnnnnnnnnnnnnnnnn\machinelearninginaction\Ch02\testDigits')        #iterate through the test set
errorCount = 0.0
mTest = len(testFileList)
for i in range(mTest):
    fileNameStr = testFileList[i]
    fileStr = fileNameStr.split('.')[0]     #take off .txt
    classNumStr = int(fileStr.split('_')[0])
    vectorUnderTest = img2vector(r'D:\nnnnnnnnnnnnnnnnnnn\machinelearninginaction\Ch02\testDigits/%s' % fileNameStr)
    classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
    print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
    if (classifierResult != classNumStr): errorCount += 1.0
print "\nthe total number of errors is: %d" % errorCount
print "\nthe total error rate is: %f" % (errorCount/float(mTest))