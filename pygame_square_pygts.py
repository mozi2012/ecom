import pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Line")
RED = (255, 0, 0)
BLACK = (0, 0, 0)
x_start, y_start = -100, 250  
x_end, y_end = 150, 250 
player_x, player_y = 200, 200
speed = 5
running = True
while running:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_s]:
        player_y += speed
    pygame.draw.rect(screen, RED, (player_x, player_y, 50, 50))
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()
