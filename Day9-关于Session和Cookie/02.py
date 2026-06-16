import requests
# 通过字典转化成cookie_jar
from requests.cookies import cookiejar_from_dict

url = "https://xueqiu.com/"

# # 请求首页, 获取到cookie值
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "no-cache",
#     "connection": "keep-alive",
#     "dnt": "1",
#     "host": "xueqiu.com",
#     "pragma": "no-cache",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
# resp = requests.get(url, headers=headers)
# # 响应头,  头里面返回了set-cookie
# # 比较原始的提取cookie值的办法. 借助响应头获取的
# # print(resp.headers.get("set-cookie"))
# print(resp.cookies)
#
# # 借助于响应头的cookie 发请求. 看看能否得到雪球上的数据
# data_url ="https://xueqiu.com/statuses/hot/listV3.json?page=1&last_id="
# resp = requests.get(data_url, headers=headers, cookies=resp.cookies)
# # resp = requests.get(data_url, headers=headers)
# print(resp.text)
# print(resp.cookies)


# 方式二:

# 这句话的意思是创建一个session. 一个session里面有什么呢???
# 通过requests源码发现session里面有headers, cookies
# session = requests.session()
# print("刚刚创建的session")
# # 如果我们可以最开始, 给session怼上一些cookie. 后续所有的请求. 自动都会有这个值
#
# # 打印出来的session.cookie是RequestsCookieJar类型的
# # 这种处理cookie的方式, 我们在后面逆向的时候需要手工维护cookie的时候
# # 就需要这种方式  -> 需要导包的
# # session.cookies = cookiejar_from_dict({
# #     "qiao": "fu"
# # })
#
# # 或者直接把cookie当字典用。 -> 不需要导包的
# session.cookies['qiaoooooo'] = "fufufufufu"
#
# print(session.cookies)
#
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "no-cache",
#     "connection": "keep-alive",
#     "dnt": "1",
#     "host": "xueqiu.com",
#     "pragma": "no-cache",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
# resp = session.get(url, headers=headers)
# print("发送第一个请求之后的session")
# print(session.cookies)
#
# session.cookies.pop("qiaoooooo")
#
# data_url ="https://xueqiu.com/statuses/hot/listV3.json?page=1&last_id="
#
# # session内部会自动的帮你维护cookie. 你什么都不用动
# # 后续所有的请求都会自动的带着这个cookie, 并且, 如果返回了新的cookie
# # 它还能自动帮你合并....你就省事儿了...
# resp = session.get(data_url, headers=headers)
# # print(resp.text)
# print("发送请求数据之后的session")
# print(session.cookies)


# # 方式三, 最推荐的一种方式
# # session可以维护cookie, 也可以设置默认的头
#
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "no-cache",
#     "connection": "keep-alive",
#     "dnt": "1",
#     "host": "xueqiu.com",
#     "pragma": "no-cache",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
#
# session = requests.session()
# # # 设置默认的头. 以后, 头就不用管了. 有两个值需要单独维护
# # 1. content-type, 需要手工维护
# # 2. referer, 需要手工维护
# session.headers = headers
#
# # 访问首页, 加载第一个cookie
# resp = session.get(url, headers={"user-agent": "qiaofuwoaini"})
#
# # print(resp.request.headers)
# # print(session.headers)  # 上面出现了两个头. 会不会把默认的给冲掉???
#
# data_url ="https://xueqiu.com/statuses/hot/listV3.json?page=1&last_id="
# resp = session.get(data_url)
# print(resp.text)