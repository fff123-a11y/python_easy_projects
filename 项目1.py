# 1. 公共类 / 父类
class Person1():
    # 定义__init__初始化方法，__height私有属性
    def __init__(self, name, __height,age=20):
        self.name = name
        self.age = age
        self.__height=__height

    # 方法

    def eat(self):
        print('我要吃了！')
        return

    def drink(self):
        print('我开始喝了！')
        return

    def __write(self):  # 注意此处 两个下划线 __ 开头 代表私有方法
        print('我要开始写作文了')

    # 位置参数
    def show_hello(name1, sex):
        sex_dict = {1: u'先生', 2: u'女士'}
        print(f"Hello,{name1} {sex_dict.get(sex, u'先生')}, welcome to python world! ")

    show_hello('xiaowu',1)


# 定义子类 Student  继承person类
class Student(Person1):
    pass


p = Person1('snail','1.89m')
s1 = Student('xiaowu','1.82m')
s1.eat()
s1.drink()
