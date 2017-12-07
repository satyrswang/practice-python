#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:43:47 2017

@author: wyq
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pickle
import numpy as np
import pandas as pd
from collections import OrderedDict

org_train_file = 'training.1600000.processed.noemoticon.csv'
org_test_file = 'testdata.manual.2009.06.14.csv'

# 提取文件中有用的字段
def usefull_filed(org_file, output_file):
	output = open(output_file, 'w')
	with open(org_file, buffering=10000, encoding='latin-1') as f:
		try:
			for line in f:                # "4","2193601966","Tue Jun 16 08:40:49 PDT 2009","NO_QUERY","AmandaMarie1028","Just woke up. Having no school is the best feeling ever "
				line = line.replace('"', '')
				clf = line.split(',')[0]   # 4
				if clf == '0':
					clf = [0, 0, 1]  # 消极评论
				elif clf == '2':
					clf = [0, 1, 0]  # 中性评论
				elif clf == '4':
					clf = [1, 0, 0]  # 积极评论

				tweet = line.split(',')[-1]
				outputline = str(clf) + ':%:%:%:' + tweet
				output.write(outputline)  # [0, 0, 1]:%:%:%: that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D
		except Exception as e:
			print(e)
	output.close()  # 处理完成，处理后文件大小127.5M

usefull_filed(org_train_file, 'training.csv')
usefull_filed(org_test_file, 'tesing.csv')

# 创建词汇表
def create_lexicon(train_file):
	lex = []
	lemmatizer = WordNetLemmatizer()
	with open(train_file, buffering=10000, encoding='latin-1') as f:
		try:
			count_word = {}  # 统计单词出现次数
			for line in f:
				tweet = line.split(':%:%:%:')[1]
				words = word_tokenize(line.lower())
				for word in words:
					word = lemmatizer.lemmatize(word)
					if word not in count_word:
						count_word[word] = 1
					else:
						count_word[word] += 1

			count_word = OrderedDict(sorted(count_word.items(), key=lambda t: t[1]))
			for word in count_word:
				if count_word[word] < 100000 and count_word[word] > 100:  # 过滤掉一些词
					lex.append(word)
		except Exception as e:
			print(e)
	return lex

lex = create_lexicon('training.csv')

with open('lexcion.pickle', 'wb') as f:
	pickle.dump(lex, f)


"""
# 把字符串转为向量
def string_to_vector(input_file, output_file, lex):
	output_f = open(output_file, 'w')
	lemmatizer = WordNetLemmatizer()
	with open(input_file, buffering=10000, encoding='latin-1') as f:
		for line in f:
			label = line.split(':%:%:%:')[0]
			tweet = line.split(':%:%:%:')[1]
			words = word_tokenize(tweet.lower())
			words = [lemmatizer.lemmatize(word) for word in words]

			features = np.zeros(len(lex))
			for word in words:
				if word in lex:
					features[lex.index(word)] = 1  # 一个句子中某个词可能出现两次,可以用+=1，其实区别不大
			
			features = list(features)
			output_f.write(str(label) + ":" + str(features) + '\n')
	output_f.close()


f = open('lexcion.pickle', 'rb')
lex = pickle.load(f)
f.close()

# lexcion词汇表大小112k,training.vec大约112k*1600000  170G  太大，只能边转边训练了
# string_to_vector('training.csv', 'training.vec', lex)
# string_to_vector('tesing.csv', 'tesing.vec', lex)
"""

import os
import random 
import tensorflow as tf
import pickle
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

f = open('lexcion.pickle', 'rb')
lex = pickle.load(f)
f.close()


def get_random_line(file, point):
	file.seek(point)
	file.readline()
	return file.readline()
# 从文件中随机选择n条记录
def get_n_random_line(file_name, n=150):
	lines = []
	file = open(file_name, encoding='latin-1')
	total_bytes = os.stat(file_name).st_size 
	for i in range(n):
		random_point = random.randint(0, total_bytes)
		lines.append(get_random_line(file, random_point))
	file.close()
	return lines


def get_test_dataset(test_file):
	with open(test_file, encoding='latin-1') as f:
		test_x = []
		test_y = []
		lemmatizer = WordNetLemmatizer()
		for line in f:
			label = line.split(':%:%:%:')[0]
			tweet = line.split(':%:%:%:')[1]
			words = word_tokenize(tweet.lower())
			words = [lemmatizer.lemmatize(word) for word in words]
			features = np.zeros(len(lex))
			for word in words:
				if word in lex:
					features[lex.index(word)] = 1
			
			test_x.append(list(features))
			test_y.append(eval(label))
	return test_x, test_y

test_x, test_y = get_test_dataset('tesing.csv')


#######################################################################

n_input_layer = len(lex)  # 输入层

n_layer_1 = 2000     # hide layer
n_layer_2 = 2000    # hide layer(隐藏层)听着很神秘，其实就是除输入输出层外的中间层

n_output_layer = 3       # 输出层


