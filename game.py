# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from constants import *
from Macgyver import *

pygame.init()

#display the window
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("MacGyver")#name for the window
background = pygame.image.load(img_background).convert()#display background image
win_screen = pygame.image.load(img_win).convert_alpha()
pygame.display.flip()#refresh

#if True continue, if false stop
main_screen = True #booleen

while main_screen:
    load_game = False
    continue_game = True
    pygame.time.Clock().tick(30)#speed of the loop
    for event in pygame.event.get():#seek all the events in pygame
        if event.type == pygame.QUIT:#close the window
            main_screen = False
            load_game = False
            continue_game = False
        elif event.type == KEYDOWN:#press a key on the keyboard
            if event.key == K_RETURN:#and Return is activated
                load_game = True#load_game screen is display
                main_screen = False#main screen is closed
                continue_game = True#stay the same
    pygame.display.flip()#refresh

    if load_game == True:
        #create the maze and display
        maze = Niveau()
        maze.display(screen)
        #create Macgyver character
        Mac = Characters(mac_case_x, mac_case_y, img_mac, maze)#macgyver object

while continue_game:

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        item = 0
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
            Mac.collect_inventory()
        if maze.structure_map[Mac.case_y][Mac.case_x] == tube_item:
            Mac.reset()
            Mac.collect_inventory()
        if maze.structure_map[Mac.case_y][Mac.case_x] == ether_item:
            Mac.reset()
            Mac.collect_inventory()
        #win
        if maze.structure_map[Mac.case_y][Mac.case_x] == "g":
            if Mac.inventory >= 3:
                continue_game = False
                win = True
                while win:
                    pygame.time.Clock().tick(30)
                    screen.blit(win_screen,(0,0))
        #lose
        elif maze.structure_map[Mac.case_y][Mac.case_x] == "g":
            if Mac.inventory < 3:
                continue_game = False
                lose = True
                while lose:
                    pygame.time.Clock().tick(30)
                    screen.blit(lose_screen,(0,0))
                    pygame.display.flip() #will update the contents of the entire display
        screen.blit(background, (0,0))
        maze.display(screen)
        screen.blit(Mac.image_convert,(Mac.x,Mac.y))#from Mac object use png file to reuse it(image_convert = mac sprite from Mac object)
        pygame.display.flip() #will update the contents of the entire display
        #display inventory
        #victory
