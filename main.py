import pygame
from game.maze import load_maze, find_walkable_tiles, can_move_to
from game.pellets import create_pellets, draw_pellets

pygame.init()

screen = pygame.display.set_mode((800,600)) #to start a window of 800 pixels wide and 600 pixels tall
open_pacman = pygame.image.load("assets/open_pacman.png").convert_alpha()
close_pacman = pygame.image.load("assets/close_pacman.png").convert_alpha()
maze_image = load_maze("assets/maze1.png")
walkable_tiles = find_walkable_tiles(maze_image)
pellets = create_pellets(walkable_tiles)

BLACK = (0,0,0)
clock = pygame.time.Clock()

pacman_x = 228
pacman_y = 392
pacman_speed = 3
pacman_image = open_pacman
last_switch = 0
animation_delay = 150

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if can_move_to(pacman_x - pacman_speed,pacman_y,walkable_tiles):
            pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        if can_move_to(pacman_x + pacman_speed,pacman_y,walkable_tiles):
            pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        if can_move_to(pacman_x,pacman_y - pacman_speed,walkable_tiles):
            pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        if can_move_to(pacman_x,pacman_y + pacman_speed,walkable_tiles):
            pacman_y += pacman_speed
    
    pacman_x = max(0,min(pacman_x,800-32))
    pacman_y = max(0,min(pacman_y,600-32))
    
    screen.fill(BLACK)
    screen.blit(maze_image, (112,0))
    draw_pellets(screen, pellets, 32, 112, 0)
    current_time = pygame.time.get_ticks()
    if current_time - last_switch >= animation_delay:
        if pacman_image == open_pacman:
            pacman_image = close_pacman 
        else:
            pacman_image = open_pacman
        last_switch = current_time
    screen.blit(pacman_image, (pacman_x,pacman_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
