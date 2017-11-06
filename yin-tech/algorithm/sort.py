# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 09:56:54 2017

@author: yuqing.wang1
"""


# arr[i], arr[j] = arr[j], arr[i]
#

s = [2,5,1,3,4,8,5,3,9,0,5]
def merge_s(s):
    if len(s)<=1: #**************************************************************
        return s
    m = len(s) / 2
    l = merge_s(s[:m])
    r = merge_s(s[m:])
    return merge(l,r)

def merge(l,r):
    res = []
    i =0
    j =0
    
    while i < len(l) and j<len(r):  
        if l[i]<=r[j]:
            res.append(l[i])
            i=i+1
        else:
            res.append(r[j])
            j=j+1
   # res+=l[i:]
   # res+=r[j:]
    for x in range(i,len(l)):
        res.append(l[x])
    for x in range(j,len(r)):
        res.append(r[x])
    return res
res = merge_s(s)
print "result",res

def quick(s,fir,last):
    if fir < last:  # 这里和merge的停止条件不同********************************************
        pos= part(s,fir,last)
        quick(s,fir,pos-1)
        quick(s,pos+1,last)
        
def part(s,fir,last):
    pos = fir
    for i in range(fir,last):
        if s[i]<s[last]:
            s[i],s[pos]=s[pos],s[i]
            pos+=1
    s[pos],s[last]=s[last],s[pos]    
    return pos
  
    

#将参数拿进函数就出现问题了    
#每次partition的时候收尾都不是关于arr的，都有变化
#def quick_sort(arr, first, last):
#    """ Quicksort
#        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
#         T(1)=θ(1),T(n)=T(n-1)+T(1)+θ(n) (1);
#         T(n)=2T(n/2)+θ（n)
#    """
#    if first < last:
#        pos = partition(arr, first, last)
#        print(arr[first:pos-1], arr[pos+1:last])
#        # Start our two recursive calls
#        quick_sort(arr, first, pos-1)
#        quick_sort(arr, pos+1, last)
#
#def partition(arr, first, last):
#    wall = first
#    for pos in range(first, last):
#        if arr[pos] < arr[last]: # last is the pivot
#            arr[pos], arr[wall] = arr[wall], arr[pos]
#            wall += 1
#    arr[wall], arr[last] = arr[last], arr[wall]
#    print(wall)
#    return wall

array = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
quick(array, 0, len(array)-1)
print "result",array    
    
  
from math import floor


def shell_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
   
   while not sorted:
        gap = int(floor(gap/shrink))
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                sorted = False
            i = i + 1


#array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
#         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
#print(array)
#comb_sort(array)
#print(array)   
#
def max_heap_sort(arr):

    for i in range(len(arr)-1,0,-1):#**
        heap(arr, i)#**
        
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

def heap(s,end):
    last_parent = (end-1) /2 #这里必须是end而不能是len(s) 两者不等#**    
    for index_parent in range(last_parent,-1,-1):    
        #如果不是最后一个父节点，且有swap则需要迭代多次。每次向下，与child比较
        while index_parent <=last_parent:  #***************************************************************
            # find the laregest child
            child = index_parent *2 +1
            if child+1 <=end and s[child]<s[child+1]:
                child = child +1
            if s[child]>s[index_parent]:
                s[child],s[index_parent] = s[index_parent],s[child]
                index_parent = child
            else: 
                break
            
#def max_heap_sort(arr):
#    """ Heap Sort that uses a max heap to sort an array in ascending order
#        Complexity: O(n log(n))
#    """
#    for i in range(len(arr)-1,0,-1):
#        max_heapify(arr, i)
#        
#        temp = arr[0]
#        arr[0] = arr[i]
#        arr[i] = temp
#
#	
#def max_heapify(arr, end):   
#    last_parent = int((end-1)/2)
#    for parent in range(last_parent,-1,-1):
#        current_parent = parent
#        while current_parent <= last_parent:
#            # Find greatest child of current_parent
#            child = 2*current_parent + 1
#            if child + 1 <= end and arr[child] < arr[child+1]:
#                child = child + 1
#
#            # Swap if child is greater than parent
#            if arr[child] > arr[current_parent]:
#                temp = arr[current_parent]
#                arr[current_parent] = arr[child]
#                arr[child] = temp
#
#                current_parent = child
#            # If no swap occured, no need to keep iterating
#            else:
#                break
		       
            
#array = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
#print("Max Heapify:")
#max_heap_sort(array)
#print(array)            
def min_heap_sort(arr):
    for i in range(0, len(arr)-1):
        min_heapify(arr, i)
	

def min_heapify(arr, start):
    end = len(arr)-1
    last_parent = int((end-start-1)/2)

    # Iterate from last parent to first
    for parent in range(last_parent,-1,-1):
        current_parent = parent

        # Iterate from current_parent to last_parent
        while current_parent <= last_parent:
            # Find lesser child of current_parent
            child = 2*current_parent + 1
            if child + 1 <= end-start and arr[child+start] > arr[child+1+start]:
                child = child + 1

            # Swap if child is less than parent
            if arr[child+start] < arr[current_parent+start]:
                temp = arr[current_parent+start]
                arr[current_parent+start] = arr[child+start]
                arr[child+start] = temp

                current_parent = child
            # If no swap occured, no need to keep iterating
            else:
                break




