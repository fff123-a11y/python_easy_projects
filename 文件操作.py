"""
ACD
A.用open()函数可以打开一个已存在的文件，或者创建一个新文件,A正确
B.a模式会往文件中追加数据，B错误
C.read()方法可以读取文件所有内容，readline方法一次读取一行内容，C正确
D.seek(0,0)把指针定位到文件开头，D正确
"""

f = open('text.txt', 'w')
a_str = input("请输入字符串：")
f.write(a_str.upper())
f = open('text.txt', 'r', encoding='utf-8')
print(f.read())

f.close()
