#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#   LYS
#   2020/7/4 16:18
#   wordcloud.py

'''
词云图分析
'''

import jieba
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
import PIL

title = []
date = []
tag = []
with open("../data/0704_data.txt", 'r', encoding='utf-8')as f:
    for line in f:
        l = line.strip().split('\t')
        if len(l) > 2:
            title.append(l[0])
            date.append(l[1])
            tag.append(l[2])

txt = ''
for i in title:
    txt += i
pic = PIL.Image.open('../data/1.jpg')
MASK = np.array(pic)
w = wordcloud.WordCloud(width=800, height=600, max_font_size=80,
                        max_words=200, repeat=False, mode='RGBA',
                        background_color='white', mask=MASK,
                        font_path=r'D:\python_learn\ku\msyh.ttf')
w.generate(''.join(jieba.lcut(txt)))
w.to_file('../d/all.png')
plt.figure('../d/all.png')  # 图片显示的名字
plt.imshow(w)
plt.axis('off')  # 关闭坐标
plt.show()

a = {}
b = {}
c = {}
for i in range(len(date)):
    if tag[i] == '1':
        if a.__contains__([date[i]][0]):
            a[date[i]] += 1
        else:
            a[date[i]] = 1
    elif tag[i] == '0':
        if b.__contains__([date[i]][0]):
            b[date[i]] += 1
        else:
            b[date[i]] = 1
    else:
        if c.__contains__([date[i]][0]):
            c[date[i]] += 1
        else:
            c[date[i]] = 1

# write in excel
import xlwt


def write_excel_xls(path, sheet_name, a):
    index = len(a)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheetname=sheet_name)  # 在工作簿中新建一个表格
    # for i in range(0, index):
    #     for j in range(0, len(value[i])):
    #         sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    i = 0
    for item in a:
        sheet.write(len(a)-1-i, 0, item)
        sheet.write(len(a)-1-i, 1, a[item])
        i += 1
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


path = "./d/tag.xls"
write_excel_xls(path, "date_tag", a)

#将abc数据分别写入文件处理


###########0706
i=1
title2=[]
title3=[]
title4=[]
title5=[]
title6=[]

with open('../d/0706_data.txt','r',encoding='utf-8') as f:
    for line in f:
        i+=1
        l = line.strip().split('\t')
        if i<336:
            if l[2] == '1':
                title2.append(l[0])
        elif 336<=i<567:
            if l[2] == '1':
                title3.append(l[0])
        elif 567<=i<747:
            if l[2] == '1':
                title4.append(l[0])
        elif 747<=i<867:
            if l[2] == '1':
                title5.append(l[0])
        else:
            if l[2] == '1':
                title6.append(l[0])

#####################
words = jieba.lcut_for_search(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(3):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
