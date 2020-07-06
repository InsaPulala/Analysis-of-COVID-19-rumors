#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
liuyusha
2020/5/22
链接网页首页，获取谣言页面链接
进入谣言页面
'''

from urllib import request
from bs4 import BeautifulSoup
import re
import os
import bs4
import time
import string
import requests
import argparse

url = "http://www.piyao.org.cn/2020yqpy/"

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

    list = soup.find_all('a')
    print(list)
    # for li in list:
    #     title_node = (li.find('a'))
    # link = title_node["href"]
    # print(link)
    # return soup

# def starttag(url):
#
#     soup = page_parser(url)
#     # for i, row in enumerate(soup.body.findAll('ul', attrs={"class": "list"})):
#     #     movies_dict = {}
#     #     for j, col in enumerate(row.findAll('li', attrs={"class": "tag1"})):
#     #         print(j, col)
#     f = open('../data/html.txt',  'w+', encoding='utf-8')
#     f.write('{0}'.format(soup))
#     f.close()


# def get_connection():
#     start_time = time.time()
#
#     soup = page_parser(url)
#     t1 = soup.find('ul', attrs={'class': "list"})
#     print(t1)
#
#     end_time = time.time()
#
#     print('已处理, 耗时: {0:.2f}s.'.format(end_time - start_time))


if __name__ == "__main__":
    page_parser(url)