import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

countdown = 10
font = pygame.font.Font("freesansbold.ttf", 32)

while countdown > 0:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    cd = font.render(str(countdown), True, (255,255,255))
    screen.blit(cd, (85,85))
    countdown -= 1
    
    pygame.display.update()
    pygame.time.delay(1000)