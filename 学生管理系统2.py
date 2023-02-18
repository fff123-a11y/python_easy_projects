import os
import pandas as pd

stulist = []  # 新建学生列表存储学生对象


class stu:
    def __init__(self):
        self.name = ""  # 学生姓名
        self.id = ""  # 学生ID
        self.score = 0  # 成绩

    def output(self, file_object):
        file_object.write(self.name)
        file_object.write(" ")
        file_object.write(self.id)
        file_object.write(" ")
        file_object.write(str(self.score))
        file_object.write("\n")


# 添加学生信息
def addstu():
    student = stu()
    student.name = input("请输入学生姓名：")
    student.id = input("请输入学生学号：")
    if (cfindstu(student.id) != -1):
        print("该学生已存在，添加失败")
        return False

    student.score = int(input("请输入学生成绩："))
    stulist.append(student)
    print("添加成功！")
    return True


# 查找学生信息
def findstu():
    idin = input("请输入学生学号：")
    for i in range(0, len(stulist)):
        if (idin == stulist[i].id):
            print("该学生信息如下：")
            print("学号：", stulist[i].id, end="\t")
            print("姓名：", stulist[i].name, end="\t")
            print("成绩：", stulist[i].score, end="\t")
            return True
    print("没有该学生信息")
    return False


# 查重 已存在：返回列表中坐标；不存在：返回-1
def cfindstu(idin):
    for i in range(0, len(stulist)):
        if (idin == stulist[i].id):
            return i
    return -1


# 查看所有学生信息
def checkstudent():
    print("学生信息如下：")
    print("=" * 50)  # 换行
    if len(stulist) == 0:
        print("当前无学生信息")
    for i in range(0, len(stulist)):
        print("学号：", stulist[i].id, end="\t")
        print("姓名：", stulist[i].name, end="\t")
        print("成绩：", stulist[i].score, end="\t")
        print("-" * 50)  # 换行


# 删除学生信息
def delstu():
    idin = input("请输入你要删除学生的学号：")
    # 利用查重函数返回删除学生在列表中坐标
    result = cfindstu(idin)
    if result == -1:
        print("该学生不存在")
    else:
        for i in range(result, len(stulist) - 1):
            stulist[i] = stulist[i + 1]
        del stulist[len(stulist) - 1]
        print("删除成功")


# 修改学生信息
def changestu():
    idin = input("请输入你要修改学生的学号：")
    result = cfindstu(idin)
    # 学生信息不存在时，返回-1
    if result == -1:
        print("该学生不存在")
    else:
        id = input("请重新输入学生id：")
        if (cfindstu(id) != -1):
            print("该id已存在，修改失败")
            return False
        stulist[result].id = id
        stulist[result].name = input("请重新输入学生姓名：")
        stulist[result].score = int(input("请重新输入学生成绩："))
        print("修改成功，按“5c”查看")


# 按学生成绩排序,采用插入法
def sortstu():
    for i in range(0, len(stulist) - 1):
        for j in range(i + 1, 0, -1):
            if stulist[j].score > stulist[j - 1].score:
                tmp = stu()
                # 冒泡排序算法
                tmp = stulist[j - 1]
                stulist[j - 1] = stulist[j]
                stulist[j] = tmp
    print("排序成功！")
    checkstudent()


# 将学生信息保存到文件
def writeinfo():
    if os.path.exists('students.txt'):
        os.remove('students.txt')
    i = 0
    while i < len(stulist):
        with open("students.txt", "a") as file_object:
            stulist[i].output(file_object)
            file_object.close()
            i += 1


# 将学生信息读取到文件中
def readinfo():
    if os.path.exists('students.txt'):
        file_object = open('students.txt', 'r')
        # 遍历
        for line in file_object:
            stu1 = stu()
            line = line.strip("\n")
            s = line.split(" ")
            # 学生信息所在位置
            stu1.name = s[0]
            stu1.id = s[1]
            stu1.score = int(s[2])
            stulist.append(stu1)
        file_object.close()
        print("加载成功")
    else:
        print("没有文件信息，加载失败")


# 保存到csv中
def writeCsv():
    csv_students = []
    for i in range(0, len(stulist)):
        csv_students.append([stulist[i].id, stulist[i].name, stulist[i].score])

    df = pd.DataFrame(data=csv_students, columns=['学号', '姓名', '成绩'])
    df.to_csv('Stu.csv', index=False)


def main():
    print("欢迎来到学生成绩管理系统")
    print("*" * 30)
    print("-" * 7, "菜单", "-" * 7)
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查找学生信息.")
    print("5.察看所有学生信息")
    print("6.学生成绩排序")
    print("7.退出系统")
    print("正在加载文件信息···")
    readinfo()  # 读取文件信息
    while True:
        writeinfo()  # 保存到文件
        writeCsv()
        a = input("请选择：")
        if (a == "1"):
            addstu()
        elif a == "2":
            delstu()
        elif a == "3":
            changestu()
        elif (a == "4"):
            findstu()
        elif (a == "5"):
            checkstudent()
        elif a == "6":
            sortstu()
        elif a == "7":
            print("已退出！")
            print("文件信息已更新！")
            break
        else:
            print("选择有误，请重新选择")


main()
