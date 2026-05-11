# 我们在创建py文件名时，一定要避开内置模块和第三方模块

# time 时间模块
import time

#1.时间戳：用数字来描述一个时间点
# 时间的0点坐标是1970-01-01 00:00:00

# 当前系统的时间戳，python的时间单位是秒
# 浏览器上计算的时间戳是毫秒为单位
print(time.time())

# 统一单位，需要模仿浏览器的
tm = int(time.time() * 1000)
print(tm)


#2.睡觉(非常重要)
# time.sleep(n) 让程序休眠n秒钟
while 1:
    print("访问中...")
    time.sleep(1) # 控制访问频率