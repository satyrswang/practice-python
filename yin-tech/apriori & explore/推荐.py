# -*- coding: utf-8 -*-
""" 
Created on Tue Oct 24 10:43:43 2017

@author: yuqing.wang1
"""
# 238639(row) 5308(planner) 85212(user)

import numpy as np
import matplotlib.pyplot as plt

#file_data = np.loadtxt(open(r'C:\Users\yuqing.wang1\Downloads\attentionofplanner.csv',"rb"),delimiter=",",skiprows=1)
file_data = np.loadtxt(open(r'C:\Users\yuqing.wang1\Downloads\attentionofplanner.csv',"rb"),delimiter=",",skiprows=1)
# print file_data[0:5,:]  
m = len(file_data[:,0])
#print "lines",m
planner = sorted(list(set(file_data[:,1])))
user = sorted(list(set(file_data[:,0])))
fir = user[0]
indexofu = user.index(file_data[0][0])
indexofp = planner.index(file_data[0][1])
#print len(planner),len(user)
#print file_data[0][0] ==fir 
#matdata = np.mat(file_data)
#dicdata= dict(file_data)
#keys = dicdata.keys()
#values = dicdata.values()
#print dicdata[1.0],keys[0:5],len(values)

#print file_data[1][1]

mymat = np.mat(np.zeros((len(user),len(planner))))
#print mymat
setofp =[]
alofp =[]
for i in range(m):
    if(file_data[i][0]==fir):
        mymat[indexofu,indexofp] = 1
        setofp.append(file_data[i][1])
    else:
        fir = file_data[i][0]
        alofp.append(setofp)
        setofp = [] 
        setofp.append(file_data[i][1])
        indexofu = user.index(file_data[i][0])
        if(file_data[i][1] in planner):
                indexofp = planner.index(file_data[i][1])
                mymat[indexofu,indexofp] = 1
alofp.append(setofp)
#print "alofp",alofp, len(alofp)

for i in alofp:
    if i ==[]:
        alofp.remove(i)
#print "alofp",alofp, len(alofp)

#print  mymat[7].shape

sumofm =sum(mymat).tolist()
sumofmm=sum(sumofm[0])
#print sumofm,len(sumofm[0]),sumofmm

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
    #    print transaction
        for item in transaction:
     #       print item
            if not [item] in C1:            
                C1.append([item])
     #           print C1
  #  print C1           
    C1.sort()
    return map(frozenset, C1)#use frozen set so we

C1 = createC1(alofp) 
dataset = map(set,alofp)
#print "getsetoffile_data",dataset,"len",len(dataset)




def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
     #   print tid
        for can in Ck:
    #        print can
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(D))
   # print numItems
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems #在set出现的次数
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData
    
retList,supportData = scanD(dataset,C1,0.05)
#print "result...",retList,supportData

#------------------------------获得了每个理财师的支持度
def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
 #   print lenLk
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
          #  print "i",i,"j",j
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
        #    print "L1",L1,"l2",L2            
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList
    
def generateRules(L, supportData, minConf):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                H1 = [frozenset([item]) for item in freqSet]
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList         

def calcConf(freqSet, H, supportData, brl, minConf=0.5):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.5):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)   


L = [retList]
minSupport = 0.05
  #  print "L",L
k = 2
while (len(L[k-2]) > 0):
#    print "L[k-2]",L[k-2],"k",k
    Ck = aprioriGen(L[k-2], k)
    Lk, supK = scanD(dataset, Ck, minSupport)#scan DB to get Lk
    supportData.update(supK)
    L.append(Lk)
    k += 1
    
#print "result...",L
#print('\n')
#print('\n')
#print "himysupportdata",supportData

reslist = generateRules(L,supportData,0.5)
#print reslist






#print sumofm,"summymatget",sumofm
#print range(1,60)
#fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10,4))
#for ax in axes:
#    ax.plot(np.array(range(1,len(sumofm)+1)), sumofm, label="each planner")
#fig.tight_layout()

#user = []
#p_uid = []
#with open(r'C:\Users\yuqing.wang1\Downloads\attentionofplanner.csv', 'rb') as f:        # 采用b的方式处理可以省去很多问题
#    reader = csv.reader(f)   
#    m = csv.readlines(reader)
#    file_data = np.mat(np.zeros((m,2)))
#    for line in reader:
#        if reader.line_num == 1: 
#            continue
#        file_data

#print user[0:5],p_uid[0:5],type(user)