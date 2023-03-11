import pygame, sys
from pygame.locals import QUIT
from random import choice, randrange
from copy import deepcopy
fps = 60
W,H = 10,20
tile = 45
res=W*tile,H*tile
pygame.init()
dis = pygame.display.set_mode(res)
clock = pygame.time.Clock()
grid = [ pygame.Rect(x*tile,y*tile,tile,tile) for x in range (W) for y in range(H)]
figures_pos=[
            [(-1,0),(-2,0),(0,0),(1,0)],
            [(0,-1),(-1,-1),(-1,0),(0,0)],
            [(-1,0),(-1,1),(0,0),(0,-1)],
            [(0,0),(-1,0),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(1,-1)],
            [(0,0),(0,-1),(0,1),(-1,0)]
            ]
figures = [[pygame.Rect(x+W//2,y+1,1,1)for x,y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0,0,tile-2,tile-2)
field = [[0 for i in range(W)] for j in range(H)]
anim_count, anim_speed, anim_limit = 0, 60, 2000

fon = pygame.font.Font('font/font.ttf', 65)
mfont = pygame.font.Font('font/font.ttf', 45)
figure=deepcopy(choice(figures))

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))
def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True 


while True:
    dx =0
    dis.fill(pygame.Color('Black')) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                  dx=-1
            if event.key == pygame.K_RIGHT:
                  dx=+1
    figure_old = deepcopy(figure)          
    for i in range(4):
      figure[i].x == dx
      if not check_borders():
        figure = deepcopy(figure_old)
        break
     anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000
                break
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break
    line, lines = H - 1, 0
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1
        else:
            anim_speed += 3
            lines += 1  
    [pygame.draw.rect(dis,(40,40,40),i_rect,1) for i_rect in grid]
    for i in range(4):
      figure_rect.x=figure[i].x*tile
      figure_rect.y=figure[i].y*tile
      pygame.draw.rect(dis,pygame.Color('White'),figure_rect)
    pygame.display.flip()
    clock.tick(fps)
