# 列表
num_list = [19, 89, 90, 80, 1, 11, 23, 64]
index_ = 0
for i in range(len(num_list)):
    if num_list[index_] % 2 == 0:
        print(num_list[index_])
        num_list.remove(num_list[index_])
    else:
        index_ += 1
print(num_list)
num_list.pop()
print(num_list)

iphone11 = ['jack', 'rain', 'shanshan', 'tom']
iphone12 = ['jack', 'rain', 'tom', 'huhu']
iphone_list = []
for i in iphone11:
    if i in iphone12:
        iphone_list.append(i)
print(iphone_list)

city_list = ["北京", "上海", "深圳", "长沙"]
city_list[1] = '广州'
print(city_list)

name_list = ['Tom', 'Lily', 'Rose']
name_list.append('Cara')
print(name_list)
name_list.insert(1, '灼灼')
print(name_list)
i = 0
while i < len(name_list):
    print(name_list[i])
    i = i + 1

str1 = input("请输入字符串：")
upper = 0
lower = 0
digit = 0
others = 0
i = 0
for i in str1:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print("大写字母有：%s个\n小写字母有：%s个\n数字有：%s个\n其它字符有：%s个" % (upper, lower, digit, others))

fruits = '苹果5个，香梨4个， 西瓜3个， 哈密瓜6个， 桃子3个， 桔子7个'
sum = 0
for i in fruits:
    if i.isdigit():
        i = int(i)
        sum = sum + i
print(sum)


# 函数
def print1():
    print("-" * 20)


print1()


def print2():
    for i in range(0, 5):
        print("-" * 20, end="\n")


print2()


def sum_num(a, b, c):
    return a + b + c


result = sum_num(5, 4, 3)
print(result)


def sums(a):
    i = 1
    sum = 0
    while i <= a:
        sum += i
        i += 1
    print(sum)


sums(3)


def average(number1, number2, number3):
    return int((number1 + number2 + number3) / 3)


result = average(2, 4, 6)
print(result)


def averages(b):
    i = 1
    num = 1
    while i <= b:
        sum = int((num + i) / 3)
        i += 1
        num += i
    print(int(num + i) / 3)


averages(3)

# 模块
import random

# 玩家出拳
player = input("请出拳：0--石头，1--剪刀，2--布：")
# 电脑出
computer = str(random.randint(0, 2))
print("电脑出的是", computer)
# 判断输赢
if (player == '0' and computer == '1') or (player == '1' and computer == '2') or (player == '2' and computer == '0'):
    print("玩家获胜！")
elif (player == computer):
    print("平局！")
else:
    print("电脑获胜！")

import random

for i in range(3):
    guess_num = input("请输入一个数字：")
    real_num = str(random.randint(1, 10))
    print("电脑数字是：", real_num)
    if guess_num > real_num:
        print("数字大了，继续猜：")
    elif guess_num < real_num:
        print("数字小了，继续猜：")
    elif guess_num == real_num:
        print("猜对了！")
        break
    else:
        print("结束程序！")
        break

try:
    a = int(input("请输入一个数a:"))
    b = int(input("请输入一个数b:"))
except ValueError:
    print("你输入的不是数字，请输入数字！")
else:
    result = int(a + b)
    print(result)
