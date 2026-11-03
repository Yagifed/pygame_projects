import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True
last_key = ''
dt = 0
sprite_img = pygame.image.load('sprites.png').convert_alpha()
map = pygame.image.load('hoenn_map.jpg')
frame = 0
i = 0
width = 48
direction = 0
frame_rect = pygame.Rect(frame * width, direction, 48, 48)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
map_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.4, 0.4)
        self.vy = random.uniform(2, 1)
        self.lifespan = 255  # Alpha-based lifespan
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifespan -= 4
        
class Emitter:
    def __init__(self, x, y):
        self.particles = []
        self.x = x
        self.y = y
    
    def emit(self):
        self.particles.append(Particle(self.x, self.y))
    
    def update(self):
        for p in self.particles.copy():
            p.update()
            if p.lifespan <= 0:
                self.particles.remove(p)
                
def draw_particles(surface, emitter):
    for p in emitter.particles:
        radius = int(p.lifespan / 50)
        color = (255, 100, 0, p.lifespan)
        pygame.draw.circle(surface, color, (int(p.x), int(p.y)), radius)

player_running_emitter_s = Emitter(player_pos.x+5, player_pos.y+42)
player_running_emitter_w = Emitter(player_pos.x+25, player_pos.y+50)
player_running_emitter_a = Emitter(player_pos.x+5, player_pos.y+42)
player_running_emitter_d = Emitter(player_pos.x+5, player_pos.y+42)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    screen.blit(map, map_pos)
    dt = clock.tick(60)
    def anim_run():
        global i
        global frame
        i = (i+1) % 8
        if i == 1: frame = (frame + 1) % 4
    def anim_sprint():
        global i
        global frame
        i = (i+1) % 5
        if i == 1: frame = (frame + 1) % 4
    def idle():
        global frame
        frame = 0
    frame_rect = pygame.Rect(frame * width, direction, 48, 48)
    screen.blit(sprite_img, player_pos, area=frame_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if keys[pygame.K_LSHIFT]:
            map_pos.y += 4 * 0.8
            anim_sprint()
            player_running_emitter_w.emit()
            player_running_emitter_w.update()
            draw_particles(screen, player_running_emitter_w)
        else:
            map_pos.y += 2 * 0.8
            anim_run()
        direction = 144
    if keys[pygame.K_s]:
        if keys[pygame.K_LSHIFT]:
            map_pos.y -= 4 * 0.8
            anim_sprint()
            player_running_emitter_s.emit()
            player_running_emitter_s.update()
            draw_particles(screen, player_running_emitter_s)
        else:
            map_pos.y -= 2 * 0.8
            anim_run()
        direction = 0
    if keys[pygame.K_a]:
        if keys[pygame.K_LSHIFT]:
            map_pos.x += 4 * 0.8
            anim_sprint()
            player_running_emitter_a.emit()
            player_running_emitter_a.update()
            draw_particles(screen, player_running_emitter_a)
        else:
            map_pos.x += 2 * 0.8
            anim_run()
        direction = 48  
    if keys[pygame.K_d]:
        if keys[pygame.K_LSHIFT]:
            map_pos.x -= 4 * 0.8
            anim_sprint()
            player_running_emitter_d.emit()
            player_running_emitter_d.update()
            draw_particles(screen, player_running_emitter_d)
        else:
            map_pos.x -= 2 * 0.8
            anim_run()
        direction = 96
    # flip() the display to put your work on screen
    pygame.display.flip()
pygame.quit()


