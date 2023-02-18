import gevent


def customer1():
    print("老板，这猪肉怎么卖？")
    gevent.sleep(2)
    print("卖不了算了，走了")


def customer2():
    print("猪肉12.8块一斤")
    gevent.sleep(1)
    print("那要亏本了，好歹让我赚个几毛，大家都不容易的")


def customer3():
    print("便宜一点，10块卖不卖？")
    gevent.sleep(3)
    print("来来来，给你，你不要跟别人说哈！")


gevent.joinall([gevent.spawn(customer1), gevent.spawn(customer2), gevent.spawn(customer3)])

"""
1.C
协程可以实现，你想让它执行到哪里就执行到哪里
2.ABC
"""
