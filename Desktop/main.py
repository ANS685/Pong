import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((0, SCREEN_HEIGHT/2, 5, 100))
player2 = pygame.Rect((1195, SCREEN_HEIGHT/2, 5, 100))
ball = pygame.Rect((387.5, 250, 25, 25))
velo = 1
P1 = 0
P2 = 0
veloy = 1

run = True
while run:

    game_font = pygame.font.SysFont("freesansbold.tff", 64)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), player2)
    pygame.draw.rect(screen, (255, 255, 255), ball)

    score1 = game_font.render(f"{P1}", False, (255, 255, 255))
    screen.blit(score1, (500, 850))

    score2 = game_font.render(f"{P2}", False, (255, 255, 255))
    screen.blit(score2, (700, 850))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)
    elif key[pygame.K_UP]:
        player2.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player2.move_ip(0, 1)

    ball.x += velo
    ball.y += veloy

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        veloy *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        velo *= -1

    if ball.colliderect(player) or ball.colliderect(player2):
        velo *= -1

    def ball_reset():
        global velo
        global veloy
        ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        velo = random.choice((1, -1))
        veloy = random.choice((1, -1))
        time.sleep(3)

    if ball.x >= 1175:
        P1 = P1 + 1
        if P1 == 11:
            break
        else:
            ball_reset()

    if ball.x <= 0:
        P2 = P2 + 1
        if P2 == 11:
            break
        else:
            ball_reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
