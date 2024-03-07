import pygame
import sys
from settings import *
from player import Player
from obs import Obstacle

# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()
player = Player(PLAYER_X, PLAYER_Y,"player.png")

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    player.update()
 
    #пересечение объектов, collisions
                
    # обновление экрана
    screen.fill(BLACK)
    player.draw(screen)
    pygame.display.update()



    
