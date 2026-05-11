# dic = {"jay": "周杰伦","jj": "林俊杰"}
#
# # {key:value}
# # 想要从字典中拿到value，必须要用key
#
# name = dic["jay"] # 如果key不存在，会报错
# print(name)
# name1 = dic.get("jj","默认值") # 如果key不存在，不会报错，没有设定默认返回值时，默认返回None
# print(name1)
#
# # 新增和修改
# # dic[key] = value 保存
# dic['eason'] = "陈奕迅" #当key不存在时，新增
# dic['jay'] = "饼杰伦" #当key存在时，修改
# print(dic)
#
# # 删除
# # dic.pop("jj")
#
# # 循环
# for key in dic:
#     print(key, dic[key])

# 嵌套 (json格式的字符串)
person = {
    "name": "汪峰",
    "age": 56,
    "pre_wife":{
        "name": "章子怡",
        "age": 43,
        "hobby":["当导师","演戏","笑"],
        "作品":["卧虎藏龙","十面埋伏"]
    },
    "作品": ["春天里","北京北京","怒放的生命"],
    "children":[
        {"name":"孩子1", "age":13, "hobby": ["捉迷藏","冰激凌"]},
        {"name":"孩子2", "age":11, "hobby": ["冰激凌","游乐场"]},
        {"name":"孩子3", "age":8, "hobby": ["捉迷藏","斗地主"]},
    ]
}
# 获取数据
# 1、汪峰的年龄
# print(person["age"])
# # 2、汪峰老婆的年龄
# print(person['pre_wife']["age"])
# # 3、罗列出汪峰老婆的爱好
# print(person['pre_wife']["hobby"])
# for item in person['pre_wife']["hobby"]:
#     print(item)
# # 4、罗列出汪峰每一个孩子的年龄
# for item in person['children']:
#     print(item['age'])
# 5、罗列出汪峰每一个孩子的爱好
#xxxx喜欢xxx,xxx,xxx
# for item in person['children']:
#     hobbies = ",".join(item['hobby'])
#     s = f"{item['name']}喜欢{hobbies}"
#     print(s)
#6、汪峰第二个孩子的第一个爱好
# print(person['children'][1]['hobby'][0])