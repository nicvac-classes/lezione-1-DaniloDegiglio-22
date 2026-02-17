
import pygame
import sys
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Pymunk - Fisica")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)
draw_options = pymunk.pygame_util.DrawOptions(screen)

floor = pymunk.Segment(space.static_body,)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((30, 30, 50))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()