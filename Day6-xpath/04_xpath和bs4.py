from lxml import etree
from bs4 import BeautifulSoup

# 1. 把html代码导入
f = open('data.xml', mode="rb")  # etree可能会需要传递字节
code = f.read()
f.close()

# 2. 把HTML交给etree.HTML来解析
xpath_page = etree.XML(code)
bs4_page = BeautifulSoup(code, "xml")

# bs4 秒出结果.
rt = bs4_page.find("modelVersion").text
print(rt)

# xpath默认出不来结果.
# xpath必须指定名称空间. 否则取不到东西.
namespace = {
    "default": "http://maven.apache.org/POM/4.0.0",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance"
}

rt2 = xpath_page.xpath("//default:modelVersion/text()", namespaces=namespace)
print(rt2)

"""带问题扣999"""
