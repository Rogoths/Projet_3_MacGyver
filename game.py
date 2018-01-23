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
mac_banner = pygame.image.load(img_macgyver_banner).convert()
win_screen = pygame.image.load(img_win).convert_alpha()
lose_screen = pygame.image.load(img_lose).convert_alpha()
mac_icon = pygame.image.load(img_mac).convert()
needle = pygame.image.load(img_needle).convert_alpha()
tube = pygame.image.load(img_tube).convert_alpha()
ether = pygame.image.load(img_ether).convert_alpha()
mainscreen = pygame.image.load(img_mainscreen).convert_alpha()

mac_music = pygame.mixer.Sound(music_mac)
mac_music.set_volume(0.1)

pygame.key.set_repeat(50, 50)# call set_repeat() to enable it
pygame.display.flip()#refresh

#if True continue, if false stop
main_screen = True #booleen

while main_screen:
    load_game = False
    continue_game = True
    mac_music.play()
    screen.blit(mainscreen, (0,30))
    font = pygame.font.Font(None, 30)
    text_mainscreen = font.render("Press ENTER to continue", 1, (255, 255, 255))
    screen.blit(text_mainscreen, (100 , 300))
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
        macgyver = Character(mac_icon, maze)#macgyver object

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

        if maze.structure_map[macgyver.case_y][macgyver.case_x] == needle_item:
            macgyver.reset()
            macgyver.collect_inventory()
            screen.blit(needle, (210,0))
        if maze.structure_map[macgyver.case_y][macgyver.case_x] == tube_item:
            macgyver.reset()
            macgyver.collect_inventory()
            screen.blit(tube, (240,0))
        if maze.structure_map[macgyver.case_y][macgyver.case_x] == ether_item:
            macgyver.reset()
            macgyver.collect_inventory()
            screen.blit(ether, (270,0))
        #win
        if maze.structure_map[macgyver.case_y][macgyver.case_x] == "g":
            if macgyver.inventory >= 3:

                continue_game = False
                load_game = False
                win = True
                while win:#end_game
                    #if win...
                    screen.blit(background, (0,30))
                    screen.blit(win_screen,(90,30))
                    font = pygame.font.Font(None, 30)
                    text = font.render("You won !", 1, (255, 255, 255)) # Display the text in white with rounded edge
                    screen.blit(text, (20,sprite_size*number_sprite_column))#display the text
                    for event in pygame.event.get():
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:#after the game quit
                            win = False

                    pygame.display.flip()

            #lose
            else:

                continue_game = False
                load_game = False
                lose = True
                while lose:
                    screen.blit(background, (0,30))
                    screen.blit(lose_screen,(0,0))
                    font = pygame.font.Font(None, 30)
                    text = font.render("You lose... Press ESCAPE to quit the game", 1, (255, 255, 255)) # Display the text in white with rounded edge
                    screen.blit(text, (20,sprite_size*number_sprite_column))#display the text
                    for event in pygame.event.get():
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:#after the game quit
                            lose = False

                    pygame.display.flip() #will update the contents of the entire display

        screen.blit(mac_banner, (0,0))
        screen.blit(background, (0,30))
        maze.display(screen)
        screen.blit(macgyver.image,(macgyver.x,macgyver.y))#from Mac object use png file to reuse it(image_convert = mac sprite from Mac object)
        screen.blit(inventory, (300,10))
        pygame.display.flip() #will update the contents of the entire display
