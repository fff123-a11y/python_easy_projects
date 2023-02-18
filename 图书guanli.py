import os

syslist = []  # 新建列表存储音像图书对象
list = []  # 新建列表存储借阅者对象


# 定义一个类，类中又音像图书的各种属性
class RandB_sys:
    def __init__(self, price, num, num1):
        self.name = ""  # 名称
        self.id = ""  # 音像图书ID
        self.price = price  # 原价
        self.num = num  # 原数量
        self.num1 = num1  # 剩余数量

    def find(self, book):
        if book.name == book:
            return book
        else:
            return None

    # 输出各种属性
    def output(self, file_object):
        file_object.write(self.name)
        file_object.write(" ")
        file_object.write(self.id)
        file_object.write(" ")
        file_object.write(str(self.price))
        file_object.write(" ")
        file_object.write(str(self.num))
        file_object.write(" ")
        file_object.write(str(self.num1))
        file_object.write("\n")


# 租借者的类
class people:
    def __init__(self, cash, days, rent):
        self.number = ""  # 租借者编号
        self.year = ""  # 租借日期 年
        self.month = ""  # 月
        self.day = ""  # 日
        self.cash = cash  # 押金
        self.days = days  # 租借天数
        self.rent = rent  # 租金

    # 输出函数
    def output1(self, file_object):
        file_object.write(self.number)
        file_object.write(" ")
        file_object.write(self.year)
        file_object.write(" ")
        file_object.write(self.month)
        file_object.write(" ")
        file_object.write(self.day)
        file_object.write(" ")
        file_object.write(str(self.cash))
        file_object.write(" ")
        file_object.write(str(self.days))
        file_object.write(" ")
        file_object.write(str(self.rent))
        file_object.write("\n")


# 创建音像图书库
def Library():
    book = RandB_sys(20, 30, 30)
    book.name = input("请输入音像图书名称：")
    book.id = input("请输入图书编号：")
    if (cfindstu(book.id) != -1):
        print("该图书已存在，添加失败")
        return False
    # 添加音像图书其他信息
    book.price = int(input("请输入音像图书原价："))
    book.num = int(input("请输入音像图书原数量:"))
    book.num = int(input("请输入音像图书剩余的数量:"))
    syslist.append(book)
    print("添加成功！")
    return True


# 查看是否重复
def cfindstu(idin):
    for i in range(0, len(syslist)):
        if (idin == syslist[i].id):
            return i
    return -1


def cfindsys(numberin):
    for i in range(0, len(syslist)):
        if (numberin == syslist[i].id):
            return i
    return -1


# 租借音像图书
def Borrow():
    aud_book = RandB_sys(20, 30, 30)
    audio = people(60, 60, 12)
    name = input("请输入即将租借的音像图书的名称：")
    number = int(input("请输入租借者编号:"))
    if (aud_book.num1 == 0):
        print("该图书已全部借走")
        return False
    if (cfindsys(number) != -1):
        print("该租借者编号已经存在，请确认后重新输入!!")
        return False
    else:
        print("请输入租借日期")
        year1 = int(input("年:"))
        month1 = int(input("月:"))
        day1 = int(input("日:"))
        price = 10
        cash = price * 3
        print("押金为{}元".format(cash))
        aud_book.num1 -= 1
        print("还剩{}册".format(aud_book.num1))

    return True


