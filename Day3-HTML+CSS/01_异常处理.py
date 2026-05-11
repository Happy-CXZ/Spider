"""
异常： 程序运行过程中出现的错误……
在 Python 解释器中，遇到了错误之后，它会自动封装一个错误对象，把错误信息收集起来。
默认情况下，出现错误后，直接终止程序的运行，并把错误信息输出在控制台上。

诉求：程序出现错误的时候，别中断，继续执行

Python提供了处理异常的逻辑 try...except...
语法规则：
try:
    代码块1
except:
    代码块2 --> 处理错误的逻辑

程序尝试执行 代码块1 ，如果出错，自动执行except中的 代码块2
程序如果没有出错， 代码块2 是不会执行的
"""
# try:
#     a = int(input(">>>:"))
#     b = int(input(">>>:"))
#     print(a+b)
# except:
#     print("程序可能出错了……")
#
# print("程序执行完成。")

"""
try:
    代码块1
except KeyError as e:
    代码块2 --> 处理错误的逻辑
except DivsionError as e:
    代码块3 --> 重启一下
except ConnectionTimeoutError as e:
    代码块4 --> 让程序睡眠一下
except Exception as e: #所有异常都可以用这个处理，一般情况就直接用这个就行
    print(e)    
finally:
    收尾工作
"""
# import traceback # 可以看见当前程序的堆栈信息
# try:
#     a = int(input(">>>:"))
#     b = int(input(">>>:"))
#     print(a+b)
# except Exception as e:
#     print(traceback.format_exc())
#
# print("程序执行完成。")

# 实战逻辑：
# 抓取99页的数据，让程序中间不要中断
# import time
# import traceback
#
# # 为了获得错误部分，后面重跑
# f1 = open("错误_url.log", mode="a", encoding="utf-8")
# # 为了看错误信息
# f2 = open("错误.log", mode="a", encoding="utf-8")
# def send_request(page):
#     for i in range(5):  # 达到一个重试的效果……
#         try:
#             print(10/(page - 7))
#             print(f"第{page}页的数据抓取完毕")
#             time.sleep(1) #模拟网络请求，数据慢
#             return # 程序没问题，正常的发了请求，正常的得到数据
#         except Exception as e:
#             f2.write(f"{page}页出现了问题……\n")
#             f2.write(traceback.format_exc()+"\n")
#             time.sleep(1)  # 模拟网络请求，数据慢
#     # 程序走到这里时，程序真的已经重试了5次，还是没有正确拿到数据
#     # 把url和参数记录下来，等结束之后，再去检查到底哪里出现了问题
#     f1.write(f"{page}页出现了问题……\n")
#
# def main():
#     for i in range(1, 100):
#         send_request(i)
#
# if __name__ == "__main__":
#     main()


"""
主动抛出异常
raise 错误
"""
def cul_a_div_b(a,b):
    if b == 0:
        # 主动抛出异常
        raise ZeroDivisionError("b is zero.")
    return a / b

print(cul_a_div_b(2,0))