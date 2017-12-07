#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:05:51 2017

@author: wyq
"""
#
#import tensorflow as tf
#
#g = tf.Graph()
#
#with g.as_default():
#    a = tf.placeholder(tf.float32, name="a")
#    b = tf.placeholder(tf.float32, name="b")
#    c = a + b
#    
#a = [node.name for node in g.as_graph_def().node]
#print(a)

#from graphviz import Digraph
#dot = Digraph()
#
#for n in g.g.as_graph_def().node:
#    dot.node(n.name,label=n.name)
#    for i in n.input:
#        dot.edge(i,n.name)

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import pygraphviz as pgv
# strict (no parallel edges)
# digraph
# with attribute rankdir set to 'LR'
A=pgv.AGraph(directed=True,strict=True,rankdir='LR')
# add node 1 with color red
A.add_node(1,color='red') 
A.add_node(5,color='blue')
# add some edges
A.add_edge(1,2,color='green')
A.add_edge(2,3)
A.add_edge(1,3)
A.add_edge(3,4)
A.add_edge(3,5)
A.add_edge(3,6)
A.add_edge(4,6)
# adjust a graph parameter
A.graph_attr['epsilon']='0.001'
print(A.string()) # print dot file to standard output
A.layout('dot') # layout with dot
A.draw('foo.ps') # write to file