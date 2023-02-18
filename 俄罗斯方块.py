import pygame, sys, random
# 初始坐标，确定行数和列数
block_initial_position, score, times, gameover, press, all_block, background = [20, 5], [0], 0, [], False, [
    [[0, 0], [0, -1], [0, 1], [0, 2]], [[0, 0], [0, 1], [-1, 1], [-1, 0]], [[0, 0], [0, -1], [-1, 0], [-1, 1]],
    [[0, 0], [0, 1], [-1, -1], [-1, 0]], [[0, 0], [0, 1], [1, 0], [0, -1]], [[0, 0], [1, 0], [-1, 0], [1, -1]],
    [[0, 0], [1, 0], [-1, 0], [1, 1]]], [[0 for column in range(0, 10)] for row in range(0, 22)]
background[0], select_block = [1 for column in range(0, 10)], list(random.choice(all_block))

# 移动函数处理
def move(n):
    # 设置一个初始值
    if n == 100:
        for row, column in select_block:
            pygame.draw.rect(screen, (255, 165, 0), (
                (column + block_initial_position[1]) * 40, 800 - (row + block_initial_position[0]) * 40, 38, 38))
        for row in range(0, 20):
            for column in range(0, 10):
                if background[row][column]: pygame.draw.rect(screen, (0, 0, 255), (column * 40, 800 - row * 40, 38, 38))
    y_drop, x_move = block_initial_position
    if n == 1 or n == -1:
        x_move += n
        for row, column in select_block:
            if (column + x_move) < 0 or (column + x_move) > 9 or background[column + y_drop][column + x_move]: break
        else:
            block_initial_position.clear(), block_initial_position.extend([y_drop, x_move])
    if n == 0:
        rotating_position = [(-column, row) for row, column in select_block]
        for row, column in rotating_position:
            if (column + x_move) < 0 or (column + x_move) > 9 or background[row + y_drop][row + x_move]: break
        else:
            select_block.clear(), select_block.extend(rotating_position)
    if n == 10:
        # 掉下的方块坐标-1
        y_drop -= 1
        for row, column in select_block:
            if background[row + y_drop][column + x_move] == 1: break
        else:
            block_initial_position.clear()
            block_initial_position.extend([y_drop, x_move])
            return
        for row, column in select_block: background[block_initial_position[0] + row][
            block_initial_position[1] + column] = 1
        complete_row = []
        for row in range(1, 20):
            if 0 not in background[row]: complete_row.append(x_move)
        complete_row.sort(reverse=True)
        for row in complete_row:
            background.pop(row)
            # 列表推导式
            background.append([0 for column in range(0, 10)])
        score[0] += len(complete_row)
        pygame.display.set_caption('俄罗斯方块[你的分数：' + str(score[0] * 100) + '分]')
        select_block.clear(), select_block.extend(list(random.choice(all_block)))
        block_initial_position.clear(), block_initial_position.extend([19, 4])
        for row, column in select_block:
            if background[row + block_initial_position[0]][column + block_initial_position[1]]: gameover.append(1)

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((400, 800))  # set_mode((400,800)) 修改数值可以修改窗口大小 但第7行和第10行要做相应的改动
while True:
    # 设置颜色
    screen.fill((255, 255, 255))
    # 按键处理
    for event in pygame.event.get():
        # 暂停游戏的处理
        if event.type == pygame.QUIT:
            sys.exit()
        # 方向键的处理 左下
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move(-1)
        # 右下
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move(1)
        # 上下
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            press = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            press = False
    if press: times += 10
    if times >= 50:
        # 移动10个单位长度
        move(10)
        times = 0
    else:
        # 时间处理
        times += 1
    # 游戏结束
    if gameover: sys.exit()
    move(100)
    pygame.time.Clock().tick(200)  # tick(200)修改数字可以修改游戏的整体速率
    pygame.display.flip()
