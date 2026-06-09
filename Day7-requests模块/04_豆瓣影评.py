import requests
from lxml import etree
import re
'''
url = 'https://movie.douban.com/review/best/'
目标:拿到该网站的标题,影评内容
1.先访问页面源代码,从页面源代码中提取到标题和data-rid
2.根据不同的data-rid,发送不同的full请求,就能拿到文章的所有内容
'''
url = 'https://movie.douban.com/review/best/'
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "ll=\"118172\"; bid=rTAabgj5mJ4; _pk_id.100001.4cf6=4cfa4846e7d87256.1773207799.; __utmz=30149280.1773207799.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1773207799.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=oY9A61nNK6z2t5e6cqWWFzta7bkxFl4J; _vwo_uuid_v2=D3802E6069AFC5A11CC9E104E54460875|97d863f773659a58d513784b6a10961c; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1780987777%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1971094671.1773207799.1780909950.1780987778.6; __utmb=30149280.0.10.1780987778; __utma=223695111.1665254563.1773207799.1780909950.1780987778.6; __utmb=223695111.0.10.1780987778; ap_v=0,6.0",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://movie.douban.com/review/best/",
    "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
response1 = requests.get(url, headers=headers)
# print(response1.text) 一定要记得验证是否取出来数据
page = etree.HTML(response1.text)
remarks = page.xpath("//div[@data-cid]")
# print(len(remarks))
for remark in remarks:
    title = remark.xpath(".//h2/a/text()")[0]
    data_cid = remark.xpath("./@data-cid")[0]
    # print(data_cid, title)
    # 拼接full的url,发请求,得到信的full内容
    full_url = f"https://movie.douban.com/j/review/{data_cid}/full"
    full_resp = requests.get(full_url, headers=headers)

    body = full_resp.json()['body']
    body_page = etree.HTML(body)
    contents = body_page.xpath("//div[@class='review-content clearfix']//text()")
    # print(len(contents))
    with open('remark.txt', 'a', encoding='utf-8') as f:
        f.write(title)
        for content in contents:
            content = re.sub(r"\s","",content)
        # print(content)
        # print("###########")
            f.write(content)
            f.write('\n')
    with open('remark.txt', 'a', encoding='utf-8') as f:
        f.write("===============================================================")