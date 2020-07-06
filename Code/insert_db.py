#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#   LYS
#   2020/6/26 20:35
#   insert_db.py
'''
将news2.txt内容存入mongodb News a01
'''

import pymongo

# 连接数据库
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['News']
collection = db['a01']

id = 0

with open('../data/news2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ii = line.strip().split('\t')
        title = ii[0]
        date = ii[1]
        sourse = ii[2]
        content = ii[3]
        link = ii[4]
        s = {'id': id, 'title': title, 'date': date, 'sourse': sourse, 'content': content, 'link': link}
        collection.insert_one(s)
        id += 1
