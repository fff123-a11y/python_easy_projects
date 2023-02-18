"""
class 类名(父类名):
		pass
"""


class Father:
    def __init__(self):
        self.eye = "丹凤眼"
        print("构造方法")

    def car(self):
        print(f"爸爸的车,{self.eye}")

    def home(self):
        print("爸爸的房")

    def money(self):
        print("爸爸的钱")


class Myself(Father):
    def test(self):
        print("这是一个测试")


m = Myself()
m.test()
m.car()
m.home()
m.money()


# print(m.eye)

# grandfather(爷爷)   father(爸爸)   myself（我）
#  爸爸 继承于 爷爷  ，我 继承于 爸爸    我自己 =》爸爸=》 爷爷
class Grandfather:
    def __init__(self):
        self.name = "爷爷"

    def home(self):
        print("爷爷的别墅")


class Father(Grandfather):
    def car(self):
        print("老爷车")


class Myself(Father):
    def money(self):
        print("我有100万")

    def girlFriend(self):
        print("我还差个女朋友")


myself = Myself()
myself.home()
myself.car()
myself.money()
myself.girlFriend()
print(myself.name)


# 总结：子类可以继承父类和父类的父类所有的属性和方法

# 思考：如果爷爷有房，爸爸也有房，我自己也有房，那么最后输出的会是谁的房？
class Grandfather:
    def home(self):
        print("四合院")


class Father(Grandfather):
    def home(self):
        print("父亲的茅草屋")


class Myself(Father):
    def home(self):
        # # 父类名.方法名(self)
        # Father.home(self)
        # super().父类方法名()  # super()只能调用本身的父类（就近原则）
        super().home()
        Grandfather.home(self)  # 类名
        print("我的土坯房")


myself = Myself()
myself.home()


# 总结：子类会覆盖父类的方法

# class 类名:


# class Test:
#     pass
#
# t = Test()
# print(t)
# class 类名():
# class Test():
#     pass
#
#
# t = Test()
# print(t)

# class 类名(object)
# object 是一个类
class Test(object):  # 推荐写这种方式  按住ctrl+点击鼠标左键
    pass


t = Test()
print(t)


# 因为子类会继承父类的所有属性和方法，而有object为父类的，就会继承object类，那么就有拥有object的所有属性和方法
# 快速消除黄色波浪线：ctrl+alt  L

class Master(object):
    def __init__(self):
        self.kongfu = "徒弟用师傅传授的煎饼果子秘方"

    def make_cake(self):
        print(f"{self.kongfu}制作煎饼果子")


class Practice(Master):
    pass


erha = Practice()
erha.make_cake()


class Master(object):
    def __init__(self):
        self.kongfu = "煎饼果子秘方"

    def make_cake(self):
        print(f"师傅的{self.kongfu}")


class School(object):
    def __init__(self):
        self.kongfu = "二哈独创的煎饼果子秘方"

    def make_cake(self):
        print(f"运用{self.kongfu}做煎饼果子")


class Practice(School, Master):
    pass


erha = Practice()
print(erha.kongfu)
erha.make_cake()

# 定义师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 创建学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 2.1 super()带参数写法
        # super(School,self).__init__()
        # super(School,self).make_cake()

        # 2.2无参数的super
        super().__init__()
        super().make_cake()

# 定义徒弟类
# 独创配方
class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
    def make_cake(self):
        # 如果不加自己初始化，导致kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因；这是想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 需求：一次性调用父类School Master的方法
    def make_old_cake(self):
        # 方法1：如果定义的类名修改，此处也要修改，代码量庞大，冗余
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法2：super()
        # 2.1：super(当前类名,self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 2.2 无参数super
        super().__init__()
        super().make_cake()

daqiu = Prentice()
daqiu.make_old_cake()

f = open('text.txt', 'w')
a_str = input("请输入字符串：")
f.write(a_str.upper())
f = open('text.txt', 'r')
print(f.read())

f.close()
