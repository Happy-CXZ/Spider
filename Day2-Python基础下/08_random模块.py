import random

# 在范围内随机生成整数
print(random.randint(10,20))  # 前后两个区间数都能取到，是闭区间

# 在目标中随机选择一个
lst = [1,2,3,4,5,6]
print(random.choice(lst))

time_sleep = random.uniform(0.5, 1)
print(time_sleep)