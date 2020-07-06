# -*- coding:utf-8 -*-
# ! usr/bin/env python3

'''
liuyusha
2020/5/9
链接网页，获取谣言页面信息
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

url = 'http://www.piyao.org.cn/2020-05/08/c_1210609423.htm'

# [^\x00-\xff.0-9].+

# "http://www.piyao.org.cn/2020yqpy/"
# 'http://www.piyao.org.cn/2020-05/08/c_1210609423.htm'

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


def get_connection():
    start_time = time.time()

    soup = page_parser(url)
    t1 = soup.find('div', attrs={'class': "con_tit"})
    # print(t1)

    t2 = soup.find('div', attrs={'class': "con_txt"})
    # print(t2)

    title = t1.find_all('h2')
    print(title)

    date = t1.find_all('p')
    print(date)

    content = t2.find_all('p')
    print(content)

    a = str(title[0])
    b = str(date[0])
    c = str(content)
    print(a[5:-7])  #title

    b = b.split('<span>')
    # print(b)    #['<p>\r\n来源： 外交部发言人办公室', '时间：  2020-05-08</span>\n</p>']
    print(b[0][9:]) #sourse
    print(b[1][5:15])   #date

    c = c.replace('<p>', '')
    c = c.replace('</p>', '')
    c = c.replace('。, 　　', '。')
    c = c.replace('？, 　　', '？')
    print(c)    #content

    end_time = time.time()

    print('已处理, 耗时: {0:.2f}s.'.format(end_time - start_time))



if __name__ == "__main__":
    get_connection()
