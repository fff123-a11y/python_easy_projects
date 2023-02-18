import sys
# 定义一个银行卡类
class BankCardHolder():
    CardID = str
    def __init__(self, cardid):
        self.CardID = cardid

# 银行的类
class Bank():
    CardID = "1001"
    def __init__(self, username, password, remainingsum):  # 用户名、密码、余额
        self.CardID = self.CardID
        self.UserName = username
        self.Password = password
        self.RemainingSum = remainingsum
        ATM.BankSys.append(self)
        Bank.CardID = str(int(self.CardID) + 1)

# 定义一个ATM类
class ATM():
    BankSys = []

    def __init__(self):
        self.Money = 50000
        self.Card = None
        self.verify = False

    # 定义一个插卡验证方法
    def chaka(self, card, passwprd):
        for carddata in self.BankSys:
            if self.Card == None or self.Card == card:
                if carddata.CardID == card.CardID:
                    self.Card = card
                    if carddata.Password == passwprd:
                        self.Carddata = carddata
                        self.verify = True
                        return self
                    else:
                        print("密码错误")
                        return
            else:
                return
        print("卡号错误")
        return

    # 退卡函数
    def tuika(self):
        self.Card = None
        self.Carddata = None
        self.verify = False

    # 余额查询方法
    def CCYE(self):
        if self.verify:
            print(self.Carddata.RemainingSum)
            return self.Carddata.RemainingSum

    # 存款方法
    def SaveMoney(self, money):
        if self.verify:
            self.Carddata.RemainingSum += money
            self.Money += money
            print("存款成功")
            return self.Card.CardID + "存款" + str(money)

    # 取款方法
    def withdrawal(self, money):
        if self.verify:
            if self.Money >= money:
                if self.Carddata.RemainingSum >= money:
                    self.Carddata.RemainingSum -= money
                    self.Money -= money
                    print("取款成功")
                    return self.Card.CardID + "取款" + str(money)
                else:
                    print("!!账户余额不足!!")
                    return 1
            else:
                print("!!ATM余额不足无法服务!!")
                return -1

    # 修改密码方法
    def ChangePW(self, oldpassword, newpassword1, newpassword2):
        if self.verify:
            if self.Carddata.Password == oldpassword:
                if newpassword1 == newpassword2:
                    self.Carddata.Password = newpassword1
                    print("修改成功")
                    return True
                else:
                    print("!!两个新密码不相同!!")
                    return 1
            else:
                print("!!密码错误!!")
                return -1

    # 卡号查询方法
    def CardQuery(self, cardid):
        for carddata in self.BankSys:
            if carddata.CardID == cardid:
                print("用户名为：", carddata.UserName)
                verify = input()
                if verify == '0':
                    return carddata
                else:
                    return
        print("!!卡号错误!!")
        return

    # 转账方法
    def EFT(self, cardid, money):
        if self.verify:
            C_Carddata = self.CardQuery(cardid)
            if C_Carddata != None:
                if self.Carddata.RemainingSum >= money:
                    self.Carddata.RemainingSum -= money
                    C_Carddata.RemainingSum += money
                    return self.Card.CardID + "转账" + cardid + "金额：" + str(money)
                else:
                    print("余额不足!")
                    return
            else:
                return

    # 汇款方法
    def remittance(self, cardid, money):
        C_Carddata = self.CardQuery(cardid)
        if C_Carddata != None:
            C_Carddata.RemainingSum += money
            self.Money += money
            return "汇款" + cardid + "金额：" + str(money)
        else:
            return


# 定义一个ATM客户端类
class ATM_client(ATM):
    # 定义插卡
    def C_chaka(self, card):
        print("--------------------欢迎使用----------------------")
        passwprd = input("请输入密码：")
        if self.chaka(card, passwprd) == None:
            self.C_chaka(self.Card)
        else:
            self.C_JH()

    # 定义票据打印
    def C_PrintNote(self, note):
        x = input("打印票据请输入 1 ,退出请按任意键")
        if x == "1":
            print(note)
            if self.verify:
                self.C_JH()
            else:
                sys.exit()
        else:
            if self.verify:
                self.C_JH()
            else:
                sys.exit()

    # 定义存款
    def C_SaveMoney(self):
        money = int(input("请输入存款金额："))
        note = self.SaveMoney(money)
        self.C_PrintNote(note)

    # 定义取款
    def C_withdrawal(self):
        money = int(input("请输入取款金额："))
        note = self.withdrawal(money)
        if note != 1 and note != -1:
            self.C_PrintNote(note)
        elif note == 1:
            if input("回车继续") != '':
                self.C_JH()
            else:
                self.C_withdrawal()
        elif note == -1:
            self.C_JH()

    # 定义修改密码
    def C_ChangePW(self):
        oldpassword = input("请输入原始密码：")
        newpassword1 = input("请输入新密码：")
        newpassword2 = input("请再次输入新密码验证：")
        X = self.ChangePW(oldpassword, newpassword1, newpassword2)
        if X:
            self.C_JH()
        elif input("回车继续") != '':
            self.C_JH()
        else:
            self.C_ChangePW()

    # 定义转账
    def C_EFT(self):
        cardid = input("请输入转账卡号：")
        C_Carddata = self.CardQuery(cardid)
        if C_Carddata is not None:
            money = int(input("请输入转账金额："))
            note = self.EFT(cardid, money)
            if note is not None:
                self.C_PrintNote(note)
            elif input("回车继续") != '':
                self.C_JH()
            else:
                self.C_EFT()
        elif input("回车继续") != '':
            self.C_JH()
        else:
            self.C_EFT()

    # 定义汇款
    def C_remittance(self):
        cardid = input("请输入汇款卡号：")
        C_Carddata = self.CardQuery(cardid)
        if C_Carddata is not None:
            money = int(input("请放入现金："))
            note = self.remittance(cardid, money)
            self.C_PrintNote(note)
        elif input("回车继续") != '':
            if self.verify:
                self.C_JH()
            else:
                self.tuika()
        else:
            self.C_remittance()

    def C_JH(self):
        n = input("查询余额请输入1     存款请输入2\n取款请输入3        修改密码业务请输入4\n转账请输入5        汇款请输入6\n退卡请输入0\n请输入：")
        if n == "1":
            self.CCYE()
            self.C_JH()
        elif n == "2":
            self.C_SaveMoney()
        elif n == "3":
            self.C_withdrawal()
        elif n == "4":
            self.C_ChangePW()
        elif n == "5":
            self.C_EFT()
        elif n == "6":
            self.C_remittance()
        elif n == "0":
            print("--------------------谢谢使用----------------------")
            self.tuika()
            return
        else:
            print('!!请输入正确服务号!!')
            self.C_JH()

cardDT1=Bank("xcx","1022390",100);card1=BankCardHolder("1001")
# cardDT2=Bank("xxx","123456",100);card2=BankCardHolder("1002")
# cardDT3=Bank("xxx","123456",100);card3=BankCardHolder("1003")
atm1=ATM()
atm1=ATM_client()
atm1.C_chaka(card1)
