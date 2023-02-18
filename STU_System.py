import csv
import time


class Administration(object):
    def __init__(self):
        self.data = self.__load()
        self.login_data = {}

    def __load(self) -> list:
        try:
            Adm = open('Administration.csv', 'r')
            readers = csv.DictReader(Adm)
            Adm_dict = [dict(i) for i in readers]
            Adm.close()
            return Adm_dict
        except Exception:
            print('文件读取失败')

    def see_course(self):
        print('当前所有的课程信息为：')
        for i in cou.data:
            print(i)
        print()

    def see_student(self):
        print('当前所有的学生信息为：')
        for i in stu.data:
            print(i)
        print()

    def see_student_course(self):
        print('当前所有学生的选课信息为:')
        for i in stu.data:
            print(i['姓名'], '的选课信息为：', i['课程'])
        print()

    def set_course(self):
        name = input('请输入你想添加的课程名')
        c = [i['名称'] for i in cou.data]
        if name in c:
            print('你准备添加的课程 已经存在')
        else:
            cou.data.append({'名称': name, '人数': 0})
            print('添加成功!')
            print()

    def set_student(self):
        name = input('请输入你想添加的学生的姓名')
        ID = input('请输入此学生的ID')
        if ID in [i['ID'] for i in stu.data]:
            print('这个ID已经存在，添加失败')
            return
        print('学生账号默认密码123456')
        password = 123456
        stu.data.append({'姓名': name, 'ID': ID, '密码': password, '课程': ''})
        print('添加成功!')
        print()

    def set_teacher(self):
        name = input('请输入你想添加的老师的姓名')
        ID = input('请输入此老师的ID')
        if ID in [i['ID'] for i in tea.data]:
            print('这个ID已经存在，添加失败')
            return
        print('老师账号默认密码123456')
        password = 123456
        tea.data.append({'姓名': name, 'ID': ID, '密码': password, '课程': ''})
        print('添加成功!')
        print()

    def app_teacher_to_class(self):
        t_name = input('请输入你想操作的老师名')
        if t_name not in [i['姓名'] for i in tea.data]:
            print('你想操作的老师不存在，请重新操作')
            return
        c_name = input('请输入你想让该老师任课的班级')
        if c_name not in [i['班名'] for i in cla.data]:
            print('你想让老师任教的班级不存在，请重新操作')
            return
        for i in tea.data:
            if i['姓名'] == t_name:
                i['班级'] = c_name
        for i in cla.data:
            if i['班名'] == c_name:
                i['任课老师'] = t_name
        print('操作成功')

    def set_class(self):
        name = input('请输入你想创建的班级的名称:')
        if name in [i['班名'] for i in cla.data]:
            print('你想创建的班级已经存在，请重新操作')
            return
        if int(input('是否添加任课老师，是输入1，否输入0')):
            t_name = input('请输入你想添加的老师名')
            if t_name not in [i['姓名'] for i in tea.data]:
                print('你想操作的老师不存在，请重新操作')
                return
        else:
            t_name = ''
        s_name_list = []
        while int(input('是否添加学生，是输入1，否输入0')):
            s_name = input('输入你想添加的学生名')
            if s_name not in [i['姓名'] for i in stu.data]:
                print('你想操作的学生不存在，请重新操作')
                return
            else:
                s_name_list.append(s_name)
        s_name = ''
        if s_name_list == []:
            cla.data.append({'班名': name, '任课老师': t_name, '学生': s_name})
            print('操作成功')
        else:
            cla.data.append({'班名': name, '任课老师': t_name,
                             '学生': s_name.join(s_name_list)})
            print('操作成功')

    def app_student_to_class(self):
        s_name = input('请输入你想操作的学生名')
        if s_name not in [i['姓名'] for i in stu.data]:
            print('你想操作的学生不存在，请重新操作')
            return
        c_name = input('请输入你想让该学生进入的班级')
        if c_name not in [i['班名'] for i in cla.data]:
            print('你想让学生进入的班级不存在，请重新操作')
            return
        for i in stu.data:
            if i['姓名'] == s_name:
                i['班级'] = c_name
        for i in cla.data:
            if i['班名'] == c_name:
                i['任课老师'] = s_name
        print('操作成功')

    def save(self):
        try:
            j = open('Administration.csv', 'w')
            writer = csv.writer(j)
            writer.writerow(list(self.data[0].keys()))
            data = [list(i.values()) for i in self.data]
            writer.writerows(data)
            j.close()
        except Exception:
            print('文件读取失败')


class Student(object):
    def __init__(self):
        self.data = self.__load()
        self.login_data = {}

    def __load(self):
        try:
            Stu = open('Student.csv', 'r')
            readers = csv.DictReader(Stu)
            Stu_dict = [dict(i) for i in readers]
            Stu.close()
            return Stu_dict
        except Exception:
            print('文件读取失败')

    def see_course(self):
        print('当前所有的课程信息为：')
        for i in cou.data:
            print(i)
        print()

    def choice_course(self):
        # print(self.data)
        c = [i['名称'] for i in cou.data]
        c_name = input('请输入你想选择的课程名：')
        if c_name not in c:
            print('你选择的课程不在课程列表中')
            return
        else:
            self.login_data['课程']: str = self.login_data['课程'] + c_name + ' '
            for i in cou.data:
                if i['名称'] == c_name:
                    i['人数'] = int(i['人数']) + 1
        print('操作成功')

    def see_own_course(self):
        if self.login_data['课程'] == '':
            print('你未选择任何课程')
        else:
            print(self.login_data['课程'])

    def save(self):
        try:
            j = open('Student.csv', 'w')
            writer = csv.writer(j)
            writer.writerow(list(self.data[0].keys()))
            data = [list(i.values()) for i in self.data]
            writer.writerows(data)
        except Exception:
            print('文件读取失败')


