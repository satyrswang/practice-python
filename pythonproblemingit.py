# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:34:34 2016

@author: w
"""
#++++++++++++++++++++++++++++++++++++++++++++++pro0001
import re
import string
import random

map ={}
#pattern = re.compile(r'([a-z0-9A-Z]{4}-){3}([a-z0-9A-Z]{4})')
def id_generator(size = 4 , chars = string.ascii_uppercase+string.digits+string.ascii_lowercase):
    list =[]
    #[random.choice(chars) for _ in range(size)]
    #(random.choice(chars) for _ in range(4))
    for i in range(4):
        #chars = string.ascii_uppercase+string.digits+string.ascii_lowercase
        a =''.join(random.choice(chars) for _ in range(size))
        # print(a)
        list.append(a)
    return list

#print (id_generator())
#chars 可以是大写，小写或者数字 随机函数random.choice(chars)

for i in range(200):
    id='-'.join(id_generator())
    while id in map.values():
        id='-'.join(id_generator())
    map[i] = id
print map
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import uuid

def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))
        print uuid_key
        key_list.append(str(uuid_key).replace('-',''))
        print key_list
    return key_list
#==============================================================================
#     
# print generate_key()
#     
# print uuid.NAMESPACE_DNS ##const
# print uuid.uuid1()
# 
#==============================================================================

#import sys sys.path.append('C:\Python27\Lib\site-packages')    
import pymysql

import string
import random

#==============================================================================
# use activation_code; 
# CREATE TABLE MyGenerateCode 
# (   SerialNumber int(5) NOT NULL, 
#     ActivationCode char(30) NOT NULL 
# ); 
#  ALTER TABLE MyGenerateCode ADD PRIMARY KEY (SerialNumber); 
#==============================================================================
map ={}
##SQLAlchemy
conn = pymysql.connect(host='127.0.0.1', port=3306, user='wyq',passwd ='1234', db='activation_code')
cursor = conn.cursor()
def id_generator(size = 4 , chars = string.ascii_uppercase+string.digits+string.ascii_lowercase):
    list =[]
    for i in range(4):
        #chars = string.ascii_uppercase+string.digits+string.ascii_lowercase
        a =''.join(random.choice(chars) for _ in range(size))
        # print(a)
        list.append(a)
    return list

for i in range(200):
    id='-'.join(id_generator())
    while id in map.values():
        id='-'.join(id_generator())
    map[i] = id   
    cursor.execute('insert into mygeneratecode values(%d,%r)'%(i,map[i]))

conn.commit()
cursor.close()
conn.close()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
#==============================================================================
# import sys
# def word_count(file_path):
#     file_object = open(file_path, 'r')
#     word_num =0
#     for line in file_object:
#         line_list = line.split()
#         word_num += len(line_list)
#     file_object.close()
#     return word_num
#     
# if _name_=="_main_":
#     if len(sys.argv)< =1:
#         print "more than one parameter."
#     else:
#         for infile in sys.argv[1:]:
#             try:
#                 print"total number is %d" word_count(infile)
#             except IOError:
#                 print "cannot open file"
#                 pass
# 
#=============================================================================运不出来
import io
import operator


def get_count_table(ignore=[',', '.', ':', '!', '?', '”', '“', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], lower=True):
    txt = open('D://pythonproingit//0004.txt','r')
    words =[]
    for line in txt:
        for i in ignore:
            line = line.replace(i, ' ')
        if lower:
            line = line.lower()
        words.append(line.split(' '))
    dic = {}
    
  #  print type(words)
    for word in words:
        if word is '':
            continue
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

print get_count_table()
result = sorted(get_count_table().items(), key=operator.itemgetter(1), reverse=True)
for item in result:
    print item[0], item[1]

txt =open('D://pythonproingit//0004.txt','r')
print type(txt)


import re
def num(path):
    path ='D://pythonproingit//0004.txt'
    with open(path, 'r') as file:
        data=file.read()
        print data
        words=re.compile('[a-zA-Z0-9]+') #compile好像是必须用的，用来格式转换什么的,然后才能进行匹配之类的操作
        dict={}

        for x in words.findall(data):
            if x not in dict:
                dict[x]=1
            else:
                dict[x]+=1

        print dict


import re,sys,os
path = os.path.split(os.path.realpath(__file__))[0]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Fliter = re.compile("[^A-Za-z-\']|((?<![A-Za-z])[-\'])|([-\'](?![A-Za-z]))")
Divider = re.compile("\s")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
File = open('D://pythonproingit//0004.txt').read()
Data =  Divider.split(Fliter.sub(" ",File))
Dict = {}
for i in Data:
	j = i.lower()
	try:
		Dict[j]+=1
	except KeyError:
		Dict[j] =1
	except:
		raise 
for i in  Dict.items():
	print "%s:%s"%i


















