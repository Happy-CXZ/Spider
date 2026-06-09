import requests

url='https://movie.douban.com/j/chart/top_list'
# 当url里面的参数过多的时候,应该用字典的方式表示,这样更容易维护

params= {
    "type": "13",
    "interval_id": "100:90", # 将特殊字符进行urlencode()->冒号':'会被编码成'%3A'
    "action": "",
    "start": "0",
    "limit": "20"
}
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "ll=\"118172\"; bid=rTAabgj5mJ4; _pk_id.100001.4cf6=4cfa4846e7d87256.1773207799.; __utmz=30149280.1773207799.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1773207799.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=oY9A61nNK6z2t5e6cqWWFzta7bkxFl4J; _vwo_uuid_v2=D3802E6069AFC5A11CC9E104E54460875|97d863f773659a58d513784b6a10961c; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1780907560%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1971094671.1773207799.1780903963.1780907560.4; __utmb=30149280.0.10.1780907560; __utma=223695111.1665254563.1773207799.1780903963.1780907560.4; __utmb=223695111.0.10.1780907560",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=",
    "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
# params: url携带的参数(Query String Parameters),requests模块会拼接好
response = requests.get(url,params=params,headers=headers)
# print(response.request.url)
'''
post请求
response = requests.post(url,params=params,data={放在请求体中的参数Form Data},headers=headers)
'''

# print(response.text) # 拿到的是文本,你打印出来的是json字符串,你看到的字符串中,有可能会被处理成\\u什么什么,处理成字典就好了
# print(response.json()) # 自动把响应体中的内容处理成字典,若此时还有\\u什么什么,说明遇到嵌套json了
items = response.json()
for movie in items:
    title = movie["title"]
    score = movie["score"]
    print(title,score)

'''
注意:
response = response.json()
它处理数据的前提是数据格式,必须是json格式的
'''