import pygame
import game_config as gc

from pygame import display, event, image
from animal import Animal
from time import sleep


def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption('My Game')

screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png')

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
curr_images = []

while running:
    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in curr_images:
                curr_images.append(index)
            if len(curr_images) > 2:
                curr_images = curr_images[1:]

    
    screen.fill((255,255,255))

    total_skip = 0

    for i, tile in enumerate(tiles):
        image_i = tile.image if i in curr_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else :
            total_skip += 1
    display.flip()

    if len(curr_images) == 2:
        idx1, idx2 = curr_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            curr_images = []
    
    if total_skip == len(tiles):
        running = False 
        

print('Goodbye!!')