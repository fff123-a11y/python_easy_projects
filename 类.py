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
