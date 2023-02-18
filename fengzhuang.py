# 	私有属性 ：__属性名=属性值
class GirlFriend:
    name = "美女"
    # 私有属性 ：__属性名=属性值 =>无法在外部直接访问（掌握）
    __secret = "秘密"
    # 声明私有属性 ：_属性名=属性值 =>外部可以直接访问
    _age = 18

    # 1.在类里面定义一个方法
    # 2.在方法里面访问私有属性
    # 3.在类外面访问该方法
    def test(self):
        print(self.__secret)
        # 类名.__私有方法(self)
        # GirlFriend.__private(self)  # 需要self
        # self.__私有方法()  # 不需要self
        self.__private()

    def __private(self):
        print("私有方法")

    def _name(self):
        print("声明私有方法")


g = GirlFriend()
print(g.name)
# print(g.__secret)
# # 第一种： _类名__私有属性名  （不推荐） =>了解
# print(g._GirlFriend__secret)
g.test()
# 总结：私有属性类外和子类都不能访问
print(g._age)
# 调用私有方法
# g.__private()
g._name()