depGraph = {

    "a" : [ "b" ],
    "b" : [ "c" ],
    "c" :  [ 'e'],
    'e' : [ ],
    "d" : [ ],
    "f" : ["e" , "d"]
}


given = [ "b", "c", "a", "d", "e", "f" ]

#用queue pop
#def dependency(depg,given):
#    
#    res = []
#    for i in range(0,len(given)):
#        if given[i] in out:
#            continue
#        queue.append(given[i]) 
#        out.append(given[i])
#        while queue:  
#            depend = depg[queue.pop(0)]
#            if depend:
#                queue.extend(depend)
#                out.extend(depend)
#    return out
#def dep(depg,start):
#    queue =[]
#    out=[]
#    queue.append(start) 
#    while queue:  
#        depend = depg[queue.pop(0)]
#        if depend:
#            queue.extend(depend)
#            out.extend(depend)
    
           
#            out.append(given[i])
#            queue.extend(depg.get(queue.pop(0)))
#            out.extend(depg.get(queue.pop(0)))
        
#            depend  = depg.get(given(i))
#            for i in depend:
#                while i:
#                    visited.add(i)
#                    i = depg.get(i)                                  

    


def retDeps(visited, start):
    queue = []
    out = []
    queue.append(start)
    while queue:
        newNode = queue.pop(0)
        if newNode not in visited:
            visited.add(newNode)
        for child in depGraph[newNode]:
            queue.append(child)
            out.append(child)
    out.append(start)
    return out
#如何查找一个pac的安装路径？
#用queue记录需要遍历的父节点 pop机制删除
#不太完整。需要修改

def retDepGraph():
    visited = set()
    out = []
    # visited.add(given[0])
    for pac in given:
        if pac in visited:
            continue
        visited.add(pac)
        #out.append(pac)
        if pac in depGraph:
            # find all children
            for child in depGraph[pac]:
                if child in visited:
                    continue
                out.extend(retDeps(visited, child))
        out.append(pac)
    print(out)
retDepGraph()
#如果在visited中则看下一个，否则
#在graph中找到pac，对每个依赖如果在visited中则看下一个，否则，对这个依赖进行搜索找到安装路径
#将依赖的安装路径extend之后加上pac
#（类似于一种逆序的获得out）
#算一个完整的visited，说明已安装过

#对树的遍历问题，深度和广度



#计数排序
def counting_sort(arr):
	"""
    Counting_sort
	Sorting a array which has no element greater than k
	Creating a new temp_arr,where temp_arr[i] contain the number of
	element less than or equal to i in the arr	
    Then placing the number i into a correct position in the result_arr
	return the result_arr
	Complexity: 0(n)
	"""
	
	m = min(arr)
	#in case there are negative elements, change the array to all positive element
	different = 0
	if m < 0:
		#save the change, so that we can convert the array back to all positive number
		different = -m
		for i in range (len(arr)):
			arr[i]+= -m
	k = max(arr)
	temp_arr = [0]*(k+1)
	for i in range(0,len(arr)):
		temp_arr[arr[i]] = temp_arr[arr[i]]+1
	#temp_array[i] contain the times the number i appear in arr
	
	for i in range(1, k+1):
		temp_arr[i] = temp_arr[i] + temp_arr[i-1]
	#temp_array[i] contain the number of element less than or equal i in arr
#	print "temp_arr",temp_arr,arr
	result_arr = [0]*len(arr)
	#creating a result_arr an put the element in a correct positon
	for i in range(len(arr)-1,-1,-1):
#         print i,arr[i],temp_arr[arr[i]] ,arr[i]-different
         result_arr[temp_arr[arr[i]]-1] = arr[i]-different
         temp_arr[arr[i]] = temp_arr[arr[i]]-1
#加和之后相当于位置，赋值到result_arr之后位置减一即可	
	return result_arr 

positive_array = [1,2,3,4,9,1,2,8,3,5,7,0,9,8,1,7,4,5]
negative_array = [-5,-6,-2,-3,-4,-5,0,-9,-2,-3,-8,-4]
x = counting_sort(positive_array)
y = counting_sort(negative_array)
#print(x)
#print(y)




#from numpy import *
#def radix(s):
#    maxs = max(s)
#    row = maxs/10
#    indata = zeros((row,10))
#    res = []
#    for i in s:
#        print indata
#        indata[(i/10) -1,(i%10) -1] =indata[(i/10) -1,(i%10) -1]+1
##    for i in range(0,row):
##        for j in range(0,10):
##            indata[i,j]=indata[i,j]+indata[i,j-1]
#    
#    
#        
#s =[1, 2, 4, 5, 9, 10, 23, 43, 57, 64, 65]       
#radix(s)


































            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    