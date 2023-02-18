name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
height = input("请输入你的身高：")
print("请输入你的名字：%s \n请输入你的年龄：%s \n请输入你的身高：%s" % (name, age, height))

length = int(input("请输入矩形的长："))
width = int(input("请输入矩形的宽："))
size = length * width
print(size)

a = 10
b = 20
c = 10
d = 20
print((a == c) and (b == c))  # False 因为a==c为真,b==c为假，有假则假
print((a > c) or (a < b))  # True 因为a>c为假，a<b为真，根据or语句的定义，则为真

name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
height = input("请输入你的身高：")
print(f"请输入你的姓名：{name}, 请输入你的年龄：{age}, 请输入你的身高：{height}", sep="\n")
"""




"""
if True:
    print("条件1")
if True:
    print("条件2")

score = 66
if score >= 80:
    print("优秀！")
elif score >= 70:
    print("很好！")
elif score >= 60:
    print("及格！")
else:
    print("不及格")

score = 56
if score >= 60:
    if score % 2 == 0:
        print("及格，分数为偶数")
    else:
        print("及格，分数为奇数")
else:
    if score % 2 == 0:
        print("不及格，分数为偶数")
    else:
        print("不及格，分数为奇数")

score = 80
print("及格" if score >= 60 else "不及格")
result = "及格" if score >= 60 else "不及格"
print(result)

age = int(input("请输入你的年龄："))
if age >= 18:
    print("可以上网")
else:
    print("不可以上网")
print("可以上网" if age >= 18 else "不可以上网")
result = "可以上网" if age >= 18 else "不可以上网"
print(result)

money_num = int(input("班长口袋里的钱数："))
if money_num >= 2000:
    print("班长请大家吃西餐")
elif 1500 <= money_num < 2000:
    print("班长请大家吃快餐")
elif 1000 <= money_num < 1500:
    print("班长请大家喝饮料")
elif 500 <= money_num < 1000:
    print("班长请大家吃棒棒糖")
else:
    print("班长下次把钱带够")

liquid_alcohol_num = int(input("酒精含量(mg/100ml):"))
if liquid_alcohol_num < 20:
    print("不构成酒驾")
elif liquid_alcohol_num >= 20:
    print("构成酒驾")
if liquid_alcohol_num >= 80:
    print("构成醉驾")

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

print(111)
