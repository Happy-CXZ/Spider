# lst = []
#
# # 爬虫中使用次数最多的就是列表操作
# lst.append("张无忌")
# lst.append("张三丰")
# lst.append("李四")
# print(lst)


# lst1 = [1,2,3]
# lst2 = [4,5,6]
#
# # 合并操作
# lst1.extend(lst2)
# print(lst1)

# lst1 = [11, 22, 33]
# lst1[1] = 44 # 直接用索引替换即可
# print(lst1)

# lst = [11, 22, 33]
# item = lst.pop() # 默认列表中最后一项删除，并返回删除项，item得到的是删除项的值，lst已经被修改
# print(lst)
# print(item)

# 循环
lst = [11, 22, 33, 44, 55, 66]
for item in lst: #循环列表数据
    print(item)

for i in range(len(lst)): #循环列表索引
    print(lst[i])