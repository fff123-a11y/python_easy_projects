str1 = "hello world"
# 下标   012345678910，引号不算下标
print(str1[1])
print(str1[2:5])
print(str1[2:5:2])  # lo 此处的l是第一个l,一次走两步
print(str1[2:10:3])
print(str1[10:2:-1])  # dlrow ol
print(str1[10:2:-3])  # doo

"""


"""

id_number = input("请输入身份证号码:")
year = id_number[6:10]
month = id_number[11:12]
day = id_number[13:14]
print("%s年%s月%s日" % (year, month, day))

str = "今天是XX节"
print(str.replace("XX", "情人"))

str1 = input("请输入字符串：")
upper_letter = 0
lower_letter = 0
digit = 0
others = 0
i = 0
for i in str1:
    if i.isupper():
        upper_letter += 1
    elif i.islower():
        lower_letter += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
res = "大写字母有：%s个\n小写字母有：%s个\n数字有：%s个\n其它字符有：%s个" % (upper_letter, lower_letter, digit, others)
print(res)
