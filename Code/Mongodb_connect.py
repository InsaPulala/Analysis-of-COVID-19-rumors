# -*- coding:utf-8 -*-
# ! usr/bin/env python3

'''
liuyusha
2020/5/8
链接数据库 MongoDB，插入数据
考虑爬虫多线程

'''

import pymongo

# 连接数据库
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['test01']
collection = db['a01']

# 插入一条数据
data = {'id': 123, 'name': 'kingname', 'age': 20, 'salary': 999999}
collection.insert_one(data)

# 插入多条数据
more_data = [
		{'id': 2, 'name': '张三', 'age': 10, 'salary': 0},
		{'id': 3, 'name': '李四', 'age': 30, 'salary': -100},
		{'id': 4, 'name': '王五', 'age': 40, 'salary': 1000},
        {'id': 5, 'name': '外国人', 'age': 50, 'salary': '未知'}]
collection.insert_many(more_data)

content = collection.find()
content = collection.find({'age': 29})
content = collection.find({'age': 29}, {'_id': 0,'name': 1, 'salary': 1})
# print(content)  #<pymongo.cursor.Cursor object at 0x0000013910BD4668>