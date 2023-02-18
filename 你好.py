# import threading
# import time
#
#
# def show():
#     for i in range(5):
#         print("子线程", i)
#         time.sleep(0.4)
#
#
# if __name__ == '__main__':
#     # 创建子线程
#     t = threading.Thread(target=show)
#     # 开启线程
#     t.start()
#     # 主线程延迟0.5秒
#     time.sleep(0.5)
#     print("主线程结束")
#
#     # 主线程会等待所有的子线程执行完毕再结束


# 如果我想要主线程结束就结束，不再执行子线程怎么做？
# 1. threading.Thread(target=show_info, daemon=True)
# 2. 线程对象.setDaemon(True)
import threading
import time


def show():
    for i in range(5):
        print("子线程", i)
        time.sleep(0.4)


if __name__ == '__main__':
    # 创建子线程
    # 1. threading.Thread(target=show_info, daemon=True)
    # t = threading.Thread(target=show, daemon=True)
    t = threading.Thread(target=show)
    # 2. 线程对象.setDaemon(True)
    t.setDaemon(True)
    # 开启线程
    t.start()
    # 主线程延迟0.5秒
    time.sleep(0.5)
    print("主线程结束")

# mutex = threading.Lock()   创建锁
# mutex.acquire()  上锁
# 这里编写代码能保证同一时刻只能有一个线程去操作, 对共享数据进行锁定
# mutex.release() 释放锁
import threading

g_num = 0
# 1.创建锁
lock = threading.Lock()


# 每循环一次给全局变量加1
def sum_num1():
    # 2.上锁
    lock.acquire()
    # 3.这里编写代码能保证同一时刻只能有一个线程去操作, 对共享数据进行锁定
    for i in range(1000000):
        global g_num
        g_num += 1
    print(f"sum1:{g_num}")
    # 4.释放锁
    lock.release()


def sum_num2():
    # 2.上锁
    lock.acquire()
    # 3.这里编写代码能保证同一时刻只能有一个线程去操作, 对共享数据进行锁定
    for i in range(1000000):
        global g_num
        g_num += 1
    print(f"sum2:{g_num}")
    # 4.释放锁
    lock.release()


# 2. 创建两个子线程执行对应的两个函数，查看计算后的结果
if __name__ == '__main__':
    # 创建子线程
    s1 = threading.Thread(target=sum_num1)
    s2 = threading.Thread(target=sum_num2)

    # 开启线程
    s1.start()
    s2.start()
