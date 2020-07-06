#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#   LYS
#   2020/6/26 21:19
#   get_inmongo.py

from urllib import request
from bs4 import BeautifulSoup
import re
import os
import bs4
import time
import requests
import re
import pymongo


def get_HTMLText(url):
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        'Cookie': 'ncbi_sid=47EF8993E4BE3193_0587SID; _ga=GA1.2.780797648.1582031800; pmc.article.report=; books.article.report=; _gid=GA1.2.288894097.1585885708; QSI_HistorySession=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2F~1585922167314; WebEnv=1zmWDqnmAX_v2YHx4rlkrq3Yhg3ZCIGss-UrAFg-SZPikri1ywXU5zjN2MwUgcrtonBWnvUs1EJyzzVzB2wC14pFkl6eh-708Vl%4047EF8993E4BE3193_0587SID; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgCIAYBC2ArAMIDMRAHGdmQCwCcAbEbm7mbgwOxEBiDWvzoA6AIwiAtnEogANCACuAOwA2AewCGqZVAAeAF0ygATJhABzAI6KoEAJ7yQZc5tWqndcwGcomiADGiE5E5hCKqlAAvIj2qBCaAD6oAEZRYIopklCoid7qioHRJMgGmgbI6soAylDK+RB5galRAAqZALI5iQb2YNH+FQGRiU5iXli+/kFOJrjmeISkFNS0jCzsHFy8AkJ8ohLSsgomYubWtg4YbqoYU4GIGOGRMXEJyWkZWd35hQHFpXKlRqdQaTQCLXaKS6uV6/Sig2QwygoxOZiwAHcsSJlAEUsgcapJDjkIgRBZ1DBZgxzGIGHMnJxabhKPMFGQzlg6Qz2eiQGJcEQXOyXFgDOEoIyJiBxbZGbIsIyaVgiELBTSFHR5lgmDwGJRQprRSBcCITJQRMKQHRpSoNNpdIZPKEsGyQELaawQtKGFqQkxaUwOCFuLSvAomJz+dxuLIAL5xoA'}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


def page_parser(url):
    html = get_HTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_connection(url, collection):
    soup = page_parser(url)

    try:
        title = soup.select("div.con_tit > h2")[0].text  # '\r\n电影院等密闭式娱乐休闲场所低中高风险地区均暂不开业\r\n'
        date = soup.select("div.con_tit > p >span")[0].text  # '发布时间：  2020-04-10 14:32:12'
        content = soup.select("div.con_txt > p")[0].text
        # '\u3000\u3000日前，国务院联防联控机制印发通知，落实分区分级防控要求，推进生产生活秩序逐步恢复，进一步做好重点场所、重点单位、重点人群的疫情防控工作。明确了密闭式娱乐、休闲场所低、中、高风险地区均暂不开业，具体要求由各地依据本地疫情形势研究确定。建议低风险地区生活服务类场所在做好室内通风、环境清洁消毒、人员健康监测的前提下正常营业；中、高风险地区生活服务类场所应当限制人员数量，减少人群聚集。（记者 王秉阳）'

        sourse = soup.select("div.con_tit > p")[0].text  # '\r\n来源： 新华社“新华视点”微博发布时间：  2020-04-10 14:32:12\n'
    except:
        pass
    else:
        t = title.strip()
        # print(t)  # title
        s = sourse.strip()
        # print(s)  # sourse

        d = re.findall(r'[0-9-]{10}', date.strip())
        d = d[0]
        # print(d)  # date
        c = content.strip()
        # print(c)  # content

        line = {'title': t, 'date': d, 'sourse': s, 'content': c, 'link': url}
        # print(line)
        collection.insert_one(line)


def page_url(url, url2):
    dict = []
    for x in range(0, 100):
        url3 = url + str(x + 1) + url2 + str(x)
        # print(x)
        html = get_HTMLText(url3)
        soup = BeautifulSoup(html, 'html.parser')
        s = str(soup)
        urls = re.findall('[a-zA-Z0-9/\._]+\.htm', s)

        for k in urls:
            dict.append(k)
    set_url = set(dict)
    # print(dict)
    return set_url


if __name__ == "__main__":
    new = []
    url = 'http://qc.wa.news.cn/nodeart/list?nid=11215616&pgnum='
    url2 = '&cnt=10&attr=63&tp=1&orderby=1&callback=jQuery11240023171643210465165_1593738848999&_=1593738849'
    # 1593738849000
    urls = page_url(url, url2)
    i = 0
    URL = 'http://www.piyao.org.cn/2020-'
    # 连接数据库
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['News']
    collection = db['a03']
    for line in urls:
        u = URL + line
        get_connection(u, collection)
