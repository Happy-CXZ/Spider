from lxml import etree

# 1.把HTML代码导入
f = open("index.html","r",encoding="utf-8")
code = f.read()
f.close()

# 2.把HTML交给etree.HTML来解析
page = etree.HTML(code)
# print(page) # <Element html at 0x257029cd600>

"""
在etree里面，你获取到的初始对象，是根节点
在etree里面，所有的HTML标签，都被称为节点
<div>
    <span></span>
</div>
节点与节点之间是有一定关系的，最简单的就是父子关系，div是span的父节点，span是div的子节点

xpath中，
/ 顶格单个出现，表示根节点，即/html
/html/body 表示html标签下的body子标签
// 表示全文检索
//div//li  表示找到div里面的li,无视层级
"""
# rt = page.xpath("/html/body/div/p")
# # xpath()的返回值是列表，先确定列表中有值，再取值 -->if rt:
# if rt:
#     print(rt[0].text)
# # xpath 中每个标签是可以计数的，在标签后面加[n],n从1开始
# rt2 = page.xpath("/html/body/div/ol[2]/li[2]")
# if rt2:
#     print(rt2[0].text)

# xpath支持属性检索,@xxxx
# 节点[@class='joy']
# rt = page.xpath("/html/body/div/ol[1]/li[@class='joy']")
# if rt:
#     print(rt[0].text)

# rt = page.xpath("//li[@class='joy']")
# if rt:
#     print(rt[0].text)
#     print(rt)

# rt = page.xpath("//div//li")
# if rt:
#     print(len(rt))
#     print(rt)

#-----------------------------------------------------
# # 1.取文本 xpath/text()
# rt = page.xpath("//li[@id='10086']/text()")
# print(rt)
# # 2.取属性 xpath/@class
# href = page.xpath("//body/ol/li[1]/a/@href")
# print(href)

# 拿href + 文本
a_list = page.xpath("//a")
for a in a_list:
    href = a.get("href")
    text = a.xpath("text()")[0]
    # href = a.xpath("@href")
    # href = a.xpath(".//@href") #"."表示当前节点
    print(href,text)