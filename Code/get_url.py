#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#   LYS
#   2020/6/3 9:59
#   get_url.py

'''连接导数据网页，获取连接'''

from urllib import request
from bs4 import BeautifulSoup
import re
import os
import bs4
import time
import requests
import re

url = 'http://qc.wa.news.cn/nodeart/list?nid=11215616&pgnum='
url2 = '&cnt=10&attr=63&tp=1&orderby=1&callback=jQuery112401909107050038461_1591149287011&_=15911492870'
out = "../data/urldata.txt"

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


def page_parser():
    dict = []
    for x in range(200):
        url3 = url + str(x) +url2 + str(x+11)
        print(x)
        html = get_HTMLText(url3)
        soup = BeautifulSoup(html, 'html.parser')
        s = str(soup)
        urls = re.findall('[a-zA-Z0-9/\._]+\.htm', s)

        for k in urls:
            dict.append(k)
    set_url = set(dict)
    print(dict)
    return set_url


def get_connection():
    start_time = time.time()
    wf = open(out, 'w', encoding='utf-8')

    urls = page_parser()

    for u in urls:

        wf.write('{0}'.format(u)+'\n')

    wf.close()
    end_time = time.time()
    print('已处理, 耗时: {0:.2f}s.'.format(end_time - start_time))




if __name__ == "__main__":
    get_connection()
