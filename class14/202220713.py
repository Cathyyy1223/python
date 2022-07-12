#===載入套件開始===
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
import random

#***載入套件結束***

#===初始化設定開始===
BLACK = (0, 0, 0)
WHITE = (255, 0, 0)
RED = (255, 0, 0)
pygame.init()
clock = pygame.time.Clock()
act = False
#***初始化設定結束***

#===遊戲視窗設定開始===
bg_x = 800
bg_y = 600
bg_size = (bg_x, bg_y)
#***遊戲視窗設定結束***
pygame.display.set_caption(u"打磚塊遊戲")
screen = pygame.display.set_mode(bg_size)
#===磚塊設定開始===
#===磚塊設定結束===

#===顯示磚塊數量設定開始===
#===顯示磚塊數量設定結束===

#===碰撞設定開始===
#===碰撞設結束===

#===初始遊戲設定開始===
#===初始遊戲設定結束===

#===底板設定開始===
#===底板設定結束===

#===球設定開始===
ball_x = 400
ball_y = 300
ball_radius = 8
ball_diameter = ball_radius * 2
ball_color = WHITE
dx = 8
dy = -8


def ball_update(win):
    global ball_x, ball_y
    global dx, dy

    ball_x += dx
    ball_y += dy

    if (ball_x > bg_x - ball_diameter or ball_x < ball_diameter):
        dx = -dx
    if (ball_y > bg_y - ball_diameter or ball_y < ball_diameter):
        dy = -dy

    pygame.draw.circle(win, ball_color, [ball_x, ball_y], ball_radius)


#===球設定結束===

#===初始遊戲設定開始===
#===初始遊戲設定結束===

#-------------------------------------------------------------------------
# 主迴圈.
#-------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    ball_update(screen)

    pygame.display.update()
    clock.tick(60)