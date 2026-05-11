# if 条件:
#     # 事件1
# else:
#     # 事件2

"""
page_content = 页面结构
提取器1 = 页面结构1
提取器2 = 页面结构2
结果 = 提取器1.提取(page_content)
if not 结果:
    结果 = 提取器2.提取(page_content)

保存起来

"""
# while循环 一般不计数……
# 死循环
# while Day1-Python基础上:
#     print("执行死循环中……")

"""
while Day1-Python基础上:
    Day1-Python基础上.发请求
    2.拿结果
    if 有结果:
        break
"""
# 但是一般这个用for循环，防止是程序问题，执行完一定次数就跃出循环了
"""
for i in range(5):
    Day1-Python基础上.发请求
    2.拿结果
    if 有结果:
        break
"""
# continue 遇到脏数据或者没有用的信息的时候，想要停止当前本次循环去处理下一次循环的时候
# break 跳出循环，不再执行
"""
lst = [房子,房子,房子]
for fang in lst:
    if fang 是一室一厅:
        continue

    保存到数据库...
"""

# python 中关于bool的特性
# 如果拿到的数据是以下内容，都是False
# 0 "" [] {} set() tuple() None
print(bool(0))
# 数据 = 提取数据()
# if 数据:
#     存起来
# else:
#     没数据



