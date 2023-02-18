# # # 矩阵计算器
from tkinter import *

m1 = []
m2 = []


def main():
    n = DisplayMainwindowAndGetNumber()
    newwindow(n)
    mlist = calculate(n)
    displayTheAnswer(n, mlist)


def DisplayMainwindowAndGetNumber():
    def pp():
        window.destroy()

    window = Tk()
    window.title('Matrix Calculation')
    ntext = StringVar()
    lb = Label(window, text='Enter the n:')
    lb.grid(row=0, column=0, padx=5, pady=5)
    ent = Entry(window, width=15, textvariable=ntext)
    ent.grid(row=0, column=1, padx=5, pady=5)
    bnt = Button(window, text='Enter', command=pp)
    bnt.grid(row=1, column=0, columnspan=2, pady=10)
    window.mainloop()
    return eval(ntext.get())


def newwindow(n):
    newwindow = Tk()
    newwindow.title('Enter Process')

    def pp():
        newwindow.destroy()

    global m1
    global m2
    # 获取输入控件来表示矩阵1
    for i in range(n):
        line = []
        for j in range(n):
            temporarytext1 = StringVar()
            ent = Entry(newwindow, width=3, textvariable=temporarytext1)
            ent.grid(row=i, column=j, padx=5, pady=5)
            line.append(temporarytext1)
        m1.append(line)
    # 在两个矩阵中间显示‘乘以’
    lb = Label(newwindow, text='乘以')
    lb.grid(row=n // 2, column=n, padx=10)
    # 获取输入控件来表示矩阵2
    for i in range(n):
        line = []
        for j in range(n):
            temporarytext2 = StringVar()
            ent = Entry(newwindow, width=3, textvariable=temporarytext2)
            ent.grid(row=i, column=1 + n + j, padx=5, pady=5)
            line.append(temporarytext2)
        m2.append(line)
    btn = Button(newwindow, text='calculate', command=pp)
    btn.grid(row=n, column=n, padx=10)
    newwindow.mainloop()


def calculate(n):
    global m1
    global m2
    mm1 = [[int(j.get()) for j in i] for i in m1]
    mm2 = [[int(j.get()) for j in i] for i in m2]
    newmatrix = []
    for i in range(n):
        newline = []
        for j in range(n):
            thesum = 0
            for k in range(n):
                thesum += mm1[i][k] * mm2[k][j]
            newline.append(thesum)
        newmatrix.append(newline)
    return newmatrix


def displayTheAnswer(n, mlist):
    nnwindow = Tk()
    nnwindow.title('Answer')
    for i in range(n):
        for j in range(n):
            temtext = StringVar()
            ent = Entry(nnwindow, width=3, textvariable=temtext, state='readonly')
            ent.grid(row=i, column=j, padx=5, pady=5)
            temtext.set(mlist[i][j])
    nnwindow.mainloop()


main()
