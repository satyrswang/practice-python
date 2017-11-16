# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 10:50:09 2017

@author: yuqing.wang1
"""
#1
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)#lambda就是函数，二fib就是指向这个函数

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


#def fib(i):
#    cache = {}
#    if args not in cache:
#        cache[args] = func(*args)
#        return cache[args]    
#    if i < 2:
#        return 1
#    return fib(i-1) + fib(i-2)

#当需要将一个变量作为所有递归中保持变化的，可放在wrap函数之外，当递归调用函数时，只进行wrap中的操作
#只需一次初始化。


#2 杨氏矩阵
#3 除去重复元素

l1 = ['b','c','d','b','c','a','a']
l2 = {}.fromkeys(l1).keys()
#print l2

l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
print l2
l2.sort(key=l1.index)
print l2

si=[]
l = ['b','c','d','b','c','a','a']
g = [si.append(i) for i in sorted(l) if not i in si] 
print si,g

l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
print l2

#4 链表调换

#5 dict
items=[('name','earth'),('port','80')]
dict2=dict(items)
dict1=dict((['name','earth'],['port','80']))
print dict2,dict1

#6 二分
#def bi(l,v):
#    length = len(l) -1 
#    m = length /2
#    if l[m] == v:
#        return m
#    elif l[m]>v:
#        return bi(l[:m],v)
#    else:
#        return bi(l[m:],v)
def bi(l,v):
    low = 0
    high = len(l) -1
    while low <= high:
        mid = (low+high)/2
        m = l[mid]
        if m>v:
            high = mid -1
        elif m<v:
            low = mid + 1
        else:
            return mid
    return None
    
    
mylist = [1,3,5,7,9]
print bi(mylist,7)


#7 找零


def coinChange(values,valuesCounts,money,coinsUsed):
    #遍历出从1到money所有的钱数可能
    for cents in range(1,money+1):
        minCoins = cents
        #把所有的硬币面值遍历出来和钱数做对比
        for kind in range(0,valuesCounts):
            if (values[kind] <= cents):
                temp = coinsUsed[cents - values[kind]] +1
                if (temp < minCoins):
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print ('面值:{0}的最少硬币使用数为:{1}'.format(cents, coinsUsed[cents]))

values = [ 25, 21, 10, 5, 1]
#coinChange(values,150)


# need_change 为需要找零的金额，
# currency_list 为该国货币的面值列表，
# num_list 为需要找零的最少货币数目, num_list的长度至少为(need_change+1)
def giveChange(need_change, currency_list, num_list):
    for change in range(need_change+1): #从0开始计算最少需要的货币数
        for currency in currency_list: #遍历每一种货币
            if (change-currency >= 0) and (num_list[change-currency]+1<num_list[change]): #计算最少货币需求数
                num_list[change] = num_list[change-currency] + 1
    return

def main():
    need_change = 63
    currency_list = [1,5,10,21,25]
    num_list = list(range(need_change+1)) #初始化num_list为0到need_change,共(need_change+1)个数
    giveChange(need_change, currency_list, num_list)
    print("%d 需要 %d 个货币来找零"%(need_change, num_list[need_change]))
if __name__ == "__main__":
    main()

#不是枚举法
#缩小问题规模
#memo
        
        
#8 遍历二叉树
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))        
 
def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print current.data
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)        
def deep(root): #其实就是前序遍历
    if not root:
        return
    print root.data
    deep(root.left)
    deep(root.right)

if __name__ == '__main__':
    lookup(tree)
    deep(tree)        
        
#9  前中后序       

#中序遍历:遍历左子树,访问当前节点,遍历右子树

def mid_travelsal(root):
    if root.left is None:
        mid_travelsal(root.left)
    #访问当前节点
    print(root.data)
    if root.right is not None:
        mid_travelsal(root.right)

#前序遍历:访问当前节点,遍历左子树,遍历右子树

def pre_travelsal(root):
    print (root.data)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

#后续遍历:遍历左子树,遍历右子树,访问当前节点

def post_trvelsal(root):
    if root.left is not None:
        post_trvelsal(root.left)
    if root.right is not None:
        post_trvelsal(root.right)
    print (root.data)        
        
pre_travelsal(tree)        
        
#10 深度
def deep(tree):
    if not tree:
        return 0
    return max(deep(tree.left),deep(tree.right))+1

# 两树是否向相同
def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q :
        return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False

#11 前中求后序
def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur
#tree中的思想，
#12 单链表逆

def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre
#前后相连的两个，在记录两个后买面的一个 pre cur tmp

#13 变位词

def Solution1(s1,s2):
        alist = list(s2)
        pos1 = 0
        stillOK = True

        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1

            if found:
                alist[pos2] = None
            else:
                stillOK = False

            pos1 = pos1 + 1

        return stillOK

print(Solution1('abcdt','dcbau'))























        
        