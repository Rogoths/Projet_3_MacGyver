# -*- coding: Utf-8 -*
"""Help MacGyver to escape of the maze!
    -You need to find all the items on the map to craft the ultimate object
    -Murdoc keep the exit
    -If you find the exit without all the items Murdoc kill you
    -If you find the with all the items you sedate Murdoc and save your hair

    files : game.py , macgyver.py , constants.py , lab1 , /musics , /images"""

import pygame
from pygame.locals import *
from constants import *
from macgyver import Level, Character

pygame.init()

#display the window
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("MacGyver")#name for the window

#variables images
BACKGROUND = pygame.image.load(IMG_BACKGROUND).convert()#display background image
MAC_BANNER = pygame.image.load(IMG_MACGYVER_BANNER).convert()
WIN_SCREEN = pygame.image.load(IMG_WIN).convert_alpha()
LOSE_SCREEN = pygame.image.load(IMG_LOSE).convert_alpha()
MAC_ICON = pygame.image.load(IMG_MAC).convert()
NEEDLE = pygame.image.load(IMG_NEEDLE).convert_alpha()
TUBE = pygame.image.load(IMG_TUBE).convert_alpha()
ETHER = pygame.image.load(IMG_ETHER).convert_alpha()
MAINSCREEN = pygame.image.load(IMG_MAINSCREEN).convert_alpha()

#musics of the game
MAC_MUSIC = pygame.mixer.Sound(MUSIC_MAC)
MAC_MUSIC.set_volume(0.1)
WIN_MUSIC = pygame.mixer.Sound(MUSIC_WIN)
WIN_MUSIC.set_volume(0.02)
LOSE_MUSIC = pygame.mixer.Sound(MUSIC_LOSE)
LOSE_MUSIC.set_volume(0.02)

pygame.key.set_repeat(50, 50)# call set_repeat() to enable it
pygame.display.flip()#refresh

#if True continue, if false stop
main_screen = True #booleen

while main_screen:
    load_game = False
    continue_game = False
    MAC_MUSIC.play()
    SCREEN.blit(MAINSCREEN, (0, 30))
    font = pygame.font.Font(None, 30)
    text_mainscreen = font.render("Press ENTER to continue", 1, (255, 255, 255))
    text_instruction = font.render("Use directionnal key to move MacGyver", 1, (255, 255, 255))
    SCREEN.blit(text_mainscreen, (100, 300))
    SCREEN.blit(text_instruction, (30, 400))
    pygame.time.Clock().tick(60)#speed of the loop
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

    if load_game:
        #create the maze and display
        maze = Level()
        maze.display(SCREEN)
        #create Macgyver character
        macgyver = Character(MAC_ICON, maze)#macgyver object

while continue_game:

    pygame.time.Clock().tick(30)
    font = pygame.font.Font(None, 20)
    inventory = font.render(macgyver.display_inventory(), 1, (255, 255, 255)) # Display the text

    for event in pygame.event.get():
        #item = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:
                macgyver.move('up')
            if event.key == K_LEFT:
                macgyver.move('left')
            if event.key == K_DOWN:
                macgyver.move('down')
            if event.key == K_RIGHT:
                macgyver.move('right')
            if event.type == pygame.QUIT:
                continue_game = False
            if event.type == pygame.QUIT:#close the window
                main_screen = False
                load_game = False
                continue_game = False

        if maze.structure_map[macgyver.case_y][macgyver.case_x] == NEEDLE_ITEM:
            macgyver.reset()

            macgyver.collect_inventory()
            SCREEN.blit(NEEDLE, (210, 0))
        if maze.structure_map[macgyver.case_y][macgyver.case_x] == TUBE_ITEM:
            macgyver.reset()
            macgyver.collect_inventory()
            SCREEN.blit(TUBE, (240, 0))
        if maze.structure_map[macgyver.case_y][macgyver.case_x] == ETHER_ITEM:
            macgyver.reset()
            macgyver.collect_inventory()
            SCREEN.blit(ETHER, (270, 0))
        #win
        if maze.structure_map[macgyver.case_y][macgyver.case_x] == "g":
            MAC_MUSIC.stop()
            if macgyver.inventory >= 3:

                continue_game = False
                load_game = False
                win = True

                while win:#end_game
                    #if win...
                    WIN_MUSIC.play()
                    #SCREEN.blit(BACKGROUND, (0, 30))
                    SCREEN.blit(WIN_SCREEN, (90, 30))
                    font = pygame.font.Font(None, 30)
                    text = font.render("You are safe! Press ESCAPE to quit the game", 1, (255, 255, 255)) # Display the text in white with rounded edge
                    SCREEN.blit(text, (0, SPRITE_SIZE * NUMBER_SPRITE_COLUMN))#display the text
                    for event in pygame.event.get():
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:#after the game quit
                            win = False
                            WIN_MUSIC.stop()
                    pygame.display.flip()
            #lose
            else:
                continue_game = False
                load_game = False
                lose = True
                while lose:
                    LOSE_MUSIC.play()
                    SCREEN.blit(BACKGROUND, (0, 30))
                    SCREEN.blit(LOSE_SCREEN, (0, 0))
                    font = pygame.font.Font(None, 30)
                    text = font.render("You lose... Press ESCAPE to quit the game", 1, (255, 255, 255)) # Display the text in white with rounded edge
                    SCREEN.blit(text, (20, SPRITE_SIZE * NUMBER_SPRITE_COLUMN))#display the text
                    for event in pygame.event.get():
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                            lose = False #after the game quit
                            LOSE_MUSIC.play()

                    pygame.display.flip() #will update the contents of the entire display

        SCREEN.blit(MAC_BANNER, (0, 0))
        SCREEN.blit(BACKGROUND, (0, 30))
        maze.display(SCREEN)
        SCREEN.blit(macgyver.image, (macgyver.x, macgyver.y))#from Mac object use png file to reuse it(image_convert = mac sprite from Mac object)
        inventory.fill((0, 0, 0))
        SCREEN.blit(inventory, (300, 10))
        inventory = font.render(macgyver.display_inventory(), 1, (255, 255, 255))
        SCREEN.blit(inventory, (300, 10))
        pygame.display.flip() #will update the contents of the entire display
