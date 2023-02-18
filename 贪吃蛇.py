import pygame, sys, random
from pygame.locals import *

redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)


def gameOver():
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()  # 获取帧率刷新控制对象

    playSurface = pygame.display.set_mode((640, 560))  # 创建游戏界面的大小
    pygame.display.set_caption('贪吃蛇')  # 创建游戏标题

    snakePosition = [100, 100]  # 蛇的位置
    snakeBody = [[100, 100], [80, 100], [60, 100]]  # 蛇身的位置
    targetPosition = [300, 300]  # 食物的位置
    targetflag = 1
    direction = 'right'  # 初始方向
    changeDirection = direction

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # 如果鼠标点击 X，退出当前程序
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:  # 键盘按下监听
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # 3.7 根据方向移动蛇头的坐标
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        # 蛇身增长
        snakeBody.insert(0, list(snakePosition))

        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetflag = 0
        else:
            snakeBody.pop()

        if targetflag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            targetPosition = [int(x * 20), int(y * 20)]
            targetflag = 1

        playSurface.fill(blackColour)
        for position in snakeBody:  # rect(Surface, color, Rect, width=0)
            pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))  # 画蛇
            pygame.draw.rect(playSurface, redColour, Rect(targetPosition[0], targetPosition[1], 20, 20))  # 画目标方块

        pygame.display.flip()

        if snakePosition[0] > 900 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 900 or snakePosition[1] < 0:
            gameOver()

        fpsClock.tick(5)


if __name__ == "__main__":
    main()
