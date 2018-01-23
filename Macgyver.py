# -*- coding: Utf-8 -*

import random
import pygame
from constants import *

class Niveau:
#générer le labyrinthe à partir du fichier lab1
    def __init__(self):
        self.structure = 0
        self.inventory = 0
        self.structure_map = self.generer()
        self.mac_case_y = 0
        self.mac_case_x = 0

    def generer(self):

        with open("lab1", "r") as fichier:#on ouvre le fichier du labyrinthe
            structure_niveau = []#permet de generer une liste
            for ligne in fichier:#permet de lire les lignes du fichier
                ligne_niveau = []#permet de generer une nouvelle liste pour faire une liste de liste
                for caractere in ligne:#permet de generer une liste dans la liste
                    if caractere != "\n":#si le characterte est different de \n on l'affiche
                        ligne_niveau.append(caractere)# ajoute chaque characteres a la liste de la ligne

                structure_niveau.append(ligne_niveau)#ajoute chaque ligne a la liste

        while self.inventory <3:
            #place les objets dans le labyrinthe
            x_item = random.randint(0, 14)
            y_item = random.randint(1, 14)

            if structure_niveau[y_item][x_item] == "o":
                if self.inventory == 0:
                    structure_niveau[y_item][x_item] = needle_item
                elif self.inventory == 1:
                    structure_niveau[y_item][x_item] = tube_item
                elif self.inventory == 2:
                    structure_niveau[y_item][x_item] = ether_item

                self.inventory += 1
                self.structure = structure_niveau#permet de recuperer "structure" pour une utilisation pour une autre methode apr exemple

        return structure_niveau
    """
    def localise(self):
        mac_position = "m"
        number_line_mac = 0
        for line in self.structure_map:
            number_case_mac = 0
            for sprite in line:
                sprite_x_mac = number_case_mac * sprite_size
                sprite_y_mac = number_line_mac * sprite_size + banner_size
                if sprite == mac_position:
                    number_case_mac, number_line_mac = sprite, line

            number_case_mac += 1
        number_case_mac += 1
        print(sprite)
    """
    def display(self, screen):
        wall = pygame.image.load(img_wall).convert_alpha()
        floor = pygame.image.load(img_floor).convert_alpha()
        needle = pygame.image.load(img_needle).convert_alpha()
        tube = pygame.image.load(img_tube).convert_alpha()
        ether = pygame.image.load(img_ether).convert_alpha()
        mac = pygame.image.load(img_mac).convert()
        murdoc = pygame.image.load(img_murdoc).convert()
        background = pygame.image.load(img_background).convert()
        number_line = 0
        for line in self.structure_map:
            number_case = 0
            for sprite in line:
                sprite_x = number_case * sprite_size
                sprite_y = number_line * sprite_size + banner_size
                if sprite == "w":
                    screen.blit(wall,(sprite_x,sprite_y))
                #elif sprite == "o": (image de sol??)
                    #screen.blit(floor,(sprite_x,sprite_y))
                elif sprite == needle_item:
                    screen.blit(needle,(sprite_x,sprite_y))
                elif sprite == tube_item:
                    screen.blit(tube,(sprite_x,sprite_y))
                elif sprite == ether_item:
                    screen.blit(ether,(sprite_x,sprite_y))
                elif sprite == "g":
                    screen.blit(murdoc,(sprite_x,sprite_y))

                number_case += 1
            number_line += 1

class Character:
    def __init__(self, image, structure):
        #initialise x and y position
        self.case_x = 0
        self.case_y = 0
        #self.case_x = case_x
        #self.case_y = case_y
        self.x = 0
        self.y = 30
        self.structure = structure
        self.image = pygame.image.load(img_mac).convert_alpha()#add the conversion for pygame image
        self.inventory = 0

    def move(self, direction):
        #déplacement à droite
        if direction == "right":
            if self.case_x < (number_sprite_line - 1):
                if self.structure.structure_map[self.case_y][self.case_x+1] !="w":
                    self.case_x += 1
                    self.x = self.case_x * sprite_size
        if direction == "left":
            if self.case_x > 0:
                if self.structure.structure_map[self.case_y][self.case_x-1] !="w":
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
        if direction == "up":
            if self.case_y > 0:
                if self.structure.structure_map[self.case_y-1][self.case_x] !="w":
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size + banner_size #add size of the banner
        if direction == "down":
            if self.case_y < (number_sprite_line - 1):
                if self.structure.structure_map[self.case_y+1][self.case_x] !="w":
                    self.case_y += 1
                    self.y = self.case_y * sprite_size + banner_size

    #def convert(self, img_convert): (a utiliser si changement d'image de macgyver apres avoir recuperé tout les objets)

        #self.image_convert = pygame.image.load(img_convert).convert_alpha()#add the conversion for pygame image

    def reset(self):

        self.structure.structure_map[self.case_y][self.case_x] = "o"

    def collect_inventory(self):
        self.inventory += 1

    def display_inventory(self):
        count = "inventory : "+ (str(self.inventory))
        return count
        #“inventaire = {}"
        #machin.format(self.inventory)
