# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:25:25 2017

@author: yuqing.wang1
"""

from numpy import *

def loadDataSet():
    return [[9,7,4,8],[1, 3,2,7,5,9,3,4], [2,3,8,6,3,5], [1,2,3,4,9,7,8, 5],[2,3,6,8,5],[3,4,2,5],[4,3,2,1],[5,3,3,1]]

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
data = loadDataSet()
C1 = createC1(data) 
dataset = map(set,data)
#print dataset
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
#    print "numitems",numItems
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems #在set出现的次数
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData
retList,supportData = scanD(dataset,C1,0.5)
#print "result...",retList,supportData

def aprioriGen(Lk, k): #creates Ck 过程为剪枝 k控制前几个数需要一样
    retList = []
    lenLk = len(Lk)
 #   print "lenLk here",lenLk
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
   #         print "i",i,"j",j
            L1 = list(Lk[i])[:k-1]; L2 = list(Lk[j])[:k-1]
  #          print "lk",Lk[i],Lk[j]
  #          print "L1",L1,"l2",L2            
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
 #   print "retlist",retList
    return retList
    
   

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
#    print "L",L
    k = 1
    while (len(L[k-1]) > 0):#当L 为空时停止
 #       print "L[k-1]",L[k-1],"k",k
        Ck = aprioriGen(L[k-1], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
  #      print "hiscandagain",Lk, supK
        supportData.update(supK)
  #      print "agiansu",supportData
        L.append(Lk)
        k += 1
  #      print "nowk",k
    return L, supportData    
    
l ,sudata = apriori(data)
print "l",l
print('\n')
print "sudata",sudata
print('\n')

    
    
#L k 
#L负责此次循环里，剪枝之后的物品集子 第一轮每个集子里是1个物品，第二轮是两个
#k 负责控制停止，当只剩下一个集子的时候，停止while
#为什么k设为2呢？要-2呢 不影响，若减1也可
#先进行对Ck遍历，获得Lk，Ck是上一步剪枝后集子，Lk再进行剪枝
#如果集子前几个一样则union，不一样则忽略。k控制到底前几个。


def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:#frozenset([1])
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
            print "prunedH",prunedH
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):#如果集子里的物品数大于两个则进一步合并
    m = len(H[0])#
    print "m",m
    if (len(freqSet) > m): #如果集子个数大于（每个集子的物品个数+1）2则重新打散，将每个物品计算support合成两个物品的集子
        print "len(freqSet)",len(freqSet),"H",H,"m",m
        Hmp1 = aprioriGen(H, m)#合并后的集子列表
        print "Hmp1",Hmp1
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        print "Hmp1",Hmp1
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
#什么是合并，则将一个集子的物品打散，重新合并成多个含有两个物品的集子
    
def generateRules(L, supportData, minConf=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    print len(L)
    for i in range(1, len(L)):#只选了集子有两个物品的为例子
        for freqSet in L[i]:
            print "freqset",freqSet
            H1 = [frozenset([item]) for item in freqSet]
            print H1
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)#基于一个集子进行合并，减少集子中物品个数
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList  

bigRuleList  = generateRules(l,sudata)



            
def pntRules(ruleList, itemMeaning):
    for ruleTup in ruleList:
        for item in ruleTup[0]:
            print itemMeaning[item]
        print "           -------->"
        for item in ruleTup[1]:
            print itemMeaning[item]
        print "confidence: %f" % ruleTup[2]
        print       #print a blank line
        
            
#pntRules(bigRuleList,)
    
    
