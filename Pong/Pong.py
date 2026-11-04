import pygame
import random as r

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    Icon=pygame.image.load("Sprite.png")
    pygame.display.set_icon(Icon)
    rect_sizex, rect_sizey = 10, 100
    ball_size = 8
    xFac, yFac = 1, 1    
    time=0
    speedx, speedy = r.uniform(0.01, 0.04), r.uniform(0.01, 0.04)
    rect_pos1 = pygame.Vector2((screen.get_width()-rect_sizex-20),(screen.get_height()-rect_sizey)//2+80)
    rect_pos2 = pygame.Vector2((20),(screen.get_height()-rect_sizey)//2+80)
    pile_ou_face= r.randint(0,1)
    if pile_ou_face== 0:
        ball_pos = pygame.Vector2((screen.get_width()-ball_size)//2,(screen.get_height()-ball_size)//2+40)
    else:
        ball_pos = pygame.Vector2((screen.get_width()-ball_size)//2,(screen.get_height()-ball_size)//2-50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill("black")
        Ball = pygame.draw.circle(screen, "white", (ball_pos.x, ball_pos.y), 10)
        Striker1 = pygame.Rect(rect_pos1.x, rect_pos1.y, rect_sizex, rect_sizey)
        Striker2 = pygame.Rect(rect_pos2.x, rect_pos2.y, rect_sizex, rect_sizey)
        pygame.draw.rect(screen, "white", Striker1)
        pygame.draw.rect(screen, "white", Striker2)
        time += 0.0000002
        
        if ball_pos.x-ball_size <= 0  or ball_pos.x+ball_size >= WIDTH:
            xFac *= -1
            speedx = r.uniform(0.01+time,0.04+time)
        ball_pos.x-= xFac*speedx
        if ball_pos.y-ball_size <= 0 or ball_pos.y+ball_size >= HEIGHT:
            yFac *= -1
            speedy = r.uniform(0.01+time,0.04+time)
        ball_pos.y-= yFac*speedy
        if pygame.Rect.colliderect(Striker1, Ball):
            xFac = 1
        if pygame.Rect.colliderect(Striker2, Ball):
            xFac = 1
        keys = pygame.key.get_pressed()
        if rect_pos1.y <= 0:
            rect_pos1.y = 0
        elif rect_pos1.y+rect_sizey >= HEIGHT:
            rect_pos1.y = HEIGHT-rect_sizey
        if keys[pygame.K_a]:
            rect_pos1.y-=0.1
        if keys[pygame.K_d]:
            rect_pos1.y+=0.1

        if rect_pos2.y <= 0:
            rect_pos2.y = 0
        elif rect_pos2.y+rect_sizey >= HEIGHT:
            rect_pos2.y = HEIGHT-rect_sizey
        if keys[pygame.K_LEFT]:
            rect_pos2.y-=0.1
        if keys[pygame.K_RIGHT]:
            rect_pos2.y+=0.1
                
        pygame.display.flip()
    pygame.quit()

main()

    

