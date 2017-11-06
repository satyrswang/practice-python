# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:58:17 2017

@author: yuqing.wang1
"""

import sitecustomize
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      #needs to be updated
        self.children = {}  
    
    def inc(self, numOccur):
        self.count += numOccur
        
    def disp(self, ind=1):
  #      print '  '*ind, self.name, ' ', self.count
        for child in self.children.values():
            child.disp(ind+1)
simpDat = [['r', 'z', 'h', 'j', 'p'],
           ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
           ['z'],
           ['r', 'x', 'n', 'o', 's'],
           ['y', 'r', 'x', 'z', 'q', 't', 'p'],
           ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
        
def updateHeader(nodeToTest, targetNode):   #this version does not use recursion
    while (nodeToTest.nodeLink != None):    #Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
       
def ascendTree(leafNode, prefixPath): #ascends from leaf node to root
    if leafNode.parent != None:
 #       print leafNode.parent
        prefixPath.append(leafNode.name)
 #       print prefixPath
        ascendTree(leafNode.parent, prefixPath)
    
def findPrefixPath(basePat, treeNode): #treeNode comes from header table
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
            print "condPats",condPats
        treeNode = treeNode.nodeLink
    return condPats
           
def updateTree(items, inTree, headerTable, count):
#    print "items, inTree, headerTable, count",items, inTree, headerTable, count
    if items[0] in inTree.children:#check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count) #incrament count
    else:   #add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree) 
        if headerTable[items[0]][1] == None: #update header table 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:  
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
        
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict
ret = createInitSet(simpDat) 
print  "mydata",ret

def createTree(dataSet, minSup=1): #create FP-tree from dataset but don't mine
    headerTable = {}
    #go over dataSet twice
    for trans in dataSet:#first pass counts frequency of occurance    
        for item in trans:# trans is key
#            print trans
 #           print item   ,dataSet[trans] 
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
#    print "headertable",headerTable
    for k in headerTable.keys():  #remove items not meeting minSup
        if headerTable[k] < minSup: 
            del(headerTable[k])
#    print "headertable",headerTable
    freqItemSet = set(headerTable.keys())
#    print 'freqItemSet: ',freqItemSet
    if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 
#    print 'headerTable: ',headerTable
    retTree = treeNode('Null Set', 1, None) #create tree
    for tranSet, count in dataSet.items():  #go through dataset 2nd time
#        print "1",tranSet,count
        localD = {}
        for item in tranSet:  #put transaction items in order
            if item in freqItemSet:
#                print "transet,count,freq,item",tranSet,count,freqItemSet,item
                localD[item] = headerTable[item][0]
#                print localD
        if len(localD) > 0:
#            print "local",localD
#            print localD.items()
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
#            print "ordered",orderedItems
            updateTree(orderedItems, retTree, headerTable, count)#populate tree with ordered freq itemset
    return retTree, headerTable #return tree and header table
rettree,ht = createTree(ret)
print "rettree ht",rettree,ht





def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    print('\n')
    print "inTree, headerTable, minSup, preFix, freqItemList",inTree, headerTable,preFix,freqItemList
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1])]#(sort header table) 
    print "bigl",bigL
    for basePat in bigL:  #start from bottom of header table
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        print 'finalFrequent Item: ',newFreqSet    #append to set
        freqItemList.append(newFreqSet)
        print freqItemList
        print "...............",basePat, headerTable[basePat][1]
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        print 'condPattBases :',basePat, condPattBases  #condPattBases : o {frozenset(['x', 's', 'r']): 1}
        print('\n')
        myCondTree, myHead = createTree(condPattBases, minSup)
        print 'head from conditional tree: ', myHead
        if myHead != None: #3. mine cond. FP-tree
            print 'conditional tree for: ',newFreqSet
            
            myCondTree.disp(1)    
            print "myCondTree, myHead, minSup, newFreqSet, freqItemList",myCondTree, myHead, minSup, newFreqSet, freqItemList
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

freqItems = []
mineTree(rettree,ht,3,set([]),freqItems)
print('\n')
print "freqItems__",freqItems




#import twitter
#from time import sleep
#import re
#
#def textParse(bigString):
#    urlsRemoved = re.sub('(http:[/][/]|www.)([a-z]|[A-Z]|[0-9]|[/.]|[~])*', '', bigString)    
#    listOfTokens = re.split(r'\W*', urlsRemoved)
#    return [tok.lower() for tok in listOfTokens if len(tok) > 2]
#
#def getLotsOfTweets(searchStr):
#    CONSUMER_KEY = ''
#    CONSUMER_SECRET = ''
#    ACCESS_TOKEN_KEY = ''
#    ACCESS_TOKEN_SECRET = ''
#    api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
#                      access_token_key=ACCESS_TOKEN_KEY, 
#                      access_token_secret=ACCESS_TOKEN_SECRET)
#    #you can get 1500 results 15 pages * 100 per page
#    resultsPages = []
#    for i in range(1,15):
#        print "fetching page %d" % i
#        searchResults = api.GetSearch(searchStr, per_page=100, page=i)
#        resultsPages.append(searchResults)
#        sleep(6)
#    return resultsPages
#
#def mineTweets(tweetArr, minSup=5):
#    parsedList = []
#    for i in range(14):
#        for j in range(100):
#            parsedList.append(textParse(tweetArr[i][j].text))
#    initSet = createInitSet(parsedList)
#    myFPtree, myHeaderTab = createTree(initSet, minSup)
#    myFreqList = []
#    mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
#    return myFreqList

#minSup = 3
#simpDat = loadSimpDat()
#initSet = createInitSet(simpDat)
#myFPtree, myHeaderTab = createTree(initSet, minSup)
#myFPtree.disp()
#myFreqList = []
#mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
