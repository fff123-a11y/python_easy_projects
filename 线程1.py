import time
import threading


def learn():
    print("我叫fzk，我的学习优秀")
    time.sleep(2)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=learn)
        t.start()


def learn(name, score):
    print(f"我的姓名是{name},我的学习是{score}")
    time.sleep(2)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=learn, args=("fzk", "优秀"))
        t.start()
