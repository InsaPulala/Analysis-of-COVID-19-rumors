#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#   LYS
#   2020/7/3 10:10
#   DFS.py

import requests
from bs4 import BeautifulSoup
import re
import time


def my_crawler(seed):
    List_of_links = []
    parent_list = []
    child_list = []
    parent_list.append(seed)
    count = 1
    depth = 1
    x = 0
    while (len(parent_list) < 50):
        if (depth > 1):
            break
        List_of_links = go_crawl(parent_list[x])
        for i in List_of_links:
            if i not in child_list:
                child_list.append(i)
        for j in child_list:
            if j not in parent_list and len(parent_list) < 1000:
                parent_list.append(j)
                count = count + 1
        if (len(child_list) == count):
            child_list = []
            depth = depth + 1
            # print(depth)
        # print(len(parent_list))
        x = x + 1

    number = 1
    f = open('..data/one.txt', 'w')
    for i in parent_list:
        row = str(number) + " " + str(i) + "\n"
        f.write(row)
        number += 1
    f.close()


def go_crawl(url):
    wikistring = ""
    totallinks, child_links = [], []
    time.sleep(1)
    seedinfo = requests.get(url)
    raw_data = seedinfo.text
    soup = BeautifulSoup(raw_data, 'html.parser')
    for link in soup.find_all('a', {'href': re.compile("http://")}):
        link_text = wikistring + link.get('href')
        refine_text = link_text.split('#')
        totallinks.append(str(refine_text[0]))
    for i in totallinks:
        if i not in child_links:
            if len(i) > 1:
                child_links.append(i)
    return child_links


if __name__ == '__main__':
    my_crawler('http://www.piyao.org.cn/2020yqpy/')