# 归还音像图书
def ReturnBook():
    aud_book = people(60, 60, 12)
    aud_book1 = RandB_sys(20, 30, 30)
    idkind = aud_book1.id[0:2]
    number = int(input("请输入租借者编号:"))
    print("归还音像图书为{}".format(aud_book1.name))
    # 借书日期
    print("借书日期：")
    year1 = int(input("年:"))
    month1 = int(input("月:"))
    day1 = int(input("日:"))
    # 还书日期
    print("还书日期：")
    year = int(input("年:"))
    month = int(input("月:"))
    day = int(input("日:"))
    #         判断种类是否为图书
    if (idkind == 'B_'):
        time = (year - year1) * 365 + (month - month1) * 30 + (day - day1)
        print("时间为{}天".format(time))
        aud_book.rent = 0.2 * time
    #     判断种类是否为VCD
    elif (idkind == 'V_'):
        time = (year - year1) * 365 + (month - month1) * 30 + (day - day1)
        print("时间为{}天".format(time))
        aud_book.rent = 0.1 * time
        #     判断种类是否为VCD
    elif (idkind == 'D_'):
        time = (year - year1) * 365 + (month - month1) * 30 + (day - day1)
        print("时间为{}天".format(time))
        aud_book.rent = 0.3 * time
        return False
    #         判断租金是否大于押金
    if (aud_book.rent == aud_book.cash):
        print("租金为{}元".format(aud_book.cash))
    else:
        print("租金为{}元".format(aud_book.rent))
    print("已删除租借者信息!")
    return True


# 购进音像图书
def buyBook():
    sys1 = RandB_sys(20, 30, 30)
    sys1.name = input("请输入名称：")
    sys1.id = input("请输入音像图书编号：")
    if (cfindstu(sys1.id) != -1):
        print("该音像或图书已存在，添加失败")
        return False
    num1 = int(input("请输入新添加的音像图书数量："))
    sys1.num += num1
    syslist.append(sys1)
    print("添加成功！")
    return True


# 报废音像图书
def delBook():
    audio_Bk = RandB_sys(20, 30, 30)
    idin = input("请输入你要报废的音像图书的编号：")
    # 利用查重函数返回删除学生在列表中坐标
    result = cfindstu(idin)
    if (audio_Bk.num1 != audio_Bk.num1):
        print("此音像图书已借出，不能报废")
    else:
        if result == -1:
            print("该音像或图书不存在，请重新输入")
        else:
            for i in range(result, len(syslist) - 1):
                syslist[i] = syslist[i + 1]
            del syslist[len(syslist) - 1]
            print("此书已报废")


# 将音像图书信息保存到文件
def writeinfo():
    if os.path.exists('Audio_Book.txt'):
        os.remove('Audio_Book.txt')
    i = 0
    while i < len(syslist):
        with open("Audio_Book.txt", "a") as file_object:
            syslist[i].output(file_object)
            file_object.close()
            i += 1


# 将信息读取到文件中
def readinfo():
    if os.path.exists('Audio_Book.txt'):
        file_object = open('Audio_Book.txt', 'r')
        # 遍历
        for line in file_object:
            sys1 = RandB_sys(20, 30, 30)
            line = line.strip("\n")
            s = line.split(" ")
            # 音像图书信息所在位置
            sys1.name = s[0]
            sys1.id = s[1]
            sys1.price = int(s[2])
            sys1.num = int(s[3])
            sys1.num1 = int(s[4])
            syslist.append(sys1)
        file_object.close()
        print("加载成功")
    else:
        print("没有文件信息，加载失败")


def main():
    print("欢迎来到音像图书租借管理系统")
    print("|", "-" * 30, "|")
    print("|    |")
    print("|", "-" * 30, "|")
    print("-" * 15, "菜单", "-" * 15)
    print("|        1——创建音像图书库      |")
    print("|        2——租借音像图书        |")
    print("|        3——归还音像图书        |")
    print("|        4——购进音像图书        |")
    print("|        5——报废音像图书        |")
    print("|        6——退出系统            |")
    print("正在加载文件信息···")
    readinfo()  # 读取文件信息
    # 主循环
    while True:
        writeinfo()  # 保存到文件
        a = input("请选择：")
        if (a == "1"):
            Library()
        elif a == "2":
            Borrow()
        elif a == "3":
            ReturnBook()
        elif (a == "4"):
            buyBook()
        elif (a == "5"):
            delBook()
        elif a == "6":
            print("已退出！")
            print("文件信息已更新！")
            break
        else:
            print("选择有误，请重新选择")


main()
