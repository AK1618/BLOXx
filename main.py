import pygame, sys
from pygame.locals import QUIT
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
figure=figures[3]
def check_borders():
  if figure[i].x<0 or  figure[i].y>W-1:
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
      
    [pygame.draw.rect(dis,(40,40,40),i_rect,1) for i_rect in grid]
    for i in range(4):
      figure_rect.x=figure[i].x*tile
      figure_rect.y=figure[i].y*tile
      pygame.draw.rect(dis,pygame.Color('White'),figure_rect)
    pygame.display.flip()
    clock.tick(fps)