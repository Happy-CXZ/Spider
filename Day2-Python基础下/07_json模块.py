"""
json存在的意义是让前后端的传输交互变得简单
json的本质就是特殊格式的字符串……

'{"name": "汪峰", "age": 18}'
json字符串和Python的字典/列表之间的转化可以交给json模块
"""
import json # 用来转化的
# s = '{"name": "汪峰", "age": 18, "money": null, "married": false}'
# 想办法把json字符串转化为字典
# dic = json.loads(s)
# print(s)
# print(dic)
# print(type(dic))
# print(dic["age"])
# 想办法把字典转化为字典json字符串
dic = {'name': '汪峰', 'age': 18, 'money': None, 'married': False}
s = json.dumps(dic)
print(s)

# 特别注意一个小问题：
# 前端生成的json是没有空格的
# Python生成的json是有空格的，转化的时候增加一个参数separators
dic = {'name': '汪峰', 'age': 18, 'money': None, 'married': False}
s = json.dumps(dic,separators=(',',':'))
print(s)