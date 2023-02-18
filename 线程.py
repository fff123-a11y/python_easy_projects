import time
import threading


def tortoise():
    for i in range(1, 11):
        print(f"乌龟跑了{i}米")
        time.sleep(1)


def rabbit():
    for i in range(1, 11):
        print(f"兔子跑了{i}米")
    time.sleep(2)


def rabbit_sleep():
    for i in range(2, 5):
        print("兔子在睡觉")
    time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=tortoise)
    t2 = threading.Thread(target=rabbit)
    t1.start()
    t2.start()

if __name__ == '__main__':
    t3 = threading.Thread(target=rabbit_sleep)
    t3.start()
    t3.join()
