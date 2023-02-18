num = 1
while num <= 100:
    print(num)
    num = num + 1

sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum)

num = 1
while num <= 100:
    if num % 2 == 1:
        print(num)
    num = num + 1

j = 1
while j < 6:
    i = 1
    while i < 11:
        print("*", end="")
        i += 1
    print()
    j += 1

str1 = "hello world"
# 下标   012345678910，引号不算下标
print(str1[1])
print(str1[2:5])
print(str1[2:5:2])  # lo 此处的l是第一个l,一次走两步
print(str1[2:10:3])
print(str1[10:2:-1])  # dlrow ol

for i in range(1, 10):
    for j in range(1, 10):
        print('{}*{}={}\t'.format(i, j, i * j))
    print()
