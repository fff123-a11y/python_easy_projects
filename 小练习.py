for i in range(1, 10):
    for j in range(1, 10):
        print('{}*{}={}\t'.format(i, j, i * j))
    print()

i = 1
while i <= 3:
    name = input("请输入您的用户名：")
    password = input("请输入密码：")
    if name == 'lisa' and password == '123456':
        print("lisa,欢迎您！")
        break
    elif name != 'lisa' and password == '123456':
        print("用户名错误，请重新输入！")
        i = i + 1
    elif password != '123456' and name == 'lisa':
        print("密码错误，请重新输入！")
        i = i + 1
    else:
        print("输入有误!")
        i = i + 1
if i == 3:
    print("程序已锁定！")

f = open('text.txt', 'w')
a_str = input("请输入字符串：")
f.write(a_str.upper())
f = open('text.txt', 'r')
print(f.read())

f.close()


class Person(object):
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __str__(self):
        return f"{self.name}今年{self.age}岁，喜欢{self.hobby}"


with open("text2.txt", "r", encoding="UTF-8") as f:
    data = f.read
    data1 = data.split("\n")
    for i in data1:
        print(i)
        data2 = i.split()
        print(data2)
        p = Person(data2[0], data2[1], data2[2])
        print(p)