def neural_network(data):
	# 定义第一层"神经元"的权重和biases
	layer_1_w_b = {'w_':tf.Variable(tf.random_normal([n_input_layer, n_layer_1])), 'b_':tf.Variable(tf.random_normal([n_layer_1]))}
	# 定义第二层"神经元"的权重和biases
	layer_2_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_1, n_layer_2])), 'b_':tf.Variable(tf.random_normal([n_layer_2]))}
	# 定义输出层"神经元"的权重和biases
	layer_output_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_2, n_output_layer])), 'b_':tf.Variable(tf.random_normal([n_output_layer]))}

	# w·x+b
	layer_1 = tf.add(tf.matmul(data, layer_1_w_b['w_']), layer_1_w_b['b_'])
	layer_1 = tf.nn.relu(layer_1)  # 激活函数
	layer_2 = tf.add(tf.matmul(layer_1, layer_2_w_b['w_']), layer_2_w_b['b_'])
	layer_2 = tf.nn.relu(layer_2 ) # 激活函数
	layer_output = tf.add(tf.matmul(layer_2, layer_output_w_b['w_']), layer_output_w_b['b_'])

	return layer_output


X = tf.placeholder('float')
Y = tf.placeholder('float')
batch_size = 90

def train_neural_network(X, Y):
	predict = neural_network(X)
	cost_func = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(predict, Y))
	optimizer = tf.train.AdamOptimizer().minimize(cost_func)

	with tf.Session() as session:
		session.run(tf.initialize_all_variables())

		lemmatizer = WordNetLemmatizer()
		saver = tf.train.Saver()
		i = 0
		pre_accuracy = 0
		while True:   # 一直训练
			batch_x = []
			batch_y = []

			#if model.ckpt文件已存在:
			#	saver.restore(session, 'model.ckpt')  恢复保存的session

			try:
				lines = get_n_random_line('training.csv', batch_size)
				for line in lines:
					label = line.split(':%:%:%:')[0]
					tweet = line.split(':%:%:%:')[1]
					words = word_tokenize(tweet.lower())
					words = [lemmatizer.lemmatize(word) for word in words]

					features = np.zeros(len(lex))
					for word in words:
						if word in lex:
							features[lex.index(word)] = 1  # 一个句子中某个词可能出现两次,可以用+=1，其实区别不大
				
					batch_x.append(list(features))
					batch_y.append(eval(label))

				session.run([optimizer, cost_func], feed_dict={X:batch_x,Y:batch_y})
			except Exception as e:
				print(e)

			# 准确率
			if i > 100:
				correct = tf.equal(tf.argmax(predict,1), tf.argmax(Y,1))
				accuracy = tf.reduce_mean(tf.cast(correct,'float'))
				accuracy = accuracy.eval({X:test_x, Y:test_y})
				if accuracy > pre_accuracy:  # 保存准确率最高的训练模型
					print('准确率: ', accuracy)
					pre_accuracy = accuracy
					saver.save(session, 'model.ckpt')  # 保存session
				i = 0
			i += 1


train_neural_network(X,Y)

##predict过程
import tensorflow as tf
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np

f = open('lexcion.pickle', 'rb')
lex = pickle.load(f)
f.close()

n_input_layer = len(lex)  # 输入层

n_layer_1 = 2000     # hide layer
n_layer_2 = 2000    # hide layer(隐藏层)听着很神秘，其实就是除输入输出层外的中间层

n_output_layer = 3       # 输出层
def neural_network(data):
	# 定义第一层"神经元"的权重和biases
	layer_1_w_b = {'w_':tf.Variable(tf.random_normal([n_input_layer, n_layer_1])), 'b_':tf.Variable(tf.random_normal([n_layer_1]))}
	# 定义第二层"神经元"的权重和biases
	layer_2_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_1, n_layer_2])), 'b_':tf.Variable(tf.random_normal([n_layer_2]))}
	# 定义输出层"神经元"的权重和biases
	layer_output_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_2, n_output_layer])), 'b_':tf.Variable(tf.random_normal([n_output_layer]))}

	# w·x+b
	layer_1 = tf.add(tf.matmul(data, layer_1_w_b['w_']), layer_1_w_b['b_'])
	layer_1 = tf.nn.relu(layer_1)  # 激活函数
	layer_2 = tf.add(tf.matmul(layer_1, layer_2_w_b['w_']), layer_2_w_b['b_'])
	layer_2 = tf.nn.relu(layer_2 ) # 激活函数
	layer_output = tf.add(tf.matmul(layer_2, layer_output_w_b['w_']), layer_output_w_b['b_'])

	return layer_output

X = tf.placeholder('float')
def prediction(tweet_text):
	predict = neural_network(X)

	with tf.Session() as session:
		session.run(tf.initialize_all_variables())
		saver = tf.train.Saver()
		saver.restore(session, 'model.ckpt')

		lemmatizer = WordNetLemmatizer()
		words = word_tokenize(tweet_text.lower())
		words = [lemmatizer.lemmatize(word) for word in words]

		features = np.zeros(len(lex))
		for word in words:
			if word in lex:
				features[lex.index(word)] = 1
		
		#print(predict.eval(feed_dict={X:[features]})) [[val1,val2,val3]]
		res = session.run(tf.argmax(predict.eval(feed_dict={X:[features]}),1 ))
		return res


prediction("I am very happe")