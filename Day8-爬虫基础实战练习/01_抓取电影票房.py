"""
网址:http://www.boxofficecn.com/boxofficecn
目标:大陆所有的电影票房
"""
import os

import requests
from lxml import etree
def get_movie_by_year(year):
    url = f'http://www.boxofficecn.com/boxoffice{year}'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1779355507,1779419969,1779435617,1780995265; HMACCOUNT=74ED4E40E6CB58EE; __51cke__=; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1780995465; __tins__4287866=%7B%22sid%22%3A%201780995265467%2C%20%22vd%22%3A%206%2C%20%22expires%22%3A%201780997264970%7D; __51laig__=6",
        "host": "www.boxofficecn.com",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    # print(response.text)
    page = etree.HTML(response.text)
    trs = page.xpath('//tr[@align="left"]')
    # print(len(trs))
    filename = f'./movies/movie_{year}.csv'
    with open(filename,'w',encoding='utf-8') as f:
        for tr in trs:
            # 用join的方式代替取0
            num = "".join(tr.xpath('./td[1]//text()'))
            # if num:
            #     num = num[0]
            # else:
            #     num = ''
            if not num:
                continue
            year = "".join(tr.xpath('./td[2]//text()'))
            # if year:
            #     year = year[0]
            # else:
            #     year = ''
            name = "".join(tr.xpath('./td[3]//text()'))
            # if name:
            #     name = name[0]
            # else:
            #     name = ''
            money = "".join(tr.xpath('./td[4]//text()'))
            # if money:
            #     money = money[0]
            # else:
            #     money = ''
            # if not (name and money and year and num):
            #     continue
            s = f'{num},{year},{name},{money}\n'
            # print(num,year,name,money)
            # 把数据保存到文件
            f.write(s)


#创建文件夹
if not os.path.exists('./movies'):
    os.mkdir('./movies')
# get_movie_by_year(2020)
for year in range(1994,2027):
    get_movie_by_year(year)
    print(f'{year}年的数据已经保存完毕')