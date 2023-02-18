class GirlFriend():
    name = "安琪拉"
    looks = "安琪拉长得很漂亮"
    figure = "前凸后翘"

    def __init__(self, name, looks, figure):
        self.name = name
        self.looks = looks
        self.figure = figure


print("安琪拉长得很漂亮，前凸后翘")

sing = "唱歌很好听"
dance = "跳爵士舞很好看"


def __init__(self, sing, dance):
    self.sing = sing
    self.dance = dance


print("安琪拉跳爵士舞很好看，唱歌很好听")


class Hero():
    def __init__(self, name, life, attack_power):
        self.name = name
        self.life = life
        self.attack_power = attack_power
        self.move()
        self.attackD()

    def move(self):
        print(f"{self.name}在移动")

    def attackD(self):
        print(f"{self.name}的生命值{self.life},发出了一招{self.attack_power}")


lb = Hero("李白", 200, 100)
lb.move()
lb.attackD()

y = Hero("瑶", 100, 50)
y.move()
y.attackD()

"""
类里面：
    1.定义类属性：属性名=值
    2.调用类属性：1.类名=属性名 2.self.属性名
    3.定义实例属性：self.属性名 = 值
    4.调用实例属性：self.属性名
    5.定义方法：1.无参数：def 方法名（self) 2.有参数：def 方法名（self,参数）
    6.调用方法：1.self.方法名（）2.类名.方法名(self)
"""


class Number:
    print("2")


Number()
z = Number()  # 2

"""
类外：
    定义类属性：类名.属性名 = 值
    调用类属性：1.类名.属性名 2.对象名.属性名
    定义实例属性：self.属性名
    调用实例属性：对象名.属性名
    调用方法：对象名.方法名()
"""
