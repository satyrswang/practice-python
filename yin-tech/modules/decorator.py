# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 10:50:09 2017

@author: yuqing.wang1
"""
import logging
#1装饰 函数可以作为参数、返回值、赋值给其他、定义在另一个函数中

# 减少代码,代替某句foo = use_logging(foo) 

def use_logging(func):

    def wrapper(name):
        logging.warn("%s is running" % func.__name__)
        return func(name)   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo(name):
    print('i am % s' % name)

foo = use_logging(foo) 
#只传递了wrapper对象 这不是很聪明的做法吗！
name = "wang"
foo(name)   #执行


@use_logging  #相当于foo = use_logging(foo) 
def foo(name):
    print("i am foo")

#只需要定义时加上 我对这个函数还要有一定操作
#插入日志、性能测试、事务处理、缓存、权限校验等场景  这些切面需求 --类似于后台进程

#装饰器不知道 foo 到底有多少个参数时，我们可以用 *args 来代替：
#如果 foo 函数还定义了一些关键字参数呢

def wrapper(*args, **kwargs):
        # args是一个数组，kwargs一个字典
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
#return wrapper
#带参数的装饰

def user_log(level):
    def decorator(func):
        def wrapper(*args,**kwargs):#告诉wrapper 有关键字参数
            if level == warn:
                logging.warn("%s warn" %func.__name__)
            else:
                logging.info("%s info" %func.__name__)
            return func(*args)
        return wrapper
    return decoraor        
#即在外面再套一层函数，传入装饰器的参数 并在wrapper中使用

#@use_logging(level="warn")等价于@decorator
#是我们调用foo函数时，不再只是内容，而且包含了装饰器中的wrapper或类中的__call__函数
class Foo(object):
    def __init__(self,func):
        self._func = func
    def __call__(self):
        print "i got the FOOCLASS"
        self._func()
@Foo
def foo():
    print "foofunc"

foo() #这里的调用是对Foo中的__call__调用

#元信息
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__      # 输出 'f'
        print func.__doc__       # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x


#多个装饰器
#@a
#@b
#@c
#def f ():
#    pass
#f = a(b(c(f)))


























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        