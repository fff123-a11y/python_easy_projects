sum = 0
num_list = [1, 3, 34, 24, 66, 55, 77, 85, 99, 100]
for index_ in num_list:
    if index_ % 2 == 0:
        sum = sum + index_
        print(sum)


class Godness():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        print(f"我的女神她叫{self.name},她的身高{self.height},她的体重{self.weight}")

    def sing(self):
        print("她唱歌很好听")

    def dance(self):
        print("她跳舞也太好看了吧")


lb = Godness("Cara", 160, 45.5)
lb.sing()
lb.dance()

dict_ = {"姓名": "Cara", "年龄": 18, "性别": "女"}
dict_.items()
with open('Cara.txt', 'a+', encoding='UTF-8') as fp:
    fp.write("姓名:Cara 年龄:18 性别:女")
    fp.seek(0)
    print(fp.read())

import threading


def num1():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)


def num2():
    for i in range(1, 101):
        if i % 2 == 1:
            print(i)


t1 = threading.Thread(target=num1)
t2 = threading.Thread(target=num2)
t1.start()
t1.join()
t2.start()

import re

print(re.findall("\d{3}", "abc123efg456"))  # 正则表达式
