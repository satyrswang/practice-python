#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:14:09 2017

@author: wyq
"""
# #** means keypoints

s = [1,4,7,3,2,6,3,5,1]
# s= []        
def bubble(s):
    for j in range(0,len(s)-1):
        for i in range(0,len(s)-j-1):
            if s[i]>s[i+1]:
               tmp = s[i]
               s[i]=s[i+1] 
               s[i+1] =tmp
               
    return s
           
#s = bubble(s)  
#print s    
        
def select(s):
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] > s[j]:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
    return s

#s = select(s)
#print s 
    
def insert(s):
    for i in range(0,len(s)):
        for j in range(i,0,-1):
            if s[j]<s[j-1]:
                tmp = s[j]
                s[j]=s[j-1]
                s[j-1]=tmp
    return s
#s = insert(s)
#print s
#--------------  
#naive          
def merge_sort(st):
    if len(st) <= 1:
        print "before everything",st
        return st
    
    middle = len(st) / 2
    print "middle",middle
    l = merge_sort(st[:middle])
    print "l",l
    r = merge_sort(st[middle:])    
    print "r",r
    return merge(l,r)#***
    
def merge(l,r):
    s =[]
    i=0
    j=0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            s.append(l[i])
            print "resultappendl",s
            i += 1
        else:
            s.append(r[j])
            print "resultappendr",s
            j += 1
#    if not l:
#        s+=r[0] 
#        return s 
#    if not r:
#        s+=l[0]
#        return s   
    print "while",i,j,l,r
    
    s += l[i:]#***
    s += r[j:]#***知道其中的一个结束了，将另一个剩下的append即可
    print "last",s
    return s
   
s=merge_sort(s)
print "finally",s      

















