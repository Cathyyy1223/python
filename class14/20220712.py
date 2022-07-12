import pygame
import sys
import random
import os
import time

os.chdir(sys.path[0])

######初始化######
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
######初始化######

######新增視窗######
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
    win.blit(bg, (0, 0))


######背景繪製######

######地鼠繪製######
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450],
        [610, 450]]  # 六個位置
tick = 0  # 計數器
max_tick = 20
pos = pos6[0]  # 外面記錄圓的位置
gophers = pygame.image.load('Gophers150.png')  # 地鼠圖片
gophers2 = pygame.image.load('Gophers2_150.png')  # 地鼠圖片
hitsur = gophers


def gophers_update(win):
    global tick, pos, score, times
    # 每幀循環執行的代碼
    if tick > max_tick:  # 每20次刷新變換一次
        new_pos = random.randint(0, 5)  # 隨機0到5
        pos = pos6[new_pos]  # 更新外部記錄的圓的位置
        tick = 0  # 重置計數器
        times += 1
    else:  # 不刷新變換的時候
        tick += 1  # 增加計數器
    # pygame.draw.circle(sur, BLUE, pos, 50)  # 使用隨機位置
    win.blit(
        hitsur,
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


######偵測是否按下######
def check_click(pos, x_start, y_start, x_end, y_end):
    x_match = pos[0] > x_start and pos[0] < x_end
    y_match = pos[1] > y_start and pos[1] < y_end
    if x_match and y_match:
        return True
    else:
        return False


######偵測是否按下######

######滑鼠顯示設定######
pygame.mouse.set_visible(False)  # 隱藏滑鼠
mpos = (0, 0)
ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
hammer = ham2


def mouse_update(win):
    global mpos, hammer
    mpos = pygame.mouse.get_pos()  # 獲取鼠標位置

    # pygame.draw.circle(win, BLUE, mpos, 10)  # 在滑鼠位置畫紅色圓
    win.blit(hammer, mpos)


######滑鼠顯示設定######

######剩餘次數設定######
typeface = pygame.font.get_default_font()
end_font = pygame.font.Font(typeface, 36)
times = 0  # 地鼠跳出的次數
times_max = 5  #最多次數


def times_update(win):
    end_sur = end_font.render(str(times), True, RED)  #重新生成分數文字表面
    win.blit(end_sur, (bg_x - end_sur.get_width() - 10, 10))  # ！！增加分數表面


######剩餘次數設定######

######遊戲結束設定######
typeface = pygame.font.get_default_font()
end_font = pygame.font.Font(typeface, 36)


def game_over(win):
    win.fill((0, 0, 0))
    pygame.mouse.set_visible(True)
    end_sur = score_font.render("Your Score is:{}/{}".format(score, times_max),
                                False, RED)  # 生成計數表面
    win.blit(end_sur, (100, 100))  # 增加分數表面


######遊戲結束設定######
######主程式######
while True:
    ######事件偵測######
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # 如果是鼠標按下事件
            hammer = ham1
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                if times < times_max:
                    tick = max_tick + 1  # 立即變換位置
                    score += 1
                    hitsur = gophers2
    ######事件偵測######

    # sur.fill(BLACK)  # 用黑色覆蓋前一幀的畫面，實現刷新
    if times > times_max:
        game_over(screen)
    else:
        screen_update(screen)
        gophers_update(screen)
        mouse_update(screen)
        score_update(screen)
        times_update(screen)
    #####更新畫面#####
    clock.tick(30)
    pygame.display.update()
    if (hammer == ham1):
        time.sleep(0.1)
        hammer = ham2
        hitsur = gophers
    #####更新畫面#####
