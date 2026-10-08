import pygame
pygame.init()

screen = pygame.display.set_mode((800,600)) #to start a window of 800 pixels wide and 600 pixels tall

YELLOW = (255,255,0) #for color black =(0,0,0),white = (255,255,255),red = (255,0,0)
clock = pygame.time.Clock()

running = True 
while running:
    pygame.draw.circle(screen,YELLOW,(400,300),30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.draw.circle(screen,YELLOW,(400,300),30)
    pygame.display.flip()
pygame.quit()
