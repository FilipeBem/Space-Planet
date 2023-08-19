import pygame
from pygame.locals import *
import random

pygame.init()

x = 1200
y = 720

screen = pygame.display.set_mode((x,y),pygame.RESIZABLE)
pygame.display.set_caption('Space Planet')

cenario = pygame.image.load('img/cenario.jpg').convert_alpha()
cenario = pygame.transform.scale(cenario, (x,y))

alien = pygame.image.load('img/UFO.png')
alien = pygame.transform.scale(alien, (100,100))

alien2 = pygame.image.load('img/alien2.png')
alien2 = pygame.transform.scale(alien2, (100,100))

alien3 = pygame.image.load('img/alien 3.png')
alien3 = pygame.transform.scale(alien3, (100,100))

playerImg = pygame.image.load('img/Navepy.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (80,80))
playerImg = pygame.transform.rotate(playerImg,-90)

missel = pygame.image.load('img/bala.png').convert_alpha()
missel = pygame.transform.scale(missel, (30,30))


pos_alien_x= 500
pos_alien_y = 360

pos_alien2_x= 700
pos_alien2_y = 360

pos_alien3_x= 300
pos_alien3_y = 360

pos_player_x = 200
pos_player_y = 300

vel_x_missel = 0
pos_missel_x = 200
pos_missel_y = 327

atirar = False

pontos = 5

font = pygame.font.SysFont('fonts/PixelGameFont.ttf', 50)

def respawn():
    x = 1350
    y = random.randint(20,620)
    return [x,y]

def respawn2():
    x = 1350
    y = random.randint(120,420)
    return [x,y]

def respawn3():
    x = 1350
    y = random.randint(220,520)
    return [x,y]

def respawn_missel():
    atirar = False
    pos_missel_x = pos_player_x
    pos_missel_y =  pos_player_y + 27
    vel_x_missel = 0
    return [pos_missel_x, pos_missel_y, atirar, vel_x_missel]

def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 70:
         pontos -= 1/2
         return True
    elif missel_rect.colliderect(alien_rect):
          pontos += 1/2
          return True
    else:
          return False
def colisions2():
    global pontos
    if player_rect.colliderect(alien2_rect) or alien2_rect.x == 70:
         pontos -= 1/2
         return True
    elif missel_rect.colliderect(alien2_rect):
          pontos += 1/2
          return True
    else:
          return False
def colisions3():
    global pontos
    if player_rect.colliderect(alien3_rect) or alien3_rect.x == 70:
         pontos -= 1/2
         return True
    elif missel_rect.colliderect(alien3_rect):
          pontos += 1/2
          return True
    else:
          return False

rodando = True

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
alien2_rect = alien2.get_rect()
alien3_rect = alien3.get_rect()
missel_rect = missel.get_rect()


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
             
            
    screen.blit(cenario, (0,0))

    real_x = x % cenario.get_rect().width
    screen.blit(cenario, (real_x - cenario.get_rect().width,0))
    if real_x < 1200:
        screen.blit(cenario, (real_x, 0))

        

        if pos_alien_x == 50 or colisions():
            pos_alien_x = respawn()[0]
            pos_alien_y = respawn()[1]

        if pos_alien2_x == 50 or colisions2():
            pos_alien2_x = respawn()[0]
            pos_alien2_y = respawn()[1]

        if pos_alien3_x == 50 or colisions3():
            pos_alien3_x = respawn()[0]
            pos_alien3_y = respawn()[1]


        if pos_missel_x == 1360 or colisions() or colisions2() or colisions3() :
            pos_missel_x, pos_missel_y, atirar, vel_x_missel = respawn_missel()

        
        player_rect.x = pos_player_x
        player_rect.y = pos_player_y

        alien_rect.x = pos_alien_x
        alien_rect.y = pos_alien_y

        alien2_rect.x = pos_alien2_x
        alien2_rect.y = pos_alien2_y

        alien3_rect.x = pos_alien3_x
        alien3_rect.y = pos_alien3_y

        missel_rect.x = pos_missel_x
        missel_rect.y = pos_missel_y


        x -= 2
        pos_alien_x -= 1 
        pos_alien2_x -= 1
        pos_alien3_x -= 1
        pos_missel_x += vel_x_missel

        move = pygame.key.get_pressed()
        if move[pygame.K_UP] and pos_player_y > 1:
            pos_player_y -= 1
            if not atirar:
              pos_missel_y -= 1
        if move[pygame.K_DOWN] and pos_player_y < 665:
            pos_player_y += 1
            if not atirar:
              pos_missel_y += 1
        
        if move[pygame.K_SPACE]:
            atirar = True
            vel_x_missel = 2
        
        if pontos == -1:
           rodando = False
       
        #pygame.draw.rect(screen, (255,0,0), player_rect, 4)
        #pygame.draw.rect(screen, (255,0,0), alien_rect, 4)
        #pygame.draw.rect(screen, (255,0,0), missel_rect, 4)
 
        score = font.render(f' Pontos: {int(pontos)} ', True, (0,0,0))
        screen.blit(score, (10,50))

        screen.blit(alien,(pos_alien_x, pos_alien_y))
        screen.blit(alien2,(pos_alien2_x, pos_alien2_y))
        screen.blit(alien3,(pos_alien3_x, pos_alien3_y))
        screen.blit(missel,(pos_missel_x, pos_missel_y))
        screen.blit(playerImg,(pos_player_x, pos_player_y))

        print(pontos)

    pygame.display.update()

