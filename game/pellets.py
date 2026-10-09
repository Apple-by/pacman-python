import pygame 

PELLET_COLOR = (255,255,0)#yellow
PELLET_RADIUS = 3

def create_pellets(walkable_tiles): #create pelst on walkable tiles
    return set(walkable_tiles)

def draw_pellets(screen,pellets,tile_size,maze_x,maze_y): #draw each pellet at the corner of its tile
    for col,row in pellets:
        pellet_x = maze_x + col * tile_size + tile_size // 2
        pellet_y = maze_y + row * tile_size + tile_size // 2

        pygame.draw.circle(screen, PELLET_COLOR,(pellet_x,pellet_y),PELLET_RADIUS)


