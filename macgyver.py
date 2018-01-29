# -*- coding: Utf-8 -*
"""file for the class og the game"""
import random
import pygame
from constants import *

class Level:
    """class that create level maze"""
    def __init__(self):
        self.structure = 0
        self.inventory = 0
        self.structure_map = self.generate()
        self.mac_case_y = 0
        self.mac_case_x = 0

    def generate(self):
        """generate the maze from an external file to a list of lists"""
        with open("lab1", "r") as file:#open the file
            structure_level = []#generate a list
            for line in file:#read the line from the file
                line_level = []
                for letter in line:#generate lists in the list
                    if letter != "\n":#disable the return
                        line_level.append(letter)#add letters to the list of the line

                structure_level.append(line_level)#add each lines in the list

        while self.inventory < 3:

            x_item = random.randint(0, 14)
            y_item = random.randint(0, 14)
            #placement of the items in the structure
            if structure_level[y_item][x_item] == "o":
                if self.inventory == 0:
                    structure_level[y_item][x_item] = NEEDLE_ITEM
                elif self.inventory == 1:
                    structure_level[y_item][x_item] = TUBE_ITEM
                elif self.inventory == 2:
                    structure_level[y_item][x_item] = ETHER_ITEM

                self.inventory += 1
                self.structure = structure_level#create the level

        return structure_level

    def display(self, screen):
        """display images in the maze previously generated"""
        wall = pygame.image.load(IMG_WALL).convert_alpha()
        needle = pygame.image.load(IMG_NEEDLE).convert_alpha()
        tube = pygame.image.load(IMG_TUBE).convert_alpha()
        ether = pygame.image.load(IMG_ETHER).convert_alpha()
        murdoc = pygame.image.load(IMG_MURDOC).convert()
        number_line = 0
        for line in self.structure_map:
            number_case = 0
            for sprite in line:
                sprite_x = number_case * SPRITE_SIZE
                sprite_y = number_line * SPRITE_SIZE + BANNER_SIZE
                if sprite == "w":
                    screen.blit(wall, (sprite_x, sprite_y))
                elif sprite == NEEDLE_ITEM:
                    screen.blit(needle, (sprite_x, sprite_y))
                elif sprite == TUBE_ITEM:
                    screen.blit(tube, (sprite_x, sprite_y))
                elif sprite == ETHER_ITEM:
                    screen.blit(ether, (sprite_x, sprite_y))
                elif sprite == "g":
                    screen.blit(murdoc, (sprite_x, sprite_y))

                number_case += 1
            number_line += 1

class Character:
    """class that create the character"""
    def __init__(self, image, structure):

        self.case_x = 0#initialise the start position from the structure
        self.case_y = 0
        self.x = 0
        self.y = 30#start position with the banner size.
        self.structure = structure
        self.image = pygame.image.load(IMG_MAC).convert_alpha()#add the conversion for pygame image
        self.inventory = 0

    def move(self, direction):
        """movements of the character"""
        #to the right
        if direction == "right":
            if self.case_x < (NUMBER_SPRITE_LINE - 1):
                if self.structure.structure_map[self.case_y][self.case_x + 1] != "w":
                    self.case_x += 1
                    self.x = self.case_x * SPRITE_SIZE
        if direction == "left":
            if self.case_x > 0:
                if self.structure.structure_map[self.case_y][self.case_x - 1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_SIZE
        if direction == "up":
            if self.case_y > 0:
                if self.structure.structure_map[self.case_y-1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIZE + BANNER_SIZE #add size of the banner
        if direction == "down":
            if self.case_y < (NUMBER_SPRITE_LINE - 1):
                if self.structure.structure_map[self.case_y+1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * SPRITE_SIZE + BANNER_SIZE

    def reset(self):
        """reset item on the maze when character go over it"""
        self.structure.structure_map[self.case_y][self.case_x] = "o"

    def collect_inventory(self):
        """add item in the inventory when character go over it"""
        self.inventory += 1

    def display_inventory(self):
        """display inventory in banner"""
        count = "ITEMS LEFT : {}".format(3 - self.inventory)
        return count
