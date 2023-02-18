a = int(input("请输入一个整数a："))
b = int(input("请输入一个整数b："))
c = int(input("请输入一个整数c："))
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

i = 1
while i <= 12:
    while i == 6 or i == 10:
        i += 1
        continue
    if i < 12:
        print(i, end=",")
    elif i == 12:
        print(i, end=" ")
    i += 1

i = 0
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

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(i, j, i * j))
    print()

import multiprocessing
import time
import os


def Function():
    print("Function", os.getpid())
    print("Function", multiprocessing.current_process())
    for i in range(5):
        print("函数")
        time.sleep(0.2)


if __name__ == '__main__':
    print("main:", os.getpid())

import multiprocessing
import time
import os


def long_time_task():
    print("当前进程:{}".format(os.getpid()))


time.sleep(2)
print("结果:{}".format(8 ** 20))

if __name__ == '__main__':
    print("当前母进程:{}".format(os.getpid()))
    start = time.time()
    for i in range(2):
        long_time_task()

    end = time.time()
    print("用时{}秒".format(end - start))


# 定义字典树中的一个节点
class Node(object):
    def __init__(self):
        self.children = {}


class Solution:
    def minimumLengthEncoding(self, words: [str]) -> int:
        words = list(set(words))  # 需要去重，否则在之后计算“叶子高度”的时候会重复计算
        trie = Node()  # 这是字典树的根
        nodes = []  # 这里保存着每个word对应的最后一个节点，比如对于单词time，它保存字母t对应的节点（因为是从后往前找的）
        for word in words:  # 逐个单词遍历
            now = trie  # 定义临时变量保存当前节点
            for w in reversed(word):  # 字符串反转
                if w in now.children:  # 如果在，就继续往下遍历
                    now = now.children[w]
                else:
                    now.children[w] = Node()
                    now = now.children[w]
            nodes.append(now)
        ans = 0
        for w, c in zip(words, nodes):
            if len(
                    c.children) == 0:  # 没有children，意味着这个节点是个叶子，nodes保存着每个word对应的最后一个节点，当它是一个叶子时，我们就该累加这个word的长度+1，这就是为什么我们在最开始要去重
                ans += len(w) + 1
        return ans


# 线程：线程之间共享内存空间，坏处：数据不安全 好处：通信
# 进程：进程之间不共享内存空间 坏处：不能实现通信 好处：数据安全
from multiprocessing import Process

num = 0
total = 1000000


def add1():
    global num
    print(f"add1的初始值为{num}")
    for i in range(total):
        num += 1
    print(f"add1的最终值为{num}")


def add2():
    global num
    print(f"add2的初始值为{num}")
    for i in range(total):
        num += 1
    print(f"add2的最终值为{num}")


if __name__ == '__main__':
    p1 = Process(target=add1)
    p2 = Process(target=add2)
    p1.start()
    p2.start()

from multiprocessing import Process
import os

add1 = "看作业"
add2 = "批改作业"


def action1():
    print(f"灼灼老师在{add1}")


def action2():
    print(f"灼灼老师在{add2}")


if __name__ == '__main__':
    p1 = Process(target=action1)
    p2 = Process(target=action2)
    p1.start()
    p2.start()
    p1.name = "优秀作业"
    print(f"p1的子进程名：", p1.name)
    print(f"p2的子进程名：", p2.name)
    print(f"主进程id:{os.getpid()},父进程id:{os.getppid()}")

from multiprocessing import Process
import os
import time


def action1():
    print("护肤")
    time.sleep(1)


def action2():
    print("化妆")
    time.sleep(1)


if __name__ == '__main__':
    p1 = Process(target=action1)
    p2 = Process(target=action2)
    p1.start()
    p1.join()
    p2.start()
