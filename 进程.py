from multiprocessing import Process


def action1():
    print("护肤")


def action2():
    print("化妆")


if __name__ == '__main__':
    p1 = Process(target=action1)
    p2 = Process(target=action2)
    p1.start()
    p1.join()
    p2.start()

from multiprocessing import Process
import os


def Homework():
    print("正在看作业")
    print(f"Homework子进程id:{os.getpid()},父进程id:{os.getppid()}")


def Question():
    print("解答问题")
    print(f"Question子进程id:{os.getpid()},父进程id:{os.getppid()}")


if __name__ == '__main__':
    p1 = Process(target=Homework, name="优秀作业")
    p2 = Process(target=Question)
    p1.start()
    p2.start()
    p1.name = "优秀作业"
    print("作业继承名:", p1.name)

import os
import time
import multiprocessing


def task():
    print(f"当前进程号：{os.getpid()}")
    time.sleep(2)
    print(f"输出8的20次方的结果:{8 ** 20}")


if __name__ == '__main__':
    print(f"当前父进程id:{os.getppid()}")
    start = time.time()
    for i in range(2):
        task()
    end = time.time()
    print(f"所用时间是{int(end - start)}")
