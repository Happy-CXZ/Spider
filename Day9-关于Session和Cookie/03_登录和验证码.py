"""
地址：http://www.woaige.net/login.php?jumpurl=
目标：完成登录操作，查看书架中的内容
"""
import requests
import ddddocr

# url = 'http://www.woaige.net/bookcase.php'
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "no-cache",
#     "connection": "keep-alive",
#     "cookie": "Hm_lvt_2df76952c7491058d07d6f137bbc0868=1781595408; HMACCOUNT=74ED4E40E6CB58EE; username=User; t=82046061256a3106ad377ca; Hm_lpvt_2df76952c7491058d07d6f137bbc0868=1781597865",
#     "host": "www.woaige.net",
#     "pragma": "no-cache",
#     "referer": "http://www.woaige.net/",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
# }
# response = requests.get(url=url,headers=headers)
# print(response.text)

# 考虑走一遍登录流程（不是必选项）
session = requests.session()
session.headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "host": "www.woaige.net",
    "pragma": "no-cache",
    "referer": "http://www.woaige.net/",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
# 走登录流程，此时，你要盯着的是cookie的生成过程
# 通过观察，发现加载验证码的时候，服务器携带了cookie回来，而这个值是后面验证登录的时候必须的一个值
code_url = "http://www.woaige.net/code.php?0.13734697024260023"
response = session.get(url=code_url)
# print(session.cookies) # 验证cookie中是否有c
# 识别图片
with open("code.jpg", "wb") as f:
    f.write(response.content)
# 1、免费
# ddddocr, 这个库是一个个人开发的库..对py版本有一定要求....
# 官方文档
# https://github.com/sml2h3/ddddocr
ddd = ddddocr.DdddOcr(show_ad = False) #参数去掉广告
# 读取图片
f = open("code.jpg", "rb")
rt = ddd.classification(f.read())
f.close()

rt2 = ddd.classification(response.content)
print(rt2)
# # 2、付费：图鉴、超级鹰
login_data = {
    "LoginForm[username]": "优秀陈小卷",
    "LoginForm[password]": "123456",
    "LoginForm[captcha]": rt,
    "action": "login",
    "submit": "登  录 "
}
login_url = "http://www.woaige.net/login.php"
login_response = session.post(login_url, data=login_data)
# print(login_response.text) # 看到它进入首页了即登录成功
# 登录成功后，会有cookie的增加
print(session.cookies)

# 有了cookie，登录信息，可以访问书架上的内容
jia_url = "http://www.woaige.net/bookcase.php"

response = session.get(jia_url)
print(response.text)

# 浏览器, 看到302会自动跳转....跳转到Location对应的地址
# session默认是按照浏览器的逻辑走的. 它看到302也会自动发起新的请求, 重新发到Location
# 我们目前看到的样子. 实际上里面是两个请求
# session人性化的一点...这是好事儿...