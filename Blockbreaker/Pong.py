import pygame
import random as r

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    rect_sizex, rect_sizey = 10, 100
    ball_size = 8
    xFac, yFac = 1, 1    
    time=0
    speedx, speedy = r.uniform(0.01, 0.04), r.uniform(0.01, 0.04)
    rect_pos = pygame.Vector2((screen.get_width()-rect_sizex)//2,(screen.get_height()-rect_sizey)//2+80)
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
        Ball = pygame.draw.circle(screen, "red", (ball_pos.x, ball_pos.y), 10)
        Striker = pygame.Rect(rect_pos.x,rect_pos.y, rect_sizex, rect_sizey)
        pygame.draw.rect(screen, "white", Striker)
        time += 0.0000002
        
        if ball_pos.x-ball_size <= 0  or ball_pos.x+ball_size >= WIDTH:
            xFac *= -1
            speedx = r.uniform(0.01+time,0.04+time)
        ball_pos.x-= xFac*speedx
        if ball_pos.y-ball_size <= 0:
            yFac *= -1
            speedy = r.uniform(0.01+time,0.04+time)
        ball_pos.y-= yFac*speedy
        if pygame.Rect.colliderect(Striker, Ball):
            yFac = 1
        if ball_pos.y >= HEIGHT:
            break
        keys = pygame.key.get_pressed()
        if rect_pos.x <= 0:
            rect_pos.x = 0
        elif rect_pos.x+rect_sizex >= WIDTH:
            rect_pos.x = WIDTH-rect_sizex
        if keys[pygame.K_a]:
            rect_pos.x-=0.1
        if keys[pygame.K_d]:
            rect_pos.x+=0.1
                
        pygame.display.flip()
    pygame.quit()

main()

    

