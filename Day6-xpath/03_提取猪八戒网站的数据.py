from lxml import etree
import re

f = open("一个恶心的网站_猪八戒.html","r",encoding="utf-8")
code = f.read()
f.close()

page = etree.HTML(code)

div_list = page.xpath("//div[@class ='search-result-list-service']//div[@source='10']")
print(len(div_list))
for div in div_list:
    price = div.xpath(".//div[@class='price']/span/text()")[0]
    title = div.xpath(".//div[@class='name-pic-box']//span/text()")
    title = re.sub(r"\s","","".join(title)) # 除掉空格
    href = div.xpath(".//div[@class='name-pic-box']//a/@href")[0]
    name = div.xpath(".//div[@class='shop-info text-overflow-line']//text()")[0]
    print(price,title,href,name)
"""
* 是通配符，代表任意的标签
//*[@class='xxx'] class为xxx的任意标签
/table/*/div/*/span/text() table下面任意一个子标签中的div中任意一个子标签的span的文本
"""