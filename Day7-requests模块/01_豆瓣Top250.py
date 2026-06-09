from lxml import etree
import requests


url = 'https://movie.douban.com/top250'
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "accept-encoding": "gzip, deflate, br, zstd",
    "cache-control": "no-cache",
    "cookie": "ll=\"118172\"; bid=rTAabgj5mJ4; _pk_id.100001.4cf6=4cfa4846e7d87256.1773207799.; __utmz=30149280.1773207799.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1773207799.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=oY9A61nNK6z2t5e6cqWWFzta7bkxFl4J; _vwo_uuid_v2=D3802E6069AFC5A11CC9E104E54460875|97d863f773659a58d513784b6a10961c; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1780903963%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1971094671.1773207799.1777282733.1780903963.3; __utmb=30149280.0.10.1780903963; __utmc=30149280; __utma=223695111.1665254563.1773207799.1777282733.1780903963.3; __utmb=223695111.0.10.1780903963; __utmc=223695111",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers)
page = etree.HTML(response.text)
movies = page.xpath("//ol[@class='grid_view']/li/div[@class='item']")
# print(len(movies))
for movie in movies:
    title = movie.xpath(".//span[@class='title']/text()")[0]
    rating_num = movie.xpath(".//span[@class='rating_num']/text()")[0]
    print(title,rating_num)


'''
若没有headers,<Response [418]>
response 是一个响应对象，里面包含了状态码、响应头、响应体……
返回结果状态码为418，100%没有给你正确的结果
'''
# 状态码
# print(response.status_code)
# 返回的响应体(纯文本) # 没有东西？服务器检测到了爬虫
# print(response.text)
'''
如果是用户会有浏览器特征，网站会从几个点去检测爬虫：
1.头信息User-Agent
2.请求参数
3.请求方式
4.签名
5.加密
6.访问频率
'''
# 如何查看请求头里面的信息
# print(response.request.headers)
# {'User-Agent': 'python-requests/2.34.2', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# chrome:'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'