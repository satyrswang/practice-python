# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 17:33:55 2017

@author: yuqing.wang1
"""
"""
   若*p既有左子树又有右子树，此时有两种处理方法：
一是先直接令PL为*f的左子树，再令PR为PL子树中最右孩子的右子树。PL子树中最右孩子即为PL子树中最大的结点。
二是令*p的直接前驱(或直接后继)代替*p，然后从二叉排序树中删除它的直接前驱(或直接后继)。
   *p的直接前驱为PL子树中最右孩子，大小仅次于*p；*p的直接后继为PR子树中最左孩子，大小仅大于*p。
"""
class TreeNode:
	def __init__(self,val):
		self.val=val;
		self.left=None;
		self.right=None;

def insert(root,val):
	if root is None:
		root=TreeNode(val);
	else:
		if val<root.val:
			root.left=insert(root.left,val);   #递归地插入元素
		elif val>root.val:
			root.right=insert(root.right,val);  
	return root;

def query(root,val):
	if root is None:
		return ;
	if root.val is val:
		return 1;
	if root.val <val:
		return query(root.right,val);  #递归地查询
	else:  
		return query(root.left,val);
def findmin(root):
	if root.left:
		return findmin(root.left);
	else:
		return root;
	
def delnum(root,val):
	if root is None:
		return ;
	if val<root.val:
		return delnum(root.left,val);
	elif val>root.val:
		return delnum(root.right,val);
	else:                                             # 删除要区分左右孩子是否为空的情况
		if(root.left and root.right):
			
			tmp=finmin(root.right);             #找到后继结点
			root.val=tmp.val;
			root.right=delnum(root.right,val);    #实际删除的是这个后继结点*****************************************
#删除如何递归
		else:
			if root.left is None:
				root=root.right;
			elif root.right is None:
				root=root.left;
	return root;
				
				
#测试代码			
root=TreeNode(3);
root=insert(root,2);
root=insert(root,1);
root=insert(root,4);

#print query(root,3);
print query(root,1);
root=delnum(root,1);
print query(root,1);

