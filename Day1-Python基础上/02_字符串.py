s = '好好学习天天向上'

print(s[2:4])
print(s[-2])

# 不要第一个字
s1 = s[1:]
print(s1)

# 字符串本身是没变，是返回一个新的字符串
# split() 切割 默认是根据空白切割(\n\r\t空格) 得到的结果是列表
# split("可爱") 根据“可爱”切割
"""
s = '可爱小猫 小猫可爱 那有一直可爱的小猫 小猫笑的可爱'
lst = s.split()
"""
"""
data = '10,英雄本色,1500万'
rank, name, money = data.split(",")
print(rank)
print(name)
print(money)
"""

# strip() 默认去掉左右两端的空白
"""
s = "\r\r\r\r\r\n\t我是世界第一大聪明   \r\n\r\t"
s1 = s.split()
print(s1)
"""

# replace(old, new)
"""
s = "你爱我 我爱你 蜜雪冰城甜蜜蜜"
s = s.replace(" ",",")
print(s)
"""
"""
s = "你   爱我,   我爱   你, 蜜雪  \n 冰  \t城甜蜜 蜜"
s = s.replace(" ","").replace("\t","").replace("\n","") # 都要替换掉，才能得到干净的字符串
print(s)
"""

# "".join(list) 把列表里面的内容，拼接成一个新的字符串
"""
lst = ["刘德华", "张国荣", "黎明"]
s = ",".join(lst)
print(s) 
"""

# f-string 格式化
"""
name = '周杰伦'
age = 20
# 在f-string中 {{ 转义为 {
s = f"我叫{name},今年{age}岁了，我想输出一个大括号{{}}"
print(s)
"""