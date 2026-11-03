import pygame
import time


def main():
    pygame.init()
    Icon=pygame.image.load("Sprite-0001.png")
    pygame.display.set_icon(Icon)
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Jeu de la vie")
    nbIteration = 100
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, (20,20,20), pygame.mouse.get_pos(), (14.5,14.5))
    
        screen.fill("black")
        for i in range(WIDTH//6):
            for j in range(HEIGHT//8):
                pygame.draw.rect(screen, (20,20,20), ((i*15,j*15), (14.5,14.5)))
        pygame.display.flip()
    pygame.quit()
    
main()

    