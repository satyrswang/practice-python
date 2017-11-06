# -*- coding: cp936 -*-
import operator
a=[1,2,3]
b=operator.itemgetter(1)
print b #定义函数b，获取对象的第一个域的值
print b(a)
b=operator.itemgetter(1,0)#定义函数b，获取对象的第1个域和第0个域的值
print b(a)



class Parent(object):
    x = 1
 
class Child1(Parent):
    pass
 
class Child2(Parent):
    pass
 
print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

#“双划线”（//）操作符将一直执行整除
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

def multipliers():
    return [lambda x : i * x for i in range(4)]
def multipliers2():
    return [lambda x, i=i : i * x for i in range(4)]

print [m(2) for m in multipliers()]
print [m(3) for m in multipliers2()]
from functools import partial
from operator import mul

def multipliers3():
    return [partial(mul, i) for i in range(4)]
print [m(2) for m in multipliers3()]
def extendList(val, list=[]):
    list.append(val)
    return list
def extendList2(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
