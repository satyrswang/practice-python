# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 12:05:40 2017

@author: yuqing.wang1
"""

#raise [None]*size yield  enumerate
# key=lambda i: i.start
#'/' +'/'.join(stack)
# for l, r in given:



# Stack Abstract Data Type (ADT)
# Stack() creates a new stack that is empty.
#    It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack.
#    It needs the item and returns nothing.
# pop() removes the top item from the stack.
#    It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it.
#    It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty.
#    It needs no parameters and returns a boolean value.
# size() returns the number of items on the stack.
#    It needs no parameters and returns an integer.

class AbstractStack:
    def __init__(self):
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def __len__(self):
        return self.top

    def __str__(self):
        result = '------\n'
        for element in self:
            result += str(element) + '\n'
        return result[:-1] + '\n------'


class ArrayStack(AbstractStack):#需要实现expand
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        AbstractStack.__init__(self)
        self.array = [None] * size

    def push(self, value):
        if self.top == len(self.array):
            self.expand()
        self.array[self.top] = value
        self.top += 1
#top 记录最大的idx
    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        value = self.array[self.top - 1]
        self.array[self.top - 1] = None
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.array[self.top]

    def expand(self):
        """
         expands size of the array.
         Time Complexity: O(n)
        """
        newArray = [None] * len(self.array) * 2 # double the size of the array
        for i, element in enumerate(self.array):
            newArray[i] = element
        self.array = newArray

    def __iter__(self):
        probe = self.top - 1
        while True:
            if probe < 0:
                raise StopIteration
            yield self.array[probe]
            probe -= 1

class StackNode(object): 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack(AbstractStack):
    def __init__(self):
        AbstractStack.__init__(self)
        self.head = None

    def push(self, value):
        node = StackNode(value)
        node.next = self.head
        self.head = node
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        value = self.head.value
        self.head = self.head.next
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.head.value

    def __iter__(self):
        probe = self.head
        while True:
            if probe is None:
                raise StopIteration
            yield probe.value
            probe = probe.next
            
### $1    
def is_valid(s):
    stack = []
    dic = { ")":"(",
            "}":"{",
            "]":"["}
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack == []:
                return False
            s = stack.pop()
            if dic[char] != s:
                return False
    return stack == []


#if __name__ == "__main__":
#    paren = "[]"
#    print(paren, is_valid(paren))
#    paren = "[]()[]"
#    print(paren, is_valid(paren))
#    paren = "[[[]]"
#    print(paren, is_valid(paren))
#    paren = "{([])}"
#    print(paren, is_valid(paren))
#    paren = "(}"
#    print(paren, is_valid(paren))

### $2 就是顺着str一个个看if即可。

def simplify_path(path):
    """
    :type path: str
    :rtype: str
    """
    skip = set(['..','.',''])
    stack = []
    paths = path.split('/')
    print "paths....",paths
    for tok in paths:
        if tok == '..':
            if stack:
                stack.pop()
        elif tok not in skip:
            stack.append(tok)
    return '/' +'/'.join(stack)

#p = '/my/name/is/..//keon'
#path = "/a/./b/../../c/"
#print(simplify_path(path))
#print(simplify_path(p))



### $3
"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
class Interval(object):
    def __init__(self,l=0,r=0):
        self.start = l
        self.end = r
        
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out

def print_intervals(intervals):
    res = []
    for i in intervals:
        res.append('['+str(i.start)+','+str(i.end)+']')
    print("".join(res))

#if __name__ == "__main__":
#    given = [[1,3],[2,6],[8,10],[15,18]]
#    intervals = []
#    for l, r in given:
#        intervals.append(Interval(l,r))
#    print_intervals(intervals)
#    print_intervals(merge(intervals))       

    

### $4
def length_longest_path(input):
    currlen, maxlen = 0, 0    # running length and max length
    stack = []    # keep track of the name length
    for s in input.split('\n'):
        print("---------")
        print("<path>:", s)
        depth = s.count('\t')    # the depth of current dir or file
        print("depth: ", depth)
        print("stack: ", stack)
        print("curlen: ", currlen)
        while len(stack) > depth:    # go back to the correct depth
            currlen -= stack.pop()
        stack.append(len(s.strip('\t'))+1)   # 1 is the length of '/'
        currlen += stack[-1]    # increase current length
        print("stack: ", stack)
        print("curlen: ", currlen)
        if '.' in s:    # update maxlen only when it is a file
            maxlen = max(maxlen, currlen-1)    # -1 is to minus one '/'
    return maxlen

st= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdirectory1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
st2 = "a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt"
print("path:", st2)

print "answer:", length_longest_path(st2)


































            
            
            
            
            
            
            
            
    