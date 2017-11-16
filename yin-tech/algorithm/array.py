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
def longest_non_repeat(s):
    start, maxlen = 0, 0
    used_char = {}
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i-start+1)
        used_char[char] = i
    return maxlen


def longest(s):
    res = set()
    length = 0
    for char in s:
        if char not in res:
            res.add(char)
        else:
            if len(res)>length:
                length = len(res)
            res = set()
            res.add(char)
    return length
        
a = "abcabcdefbb"
print(a)
print(longest_non_repeat(a))
print longest(a)


#4 three_sum

def three(s,needsum=0,neednum=3):
    s.sort()
    al = []
   # sum_al = sum(already)
    for i, num in enumerate(s):
        gap = needsum - num
        neednum = neednum -1
      #  print "i,num",i,num,gap,neednum
        gettwo = two(s[i+1:],gap,neednum)
      #  print "gettwo",gettwo
        if gettwo:
            for e in gettwo:
                e.insert(0,num)
                al.append(e)
    return al

def two(s,needsum,neednum=2):
    res = []
    get = []
    for i, num in enumerate(s):
     #   print "two i num",i,num
        get.append(num)
        e = needsum -num
     #   print "get,e,res",get,e,res
        if e in s[i+1:]:
            get.append(e)
            res.append(get)
        get = []
    return res
        
x = [-1,0,1,2,-1,-4]
print(three(x))           
#逻辑没问题，问题在到底哪个变量我存放那个
              
    
#        if i == needsum-sum_al and len(already)==neednum-1:
#            already.append(i)
#            return already
#        elif len(already)<needsum-1:
            
    


#5 rotate_array
#左右手问题

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)
#左手翻转，右手翻转，整体翻转

def reverse(array, a, b):
    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1





















