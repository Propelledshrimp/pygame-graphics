#Computer Programming
#Graphics Mini Project
#Tatem Pearson

# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Winter"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)
RED = (255, 0, 0)
GREEN = (21, 109, 9)
BLUE = (0, 0, 255)
ORANGE = (255, 224, 50)
LIGHT_BLUE = (69,240,249)
GREY = (165, 165, 165)
BROWN = (95, 45, 21)  


def draw_cloud(x,y):
    pygame.draw.ellipse(screen, GREY, [x, y+20, 40, 40])
    pygame.draw.ellipse(screen, GREY, [x+60, y+20, 40, 40])
    pygame.draw.ellipse(screen, GREY, [x+20, y+10, 25,25])
    pygame.draw.ellipse(screen, GREY, [x+35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x+20, y+20, 60, 40])

def draw_tree(x,y):
    pygame.draw.rect(screen, BROWN, [x, y , 50, 75])
    pygame.draw.polygon(screen, GREEN, [[x+25, y-250], [x-50, y] , [x+100,y]]) 

    
"""make snow"""
snow = []
for i in range(250):
    x = random.randrange(0,800)
    y = random.randrange(30, 400)
    r = random.randrange(1,5)
    snow.append([x,y, r, r]) 

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    ''' sky '''
    screen.fill(LIGHT_BLUE)

    ''' snow '''
    for s in snow:
        pygame.draw.ellipse(screen, WHITE, s) 

    ''' ground '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]]
        pygame.draw.polygon(screen, BLACK, post)

    pygame.draw.rect(screen, BLACK, [0, y+10, 800, 5])
    pygame.draw.rect(screen, BLACK, [0, y+25, 800, 5])
    for x in range(-50, 800, 50):
        draw_cloud(x, 5) 
 

    for x in range(75, 800, 200):
        draw_tree(x, 400) 
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