class Course(object):
    def __init__(self):
        self.data = self.__load()

    def __load(self):
        try:
            Cou = open('Course.csv', 'r')
            readers = csv.DictReader(Cou)
            Cou_dict = [dict(i) for i in readers]
            Cou.close()
            return Cou_dict
        except Exception:
            print('文件读取失败')

    def save(self):
        try:
            j = open('Course.csv', 'w')
            writer = csv.writer(j)
            writer.writerow(list(self.data[0].keys()))
            data = [list(i.values()) for i in self.data]
            writer.writerows(data)
        except Exception:
            print('文件读取失败')


class Classroom(object):
    def __init__(self):
        self.data = self.__load()

    def __load(self):
        try:
            Cla = open('Classroom.csv', 'r')
            readers = csv.DictReader(Cla)
            Cla_dict = [dict(i) for i in readers]
            Cla.close()
            return Cla_dict
        except Exception:
            print('文件读取失败')

    def save(self):
        try:
            j = open('Classroom.csv', 'w')
            writer = csv.writer(j)
            writer.writerow(list(self.data[0].keys()))
            data = [list(i.values()) for i in self.data]
            writer.writerows(data)
        except Exception:
            print('文件读取失败')


class Teacher(object):
    def __init__(self):
        self.data = self.__load()
        self.login_data = {}

    def __load(self):
        try:
            Tea = open('Teacher.csv', 'r')
            readers = csv.DictReader(Tea)
            Tea_dict = [dict(i) for i in readers]
            Tea.close()
            return Tea_dict
        except Exception:
            print('文件读取失败')

    def see_course(self):
        print('当前所有的课程信息为：')
        for i in cou.data:
            print(i)
        print()

    def see_class(self):
        print('所教班级为:', self.login_data['班级'])
        print()

    def see_class_student(self):
        print('所教班级中的学生为：')
        for i in cla.data:
            if i['班名'] == self.login_data['班级']:
                print(i['学生'])
        print()

    def save(self):
        try:
            j = open('Teacher.csv', 'w')
            writer = csv.writer(j)
            writer.writerow(list(self.data[0].keys()))
            data = [list(i.values()) for i in self.data]
            writer.writerows(data)
        except Exception:
            print('文件读取失败')


def login(ID, password) -> int:
    # 判断是否为管理员
    for i in adm.data:
        if ID == i['ID'] and password == i['密码']:
            adm.login_data = i
            return 1
    # 判断是否为学生
    for i in stu.data:
        if ID == i['ID'] and password == i['密码']:
            stu.login_data = i
            return 2
    # 判断是否为老师
    for i in tea.data:
        if ID == i['ID'] and password == i['密码']:
            tea.login_data = i
            return 3
    return 0


if __name__ == '__main__':
    print('欢迎来到我的学生管理系统')
    time.sleep(0.5)
    print('正在加载中~')
    adm = Administration()
    stu = Student()
    cou = Course()
    tea = Teacher()
    cla = Classroom()
    time.sleep(0.3)
    print('加载完毕')
    while True:
        ID = input('请输入你的账号：')
        password = input('请输入你的密码：')
        flag = login(ID, password)
        if not flag:
            print('输入的账号或密码错误')
            flag_1 = int(input('是否重新登录 重新登录输入1 取消登录输入0'))
            if flag_1:
                continue
            else:
                break
        elif flag == 1:
            print('欢迎管理员')
            break
        elif flag == 2:
            print('欢迎学生')
            break
        elif flag == 3:
            print('欢迎老师')
            break
    if flag == 1:
        while True:
            check = int(
                input(
                    '1.创建课程\n2.创建学生账号\n3.查看所有课程\n4.查看所有学生\n5.查看所有学生的选课信息\n6.创建讲师'
                    '\n7.为讲师指定班级\n8.创建班级\n9.为学生指定班级\n10.退出程序'))
            if check == 1:
                adm.set_course()
            elif check == 2:
                adm.set_student()
            elif check == 3:
                adm.see_course()
            elif check == 4:
                adm.see_student()
            elif check == 5:
                adm.see_student_course()
            elif check == 6:
                adm.set_teacher()
            elif check == 7:
                adm.app_teacher_to_class()
            elif check == 8:
                adm.set_class()
            elif check == 9:
                adm.app_student_to_class()
            elif check == 10:
                break
    elif flag == 2:
        while True:
            check = int(input('1.查看所有课程\n2.查看所选课程\n3.选择课程\n4.退出程序'))
            if check == 1:
                stu.see_course()
            elif check == 2:
                stu.see_own_course()
            elif check == 3:
                stu.choice_course()
            elif check == 4:
                break
    elif flag == 3:
        while True:
            check = int(input('1.查看所有课程\n2.查看所教班级\n3.查看班级中的学生\n4.退出程序'))
            if check == 1:
                tea.see_course()
            elif check == 2:
                tea.see_class()
            elif check == 3:
                tea.see_class_student()
            elif check == 4:
                break
    print('数据存储中~')
    adm.save()
    tea.save()
    stu.save()
    cla.save()
    cou.save()
    time.sleep(0.5)
    print('感谢您的使用！')

