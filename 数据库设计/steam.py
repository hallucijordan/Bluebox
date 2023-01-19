import time
from urllib import request
import csv
import requests
from lxml import etree
import os
from pprint import pprint
import random
from fake_useragent import UserAgent
ua = UserAgent()
ddd = ua.random
#
import io

import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
headers = {
    'User-Agent': ddd,
    }
li = []
for i in range(501,551 ):

    url = f'https://store.steampowered.com/search/?supportedlang=schinese&category1=998&page={i}&ndl=1'
    res = requests.get(url, headers=headers)
    res1 = res.content.decode('UTF-8')
    res2 = etree.HTML(res1)
    res3 = res2.xpath('//div[@id="search_resultsRows"]/a')
    for ii in res3:
        try:
            div = {}
            div['游戏名称'] = ii.xpath('.//span[@class="title"]/text()')[0]
            div['游戏id'] = ii.xpath('@data-ds-appid')[0]
            div['发行日期'] = ii.xpath('.//div[@class="col search_released responsive_secondrow"]/text()')[0]
            div['游戏链接'] = ii.xpath('@href')[0]
            div['游戏主页图片'] = ii.xpath('./div/img/@src')[0]
            div['游戏评价'] = ii.xpath('./div[@class="responsive_search_name_combined"]/div[@class="col search_reviewscore responsive_secondrow"]/span/@data-tooltip-html')[0].replace('<br>','')
            if ii.xpath('./div[@class="responsive_search_name_combined"]/div[4]/div[@class="col search_price  responsive_secondrow"]/text()'):
                div['游戏价钱'] = ii.xpath('./div[@class="responsive_search_name_combined"]/div[4]/div[@class="col search_price  responsive_secondrow"]/text()')[0].split()
            else:
                div['游戏价钱'] = ii.xpath('./div[@class="responsive_search_name_combined"]/div[4]/div[2]/text()')[0].split()
            li.append(div)
            print(div)
        except:
            pass
with open('stema游戏.csv', 'w', encoding='utf-8', newline='')as f:
    FF = csv.DictWriter(f, fieldnames=('游戏名称', '游戏id', '发行日期', '游戏链接', '游戏主页图片', '游戏评价', '游戏价钱'))
    FF.writeheader()
    FF.writerows(li)