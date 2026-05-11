# 1、创建文件
# w模式下，open文件的时候，文件不存在时，会自动创建新的文件，文件存在时，会覆盖原来文件的内容
# f = open("sample.txt",mode="w",encoding="utf-8")
# f.close()

# 2、向文件写入内容
# w 写的权限，没有读的，覆盖文件内容
# a 写的权限，没有读的，追加文件内容
# f = open("sample.txt",mode="w",encoding="utf-8")
# f.write("我是周杰伦")
# f.close()

# 3、如何拷贝一个文件(图片,mp4,mp3,zip...)
# b: 读写的是字节，此时，不可以给出encoding参数的
# with open("image.jpg", "rb") as f1, open("image2.jpg", "wb") as f2:
#     content = f1.read()
#     f2.write(content)

# 4、读取文件中一行一行的数据
# r:读取文件中的内容
with open("url.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip() # 去掉末尾的\n
        print(line)