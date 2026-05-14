from bs4 import BeautifulSoup

f = open("桌面壁纸_主页.html","r",encoding="utf-8")
code = f.read()
f.close()

# 获取所有详情页的url
page = BeautifulSoup(code, "html.parser")
# rt = page.find("ul", attrs={"class":"pic-list2"}) # 和下面find_all[0]一个效果
# rt = page.find_all("ul", attrs={"class":"pic-list2"})[0]
#
# rt2 = rt.find_all("a", attrs={"class":"pic"})
# # print(len(rt2))
# for a in rt2:
#     print(a.get("href"))

ret = page.select_one("body > div.wrapper.top-main.clearfix > div.main > ul:nth-child(3)")
a_list = ret.select("a.pic")
for a in a_list:
    print(a.get("href"))