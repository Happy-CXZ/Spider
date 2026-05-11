import os

# 1.文件路径相关的操作
# file_path = "./abc/def/a/b/d.txt"
# file_path2 = "url.txt"

# 判断文件是否存在
# print(os.path.exists(file_path))
# print(os.path.exists(file_path2))

# 创建文件夹
# os.makedirs("./a/b/c/d")  # 创建文件夹目录结构

# 获取某路径的文件夹
# print(os.path.basename(file_path)) # 拿文件名
# print(os.path.dirname(file_path)) # 拿路径

# 判断是否是文件夹
# print(os.path.isdir(file_path))

# 创建文件的完整程序逻辑:
file_path = "./ab/c/d/e/d.txt"
# 判断文件夹路径是否存在，如果存在，才能创建，不存在，先创建文件夹
if not os.path.isdir(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))


open(file_path,"w",encoding="utf-8")









