"""
设计一个密码登录程序，用户名为Elyse, 密码为123456
当输入的用户名和密码都正确时，输出“Elyse, 欢迎您!"
当输入的用户名不正确时，输出”用户名错误，请重新输入！”
当输入的密码不正确时，输出”密码错误，请重新输入！”
当输入的账号或密码均不正确，输出“用户名或密码错误，请重新输入！”
（用户只有三次登录机会，登录成功程序结束，失败三次程序也结束，并且提示您的账号已锁定）
"""
for i in range(1, 4):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == 'Elyse' and password == 123456:
        print("Elyse, 欢迎您！")
        break
    elif username != 'Elyse':
        print("用户名错误，请重新输入！")
    elif password != 123456:
        print("密码错误，请重新输入！")
    elif username != 'Elyse' and password != 123456:
        print("用户名或密码错误，请重新输入！")
else:
    print("您的账号已锁定!")
