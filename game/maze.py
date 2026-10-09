import pygame

TILE_SIZE = 32
MAZE_COLS = 18
MAZE_ROWS = 18

def load_maze(image_path):#load and scale the maze 1 image
    maze_image = pygame.image.load(image_path).convert()
    maze_image = pygame.transform.scale(maze_image,(MAZE_COLS * TILE_SIZE, MAZE_ROWS * TILE_SIZE))
    return maze_image


def find_walkable_tiles(maze_image):#return grid positions which are paths rather tha walls
    walkable_tiles = []
    for row in range(MAZE_ROWS):
        for col in range(MAZE_COLS):
            pixel_x = col * TILE_SIZE + TILE_SIZE // 2
            pixel_y = row * TILE_SIZE + TILE_SIZE // 2
            color = maze_image.get_at((pixel_x, pixel_y))

            if color.r < 40 and color.g < 40 and color.b < 40:
                walkable_tiles.append((col, row))

    return walkable_tiles


def can_move_to(x,y,walkable_tiles,maze_x = 112, maze_y = 0):#check whether destination tile is a path
    tile_col = (x+16-maze_x) // TILE_SIZE
    tile_row = (y+16-maze_y) //TILE_SIZE

    return(tile_col,tile_row) in walkable_tiles





