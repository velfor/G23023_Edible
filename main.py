import pygame
import sys
from settings import *
from player import Player
from obs import Obstacle

# создание объектов и групп
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()
#группы
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group()

#объекты
player = Player(PLAYER_X, PLAYER_Y,"player.png")
all_sprites.add(player)

for i in range(5):
    obs = Obstacle("ham.png", True)
    all_sprites.add(obs)
    items.add(obs)

for i in range(2):
    obs = Obstacle("paper.png", False)
    all_sprites.add(obs)
    items.add(obs)

# переменные
score = 0

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
    all_sprites.update()
 
    #пересечение объектов, collisions
    hits = pygame.sprite.spritecollide(player, items, True)
    for hit in hits:
        if hit.get_edible() == True:
            score += 10
            obs = Obstacle("ham.png", True)
            all_sprites.add(obs)
            items.add(obs)
            
    # обновление экрана
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()



    
