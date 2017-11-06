# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 18:09:14 2017

@author: yuqing.wang1
"""

# a = list(a) if isinstance(a, (list, tuple)) else [] 
#



 #$1
 
def josepheus(list_data, skip):
     idx = 0
     skip = skip -1
     while len(list_data):

           idx = (skip+idx) % len(list_data) #hashing to keep changing the index to every 3rd******************************
           
           print(list_data.pop(idx))
a = ['1','2','3','4','5','6','7','8','9']
#josepheus(a,3)
#用到了pop， 将list_data直接变化。关键是idx  
#当len 为9,idx 为2,len=8 idx=4,len=7 idx=6
#len=6 idx=2  
#len一定是随着pop自减 idx？一定有取余数和skip有关。但skip是定值
#想到和上一个idx有关 因为呈现2,4,6规律  skip+idx  理解和具体数字无关只和idx有关


#$2 
#以下为错误范例
a = [2, 1, [3, [4, 5], 6], 7, [8]]
#def flatten(l):
#    res = []
#    for i in l:
#        if isinstance(i,(list,tuple)):
#            res.append(flatten(i))
#        else:
#            res.append(i)
#    return res        

#使用了isinstance

def flatten(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []  #****************************************************
#这个步骤不可少。要将a带入到下一步的append中
    for i in l:
        if isinstance(i, (list, tuple)):
            a = flatten(i, a)
        else:
            a.append(i)
    return a
res = flatten(a)
print res
# stack version

#3


def stackversion(l):
    


























