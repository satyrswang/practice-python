#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:39:03 2017

@author: wyq
"""
#t=0  t=1    t=2  t=3     t=4
#[The, brown, fox, is,     quick]
#[The, red,   fox, jumped, high]

words_in_dataset[0] = [The, The]
words_in_dataset[1] = [brown, red]
words_in_dataset[2] = [fox, fox]
words_in_dataset[3] = [is, jumped]
words_in_dataset[4] = [quick, high]
batch_size = 2, time_steps = 5
#首先是句子的list，list的每个元素为list-句子在该位置的word 初始为0

words_in_dataset = tf.placeholder(tf.float32, [time_steps, batch_size, num_features])
#维度，最长句子长度， 
lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)

hidden_state = tf.zeros([batch_size, lstm.state_size])
current_state = tf.zeros([batch_size, lstm.state_size])
state = hidden_state, current_state
probabilities = []
loss = 0.0
for current_batch_of_words in words_in_dataset:
    # The value of state is updated after processing each batch of words.
    output, state = lstm(current_batch_of_words, state)

    # The LSTM output can be used to make next word predictions
    logits = tf.matmul(output, softmax_w) + softmax_b
    probabilities.append(tf.nn.softmax(logits))
    loss += loss_function(probabilities, target_words)