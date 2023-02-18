with open('邀请函.txt', 'a+', encoding='UTF-8') as fp:
    fp.write("诚挚邀请您来参加本次晚会")
    fp.write("\nbest wishes\n")
    fp.write("lucy\n")
    fp.seek(0)
    print(fp.read())
