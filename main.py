import sys
import random
import pygame
import time
import math
from pygame import mixer
mixer.init()
import os

path = "music"
all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.ogg')]
mixer.music.set_volume(0.7)
import random

randomfile = random.choice(all_mp3)

import pygame

pygame.mixer.init()
pygame.mixer.music.load(randomfile)
pygame.mixer.music.play()
import pygame


pygame.init()


display_width = 960
display_height = 635

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('gradient switch')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('pictures/whadkgames.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width)
y = (display_height)


gameDisplay.blit(carImg, (0, 0))
pygame.display.flip()
showing_solution = True

time.sleep(2)

gameDisplay.blit (carImg, (0, 0))
pygame.display.flip()

carImg = pygame.image.load('pictures/gradientgame.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width)
y = (display_height)


gameDisplay.blit(carImg, (0, 0))
pygame.display.flip()
showing_solution = True
changed_game_state = False
while changed_game_state == False:
    ev = pygame.event.wait()
    if ev.type == pygame.MOUSEBUTTONDOWN:
        changed_game_state = True
        gameDisplay.blit (carImg, (0, 0))
        pygame.display.flip()

IMAGE_FILE = "ding3.png" 
IMAGE_SIZE = (1000, 800)
TILE_WIDTH = 200
TILE_HEIGHT = 200
COLUMNS = 5
ROWS = 4

# bottom right corner contains no tile
EMPTY_TILE = (COLUMNS-1, ROWS-1)   

BLACK = (0, 0, 0)

# horizontal and vertical borders for tiles
hor_border = pygame.Surface((TILE_WIDTH, 1))
hor_border.fill(BLACK)
ver_border = pygame.Surface((1, TILE_HEIGHT))
ver_border.fill(BLACK)

# load the image and divide up in tiles
# putting borders on each tile also adds them to the full image
image = pygame.image.load(IMAGE_FILE)
tiles = {}
for c in range(COLUMNS) :
    for r in range(ROWS) :
        tile = image.subsurface (
            c*TILE_WIDTH, r*TILE_HEIGHT, 
            TILE_WIDTH, TILE_HEIGHT)
        tiles [(c, r)] = tile
        if (c, r) != EMPTY_TILE:
            tile.blit(hor_border, (0, 0))
            tile.blit(hor_border, (0, TILE_HEIGHT-1))
            tile.blit(ver_border, (0, 0))
            tile.blit(ver_border, (TILE_WIDTH-1, 0))
            # make the corners a bit math.floored
            tile.set_at((1, 1), BLACK)
            tile.set_at((1, TILE_HEIGHT-2), BLACK)
            tile.set_at((TILE_WIDTH-2, 1), BLACK)
            tile.set_at((TILE_WIDTH-2, TILE_HEIGHT-2), BLACK)
tiles[EMPTY_TILE].fill(BLACK)

# keep track of which tile is in which position
state = {(col, row): (col, row) 
            for col in range(COLUMNS) for row in range(ROWS)}

# keep track of the position of the empty tyle
(emptyc, emptyr) = EMPTY_TILE

# start game and display the completed puzzle
pygame.init()
display = pygame.display.set_mode(IMAGE_SIZE)
pygame.display.set_caption("gradient switch")
display.blit (image, (0, 0))
pygame.display.flip()

# swap a tile (c, r) with the neighbouring (emptyc, emptyr) tile
def switch (c, r) :
    global emptyc, emptyr 
    display.blit(
        tiles[state[(c, r)]],
        (emptyc*TILE_WIDTH, 
        emptyr*TILE_HEIGHT))
    display.blit(
        tiles[EMPTY_TILE],
        (c*TILE_WIDTH, 
        r*TILE_HEIGHT))
    state[(emptyc, emptyr)] = state[(c, r)]
    state[(c, r)] = EMPTY_TILE
    (emptyc, emptyr) = (c, r)
    pygame.display.flip()

# shuf the puzzle by making some random switch moves
def shuf() :
    global emptyc, emptyr
    last_r = 0 
    for i in range(75):
        pygame.time.delay(0)
        while True:
            r = random.randint(1, 4)
            if (last_r + r == 5):
                continue
            if r == 1 and (emptyc > 0):
                switch(emptyc - 1, emptyr) 
            elif r == 4 and (emptyc < COLUMNS - 1):
                switch(emptyc + 1, emptyr) 
            elif r == 2 and (emptyr > 0):
                switch(emptyc, emptyr - 1) 
            elif r == 3 and (emptyr < ROWS - 1):
                switch(emptyc, emptyr + 1) 
            else:
                
                continue
            last_r=r
            break 


at_start = True
showing_solution = False
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN :
        if at_start:
            
            shuf()
            at_start = False
        elif event.dict['button'] == 1:
    
            mouse_pos = pygame.mouse.get_pos()
            c = mouse_pos[0] / TILE_WIDTH
            
            r = mouse_pos[1] / TILE_HEIGHT
            if (    (abs(math.floor(c)-emptyc) == 1 and math.floor(r) == emptyr) or  
                    (abs(math.floor(r)-emptyr) == 1 and math.floor(c) == emptyc)):
                try:
                    switch (math.floor(c), math.floor(r))
                except:
                    pass
            else:
                print(c)
                print(r)
                print(emptyc)
                print(emptyr)
        elif event.dict['button'] == 3:
            # mouse right button: show solution image
            saved_image = display.copy()
            display.blit(image, (0, 0))
            pygame.display.flip()
            showing_solution = True
    elif showing_solution and (event.type == pygame.MOUSEBUTTONUP):
        # stop showing the solution
        display.blit (saved_image, (0, 0))
        pygame.display.flip()
        showing_solution = False