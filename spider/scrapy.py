#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
#import matplotlib

#print(sorted(sys.modules.keys()))

def create_project_dir(directory):
	if not os.path.exists(directory):
		print("creating directory" + directory)
		os.makedirs(directory)
def create_data_files(project_name,base_url):
	queue = project_name + "/queue.txt"
	crawled  =  project_name + "/crawled.txt"
	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,' ')

def write_file(path,data):
	f = open(path,'w')
	f.write(data)
	f.close()


#create_data_files("thenewboston","https://thenewboston.com/")

def append_tofile(path,data):
	with open(path,'a') as file:
		file.write(dat +'\n')

def delete_file_content(path):
	with open(path,'w'):
		pass

def file_to_set(path):
	result = set()
	with open(path,'rt') as f:
		for line in f:
			result.add(line.replace('\n',''))
	return result

def set_to_file(links,file):
	delete_file_content(file)
	for link in sorted(links):
		append_tofile(file)


















