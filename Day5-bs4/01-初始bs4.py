"""
bs4 是一款用来解析 html(xml) 结构的第三方库
pip install bs4
"""
from bs4 import BeautifulSoup

f = open("index.html","r",encoding="utf-8")
code = f.read()
f.close()

# 1.把你要解析的东西丢给BeautifulSoup
# 第一个参数是你要解析的东西
# 第二个参数代表的是使用何种解析的方式来解析内容，常见值：html.parser,lxml(需要单独安装 pip install lxml)
page = BeautifulSoup(code,"html.parser")

# 2.使用bs4查询逻辑进行标签的检索
# 2.1 使用标签来查找
"""
page.find("标签名", attrs = {属性名:属性值}) # 找到第一个标签，返回值是element
page.find_all("标签名", attrs = {属性名:属性值}) # 找到所有的标签，返回的是列表[ element ]

bs4 拿到的内容是Tag类型，想要提取文本，直接在Tag后面加.text，后代所有的文本全部提取出来
class 属性：可以拆开解析，间隔只能有一个空格
"""
# ret = page.find("div", attrs={"class": "c2 small-text"})
# print(ret.text)
# print(type(ret))
#
# divs = page.find_all("div")
# for div in divs:
#     print(div.text)

# divs = page.find_all("div", attrs={"class":"small-text"})
# for div in divs:
#     print(div.text)

# imgs = page.find_all("img")
# for img in imgs:
#     # print(img["src"])
#     print(img.get("src"))

# 2.2 使用css来查找
# page.select("css选择器")           page.find_all("标签")
# page.select_one("css选择器")       page.find("标签")

# s = page.select_one(".c3").text
# print(s)

# s = page.select(".c3")
# for i in s:
#     print(i.text)

#css 可以从浏览器上直接复制，但是注意有的时候复制过来的无法使用需要微调
s = page.select("body > div.c2.small-text > p")
for i in s:
    print(i.text)

