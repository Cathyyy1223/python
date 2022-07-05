import pygame
import sys
import random
import os

os.chdir(sys.path[0])
######初始化######
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
######初始化######

bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
screen = pygame.display.set_mode([bg_x, bg_y])  # 設定窗口
pygame.display.set_caption("打地鼠")
######新增視窗######

######背景繪製######
sur = pygame.Surface([bg_x, bg_y])  # 繪製背景容器


def screen_update(win):
    win.blit(sur, (0, 0))


######背景繪製######

######地鼠繪製######
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450],
        [610, 450]]  # 六個位置
tick = 0  # 計數器
max_tick = 20
pos = pos6[0]  # 外面記錄圓的位置
gophers = pygame.image.load('Gophers150.png')


def gophers_update(win):
    global tick, pos, score
    # 每幀循環執行的代碼
    if tick > max_tick:  # 每20次刷新變換一次
        new_pos = random.randint(0, 5)  # 隨機0到5
        pos = pos6[new_pos]  # 更新外部記錄的圓的位置
        tick = 0  # 重置計數器
    else:  # 不刷新變換的時候
        tick += 1  # 增加計數器
    pygame.draw.circle(sur, BLUE, pos, 50)  # 使用隨機位置
    win.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))


######地鼠繪製######

######分數顯示######
score = 0  #分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)


def score_update(win):
    score_sur = score_font.render(str(score), False, RED)  # ！！生成計數表面
    win.blit(score_sur, (10, 10))  # ！！增加分數表面


######分數顯示######


def check_click(pos, x_start, y_start, x_end, y_end):
    x_match = pos[0] > x_start and pos[0] < x_end
    y_match = pos[1] > y_start and pos[1] < y_end
    if x_match and y_match:
        return True
    else:
        return False


######主程式######
while True:
    ######事件偵測######
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1

    ######事件偵測######

    sur.blit(bg, (0, 0))

    screen_update(screen)
    gophers_update(screen)
    score_update(screen)
    #####更新畫面#####
    clock.tick(30)
    pygame.display.update()
    #####更新畫面#####
