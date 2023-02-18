class Master(object):
    def __init__(self):
        self.kongfu = "师傅的精湛的技术"

    def Make_cake(self):
        print(f"徒弟用{self.kongfu}制作煎饼果子")


class Practice(Master):
    pass


erha = Practice()
erha.Make_cake()


class Master(object):
    def __init__(self):
        self.kongfu = "煎饼果子秘方"

    def Make_cake(self):
        print(f"师傅的{self.kongfu}")


class School(object):
    def __init__(self):
        self.kongfu = "独创的煎饼果子秘方"

    def Make_cake(self):
        print(f"二哈用{self.kongfu}制作煎饼果子")


class Practice(School, Master):
    pass


erha = Practice()
print(erha.kongfu)
erha.Make_cake()  # 二哈用独创的煎饼果子秘方制作煎饼果子


class Practice(object):
    def __init__(self):
        self.kongfu = "师傅传授的技术"
        self.money = 200000000

    def Make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

    def Money(self):
        print(f"师傅不想要徒弟给的{self.money}元")


class Tusun(Practice):
    pass


t = Tusun()
t.Money()


# 定义师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 创建学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[六星煎饼果子配方]'

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


# 多继承
class School(object):
    def __init__(self):
        self.technic = "在学校学习java"

    def make_code(self):
        print(f"二哈{self.technic}")


class SixEdu(object):
    def __init__(self):
        self.knowledge = "六星报名学习python"

    def make_code(self):
        print(f"二哈在{self.knowledge}")


class Practice(SixEdu, School):
    pass


erha = Practice()
erha.make_code()


class Bird(object):
    def work(self):
        print("鸟扇动翅膀来飞行")


class Plane(Bird):
    def work(self):
        print("飞机靠空气动力学来飞行")


class Rocket(Plane):
    def work(self):
        print("火箭靠高能燃料飞行")


def Fly(Rocket, Plane, Bird):
    def work(self, obj):
        obj.work()


b = Bird()
p = Plane()
r = Rocket()
b.work()
p.work()
r.work()


class Father(object):
    def sing(self):
        print("父亲会唱歌")


class Mother(object):
    def dance(self):
        print("母亲会跳舞")


class Daughter(Mother, Father):
    def action(self):
        print("女儿会唱歌和跳舞，而且女儿跳舞跳得比母亲还好")


class Taekwondo(object):
    def fight(self):
        print("女儿打架也是把好手")


f = Father()
m = Mother()
d = Daughter()
t = Taekwondo()
f.sing()
m.dance()
d.action()
t.fight()  # 实例化对象
