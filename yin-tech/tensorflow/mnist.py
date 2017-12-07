# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:59:22 2017

@author: yuqing.wang1
"""

#import corss_validation
#from sklearn  import *
#
#iris = tf.contrib.learn.datasets.load_dataset('iris')
#print(iris.data.shape,iris.target.shape)
#
#x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
#print(x_test.shape)
#
#feature_columns = tf.contrib.learn.infer_real_valued_columns_from_input(x_train)
#print(feature_columns)
#
#classifier = tf.contrib.learn.DNNClassifier(feature_columns = feature_columns, hidden_units = [10,20,10],n_classes =3)
#
#classifier.fit(x_train,y_train,steps = 200)
#predictions = list(classifier.predict(x_test,as_iterable = True))
#score = metrics.accuracy_score(y_test,predictions)
#
#print('Accuracy: {0:f}'.format(score))

#a = tf.constant([2,2],name="a")
#b=tf.constant([3,6],name="b")
#x=tf.add(a,b,name="add")
#with tf.Session() as sess:
#    writer = tf.summary.FileWriter('/log_for_tfsession',sess.graph)
#    print(sess.run(x))
#writer.close()
import tensorflow as tf
import time
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
MNIST = input_data.read_data_sets("/data/mnist",one_hot=True)

learning_rate=0.1
batch_size=128
n_epochs=25

x = tf.placeholder(tf.float32,[batch_size,784],name="image")
y = tf.placeholder(tf.float32,[batch_size,10],name = "label")

w=tf.Variable(tf.random_normal(shape=[784,10], stddev =0.01),name="weight")
b=tf.Variable(tf.zeros([1,10]),name="bias")
logits = tf.matmul(x,w)+b

entropy = tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = y)
loss = tf.reduce_mean(entropy)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    
    n_batches = int(MNIST.train.num_examples/batch_size)
    
    for i in range(n_epochs):
        x_batch,y_batch = MNIST.train.next_batch(batch_size)
        sess.run([optimizer,loss,logits],feed_dict={x:x_batch,y:y_batch})
        
    total_correct_preds = 0
    t_batches = int(MNIST.test.num_examples/batch_size)
   
    for i in range(t_batches):
        x_batch,y_batch = MNIST.test.next_batch(batch_size)
        _, loss_batch, logits_batch =sess.run([optimizer,loss,logits],feed_dict={x:x_batch,y:y_batch})
        
        preds = tf.nn.softmax(logits_batch)
        
        correct_preds = tf.equal(tf.argmax(preds,1),tf.argmax(y_batch,1))
        accuracy = tf.reduce_sum(tf.cast(correct_preds,tf.float32))
        
        total_correct_preds += sess.run(accuracy)
    
    print("accuracy{0}".format(total_correct_preds/MNIST.test.num_examples))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        