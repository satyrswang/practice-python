# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:34:34 2016
@author: w
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    from utils import cheese# 下面附上utils模块的实现
    cheese()
    return 'Yet another hello!'

if __name__ == '__main__':
    app.run()

