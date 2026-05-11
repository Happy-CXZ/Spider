"""
ascii
8bit = 1 byte
0000 0000  0000 0000 编码数量从256扩大到65536个
长度是 16bit,2byte,扩展完是一个标准ANSI
中国基于ANSI形成专门的编码：GB码，例如GBK

编排的时候发现全球的文字和符号远超65536，再进行扩充1倍，最终扩充到32bit,4byte
0000 0000 0000 0000 0000 0000 0000 0000
全球统一编码，叫Unicode，但是无法在网络通信和传输过程中使用
我们今天的程序，在执行的时候，内存层面使用的就是Unicode

为了保存数据的传输和存储，发明了可变长度的Unicode
utf-8 最小的一个字符长度是8bit,1byte -> 现在用的最多的字符集就是它
utf-8的逻辑：
    ascii范围的东西：1byte, 8bit
    欧洲文字：2byte, 16bit
    中文：3byte, 24bit

所有文字的传输和存储必须转化成gbk和utf-8来进行
"""
s = "我爱你"
# 把字符从内容中转化为字节，然后才可以传输或者存储
# s.encode(字符集)
bs = s.encode("gbk") # b'\xce\xd2\xb0\xae\xc4\xe3'
# \xff -> 十六进制一个字节
print(bs)
print(b'c' == b'\x63')
print(b'\xea\xabc\xcc\x1ab\xcd1f\xcd'.__len__()) #多少个字节，10个
bs = s.encode("utf-8") # b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'
print(bs)

# gbk 是没法直接转化为 utf-8 的，需要一个还原成字符串的过程

bs1 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0' # utf-8
# 解码
s = bs1.decode("utf-8")
print(s)