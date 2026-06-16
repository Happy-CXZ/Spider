"""
网址：http://www.metalinfo.cn/mi.html
目标：标题，内容，发布时间，来源
"""
import requests
from lxml import etree

url = "http://www.metalinfo.cn/json/search/list"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-length": "86",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "Hm_lvt_204973c50a7ce5a180c8edd164761976=1781166340; HMACCOUNT=74ED4E40E6CB58EE; JSESSIONID=B056604A69FABE1DEBE75D0179DB04D7; Hm_lpvt_204973c50a7ce5a180c8edd164761976=1781171422",
    "host": "www.metalinfo.cn",
    "origin": "http://www.metalinfo.cn",
    "pragma": "no-cache",
    "referer": "http://www.metalinfo.cn/mi.html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

data = {
    "pageSize": "20",
    "current": "1",
    "resourceType": "r_news",
    "facetFilter": "{}",
    "order": "desc",
    "sort": "sort_time"
}

response = requests.post(url,data=data,headers=headers)

dic = response.json()
tid = "4de50205386c41af94409fdf8d2e1118"
for record in dic['result']['records']:
    # print(record)
    print("=========")
    title = record['title']
    detail = record['r_abstract']
    time = record['real_time']
    release_url = record['release_url']
    rid = record['rid']
    print(title[:5],time,release_url,detail)

    detail_page_url = f"http://www.metalinfo.cn/news/{rid}.html?rtype=r_news&columnId={tid}"
    print(detail_page_url)

    detail_url = "http://www.metalinfo.cn/json/resource/detail"
    params = {
        "rid" : rid,
        "rtype": "r_news",
        "columnId": tid
    }
    # detail_headers = {
    #     "accept": "application/json, text/javascript, */*; q=0.01",
    #     "accept-encoding": "gzip, deflate",
    #     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    #     "cache-control": "no-cache",
    #     "connection": "keep-alive",
    #     "cookie": "Hm_lvt_204973c50a7ce5a180c8edd164761976=1781166340; HMACCOUNT=74ED4E40E6CB58EE; JSESSIONID=B056604A69FABE1DEBE75D0179DB04D7; Hm_lpvt_204973c50a7ce5a180c8edd164761976=1781172632",
    #     "host": "www.metalinfo.cn",
    #     "pragma": "no-cache",
    #     "referer": detail_page_url,
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    #     "x-requested-with": "XMLHttpRequest"
    # }
    detail_headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        # "content-length": "86",     # 请求体有多少内容, get请求是没有请求体的....77777 9999
        # "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "Hm_lvt_204973c50a7ce5a180c8edd164761976=1781166340; HMACCOUNT=74ED4E40E6CB58EE; JSESSIONID=B056604A69FABE1DEBE75D0179DB04D7; Hm_lpvt_204973c50a7ce5a180c8edd164761976=1781172632",
        "dnt": "1",
        "host": "www.metalinfo.cn",
        "pragma": "no-cache",
        "referer": detail_page_url,  # 当前这个请求是来自于哪个url 7779999
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    response = requests.get(detail_url,params=params,headers=detail_headers)
    print(response.text)
    break