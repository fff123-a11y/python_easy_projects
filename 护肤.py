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
