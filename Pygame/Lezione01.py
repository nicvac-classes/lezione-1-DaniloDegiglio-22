import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("Test Pygame")
clock = pygame.time.Clock()

x = 320
y = 240
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    screen.fill((35, 35 , 50))
    pygame.draw.circle(screen,(255,100,100),(x,y), 30)
    clock.tick(60)
    
    pygame.display.flip()