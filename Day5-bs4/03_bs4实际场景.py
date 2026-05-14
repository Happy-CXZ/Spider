# bs4 更多时候是用来处理xml
from bs4 import BeautifulSoup

f = open("data.xml","r",encoding="utf-8")
code = f.read()
f.close()

# 如果遇到一个bug，提示说给字符串或者给字节，可以更换成字节传递
# 即 f = open("data.xml","rb")
page = BeautifulSoup(code,"xml")
# print(page)

# rt = page.find("dependencyManagement").find("dependency").find("artifactId")
# print(rt.text)

# tr = page.select_one("dependencyManagement artifactId")
# print(tr.get_text())

f2 = open("字.svg","rb")
svg = f2.read()
f2.close()

page2 = BeautifulSoup(svg,"xml")
ts = page2.find_all("text")
s = ""
for t in ts:
    print(t.text)
    s += t.text
print(s)
