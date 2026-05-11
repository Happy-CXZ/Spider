import re

# 利用正则表达式搜索
# # 1、search 从前到后匹配，遇到匹配的内容，直接结束，返回结果。
# res = re.search(r"\d","我今天吃了3个馒头，喝了2盒牛奶")
# # search的结果被封装在Match对象中，想要结果，需要.group()获取
# print(res.group())


# # 2、findall 直接把匹配的结果返回，放在列表里
# res = re.findall("\d+","我今天发放了300个馒头，喝了20盒牛奶")
# # search的结果被封装在Match对象中，想要结果，需要.group()获取
# print(res)

# 3、finditer 迭代器，节约内存，增加性能
# res = re.finditer("\d+","我今天发放了300个馒头，喝了20盒牛奶")
# # finditer的结果是列表，想要结果，需要.group()获取
# for item in res:
#     print(item)
#     print(item.group())


# 提前定义一个正则后面随时用
# obj = re.compile(r'(\d)')
# result = obj.search("我今天吃了3个馒头，喝了2盒牛奶")
# print(result.group())


# s = """
#    <div class='西游记'><span id='10010'>中国联通1</span></div>
#    <div class='三国演义'><span id='10011'>中国联通2</span></div>
#    <div class='水浒传'><span id='10012'>中国联通3</span></div>
#    <div class='红楼梦'><span id='10013'>中国联通4</span></div>
#    """
# obj = re.compile(r"<div class='(?P<book>.*?)'><span id='(?P<id>.*?)'>(?P<name>.*?)</span></div>")
# result = obj.finditer(s)
# for item in result:
#     book = item.group('book')
#     id = item.group('id')
#     name = item.groupdict()['name']
#     print(book, id, name)


# 字符串替换
s = "    字符串替换要好\t  好学，\n还有半 \r \t小时今天  就要结束啦"
r = s.replace(" ","").replace("\t","").replace("\n","").replace("\r","")
print(r)
# r1 = re.sub(正则, 需要替换进去的内容, 原字符串)
r1 = re.sub("\s","",s)
print(r1)