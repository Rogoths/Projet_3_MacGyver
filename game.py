# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from constants import *
from Macgyver import *

pygame.init()

#display de the window
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("MacGyver")

#if True continue, if false stop
main_screen = True

while main_screen:
    load_game = False
    continue_game = True
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():#seek all the events in pygame
        if event.type == pygame.QUIT:
            main_screen = False
            load_game = False
            continue_game = False
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:#press start to continue
                load_game = True
                main_screen = False
                continue_game = True
    pygame.display.update()

    if load_game == True:
        #create the maze and display
        maze = Niveau()
        maze.display(screen)
        #create Macgyver character
        Mac = Macgyver(mac_case_x, mac_case_y, img_mac_nerd, maze)

while continue_game:

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                Mac.move('up')
            if event.key == K_LEFT:
                Mac.move('left')
            if event.key == K_DOWN:
                Mac.move('down')
            if event.key == K_RIGHT:
                Mac.move('right')
            if event.type == pygame.QUIT:
                continue_game = False

        if maze.structure_map[Mac.case_y][Mac.case_x] == needle_item:
            Mac.reset()
        if maze.structure_map[Mac.case_y][Mac.case_x] == tube_item:
            Mac.reset()
        if maze.structure_map[Mac.case_y][Mac.case_x] == ether_item:
            Mac.reset()


        #if maze.structure_map[Mac.case_y][Mac.case_x] == "g" and


        maze.display(screen)
        screen.blit(Mac.image_convert,(Mac.x,Mac.y))
    pygame.display.flip() #will update the contents of the entire display
