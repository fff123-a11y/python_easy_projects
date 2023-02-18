import re


def main(mail_addr):
    ret = re.match(r".{4,20}\@163\.com", mail_addr)

    ret = re.match(r"[a-zA-Z0-9]{4, 20}@163\.com", mail_addr)
    print(mail_addr)


if __name__ == '__main__':
    mail_addr = input("请输入一个邮箱地址：")
    main(mail_addr)

n = 1
day = 11
while day > 1:
    n = (n + 1) * 2
    day -= 1
    print(day, n)

list = [9, 10, 23, 45, 17, 24, 56, 89, 67]
max_data = list[0]
for i in list:
    if i > list[0]:
        max_data = i
print(max_data)
