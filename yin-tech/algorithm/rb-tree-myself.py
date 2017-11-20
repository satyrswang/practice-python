# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:30:30 2017

@author: yuqing.wang1
"""
class RBTree(object):
    def __init__(self):
        self.root = None

    class node(object):
        def __init__(self,key,v=None,N):
            self.key = key
            self.v= v
            self.l = None
            self.r= None
            self.color = False #black
            self.N=N  #nodes of subtree 
            self.p =None
            
    def _rotate_left(self,h): 
        x = h.r
        h.r = x.l
        x.l = h
        x.color,x.N=h.color,h.N
        h.color,h.N = True, self._size(h.l)+self._size(h.r)+1
        return x  #给定需要左旋的node，返回旋转后最高的node--替代了传入node位置的新node
    
    def _rotate_right(self,h):
        x = h.l
        h.l=  x.r
        x.r=h
        x.color,x.N=h.color,h.N
        h.color,h.N = True, self._size(h.l)+self._size(h.r)+1
        return x
    
    def _flip_color(self,h):
        h.l.color = not h.l.color
        h.r.color = not h.r.color
        h.color = not h.color
        
        
    
    def _get(self,x,k):
        v =None
        while x is not None:
            if x.key< k :
                x = x.r
            else:
                x =x.l
            if x.key ==k:
                v = x.v      
        return v #从x出开始向下搜索
    def is_red(self,x):
        return False if not x else x.color
    def is_black(self,x):
        return True if not x else not x.color
    
    def _put(self,h,k,v):
        if h is None:
            return self.node(k,v,1)  #如果是最后则返回到h.l或者h.r中
        if k<h.k:
            h.l =  self._put(h.l,k,v)
        elif k>h.k:
            h.r = self._put(h.r,k,v)
        elif k == h.k:
            h.val = val
        if self.is_red(h.l.l) and self.is_red(h.l):
            self._rotate_right(h)
        if self.is_red(h.l) and self.is_black(h.r):
            self._rotate_left(h.r)
        if self.is_red(h.r) and self.is_red(h.l):
            self._flip_color(h)
        h.N = self.__size(h.left) + self.__size(h.right) + 1
        return h
            
         
    def _index(self,h,key):
        if not h: 
            return None
        if h.k <key:
            return self._index(h.r,key) + self._size(h.l)+1
        elif h.k> key:
            return self._index(h.l,key)
            
        else:
            return self._size(h.l)
        
        
        

        

#    def INSERT(self, val):
#
#        z = RBTnode(val)
#        y = None
#        x = self.root
#        while x is not None:
#            y = x
#            if z.val < x.val:
#                x = x.left
#            else:
#                x = x.right
#
#        z.PAINT(RED)
#        z.parent = y
#
#        if y is None:
#            # 插入z之前为空的RBT
#            self.root = z
#            self.INSERT_FIXUP(z)
#            return
#
#        if z.val < y.val:
#            y.left = z
#        else:
#            y.right = z
#
#        if y.color == RED:
#            # z的父节点y为红色，需要fixup。
#            # 如果z的父节点y为黑色，则不用调整
#            self.INSERT_FIXUP(z)
#
#        else:
#            return
#
#    def INSERT_FIXUP(self, z):
#        # case 1:z为root节点
#        if z.parent is None:
#            z.PAINT(BLACK)
#            self.root = z
#            return
#
#        # case 2:z的父节点为黑色
#        if z.parent.color == BLACK:
#            # 包括了z处于第二层的情况
#            # 这里感觉不必要啊。。似乎z.parent为黑色则不会进入fixup阶段
#            return
#
#        # 下面的几种情况，都是z.parent.color == RED:
#        # 节点y为z的uncle
#        p = z.parent
#        g = p.parent  # g为x的grandpa
#        if g is None:
#            return
#            #   return 这里不能return的。。。
#        if g.right == p:
#            y = g.left
#        else:
#            y = g.right
#
#        # case 3-0:z没有叔叔。即：y为NIL节点
#        # 注意，此时z的父节点一定是RED
#        if y == None:
#            if z == p.right and p == p.parent.left:
#                # 3-0-0:z为右儿子,且p为左儿子，则把p左旋
#                # 转化为3-0-1或3-0-2的情况
#                self.LEFT_ROTATE(p)
#                p, z = z, p
#                g = p.parent
#            elif z == p.left and p == p.parent.right:
#                self.RIGHT_ROTATE(p)
#                p, z = z, p
#
#            g.PAINT(RED)
#            p.PAINT(BLACK)
#            if p == g.left:
#                # 3-0-1:p为g的左儿子
#                self.RIGHT_ROTATE(g)
#            else:
#                # 3-0-2:p为g的右儿子
#                self.LEFT_ROTATE(g)
#
#            return
#
#        # case 3-1:z有黑叔
#        elif y.color == BLACK:
#            if p.right == z and p.parent.left == p:
#                # 3-1-0:z为右儿子,且p为左儿子,则左旋p
#                # 转化为3-1-1或3-1-2
#                self.LEFT_ROTATE(p)
#                p, z = z, p
#            elif p.left == z and p.parent.right == p:
#                self.RIGHT_ROTATE(p)
#                p, z = z, p
#
#            p = z.parent
#            g = p.parent
#
#            p.PAINT(BLACK)
#            g.PAINT(RED)
#            if p == g.left:
#                # 3-1-1:p为g的左儿子，则右旋g
#                self.RIGHT_ROTATE(g)
#            else:
#                # 3-1-2:p为g的右儿子，则左旋g
#                self.LEFT_ROTATE(g)
#
#            return
#
#
#        # case 3-2:z有红叔
#        # 则涂黑父和叔，涂红爷，g作为新的z，递归调用
#        else:
#            y.PAINT(BLACK)
#            p.PAINT(BLACK)
#            g.PAINT(RED)
#            new_z = g
#            self.INSERT_FIXUP(new_z)
#   
##    def _size(self,h):
##        c = 1
##        while h.l is not None:
##            c = c+1
##            h = h.l
##        while h.r is not None:
##            c = c+1
##            h = h.r
##        return c
##            
#     
#        
    