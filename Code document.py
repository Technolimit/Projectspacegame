import pygame
from pygame.locals import *
import time
pygame.init()
screen = pygame.display.set_mode((640, 480))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (135, 206, 250)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 40)
score = 0
running = True

      

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
           running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            screen.blit(og_planet, (288, 208))
            score = int(score)
            score += 1
            score = str(score)
            score_txt = font.render(score, True, LIGHT_BLUE)
            screen.blit(score_txt, (20, 20))
        score=int(score)
        if score>=15:
            score=str(score)
            txt='water unlocked'
            water_unlocked=True
            screentxt= font.render(txt, True, BLUE)
            screen.blit(screentxt, (400,20))
        pygame.display.update()