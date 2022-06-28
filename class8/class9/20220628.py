import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((200, 300))
width, height = screen.get_size()

background = pygame.Surface((width, height))
background.fill((255, 255, 255))
pygame.display.set_caption("my game")
sw = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sw = not (sw)

    if sw:
        screen.blit(background, (0, 0))
        pygame.draw.circle(background, (255, 0, 0), (130, 100), 30, 0)
        pygame.draw.circle(background, (255, 0, 0), (50, 100), 30, 0)
        pygame.draw.rect(background, (255, 0, 0), [120, 130, 60, 40])
        pygame.draw.ellipse(background, (255, 0, 0), [65, 150, 60, 40])
        pygame.draw.line(background, (255, 0, 0), (30, 30), (60, 60), 6)
        pygame.draw.polygon(background, (100, 100, 45),
                            [[100, 100], [50, 50], [0, 0]], 0)
        pygame.draw.arc(background, (255, 10, 0), [100, 100, 100, 50],
                        math.radians(180), math.radians(0), 2)
        # screen=pygame.display.set_mode((200,300))
        # width,height=screen.get_size()
    else:
        background.fill((255, 255, 255))
        screen.blit(background, (0, 0))

    pygame.display.update()