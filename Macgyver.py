import random

class Niveau:
#générer le labyrinthe à partir du fichier lab1
    def __init__(self):
        self.structure = 0
        self.inventory = 0
        self.structure_map = self.generer()

    def generer(self):
        print("Affichage du labyrinthe")
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
            x_potion = random.randint(0, 14)
            y_potion = random.randint(0, 14)

            if structure_niveau[y_potion][x_potion] == "o":
                if self.inventory == 0:
                    structure_niveau[y_potion][x_potion] = "S" #sword
                elif self.inventory == 1:
                    structure_niveau[y_potion][x_potion] = "A" #armor
                elif self.inventory == 2:
                    structure_niveau[y_potion][x_potion] = "P" #potion

                self.inventory += 1
                self.structure = structure_niveau#permet de recuperer "structure" pour une utilisation pour une autre methode apr exemple

        print(structure_niveau)
"""
    def display(self):

        for line in self.structure_map:
            for caractere in line:
                print(self.structure_map[line][caractere], end=" ")
            print()
"""


class Macgyver:
    def __init__(self, case_x, case_y, structure):
        #on établi les positions par défaut de x et y
        self.case_x = 0
        self.case_y = 0
        self.case_x = case_x
        self.case_y = case_y
        self.structure = structure

    def move(self, direction):
        #déplacement à droite
        if direction == "right":
            if self.structure.structure_map[self.case_y][self.case_x+1] !="w":
                self.case_x += 1
        if direction == "left":
            if self.structure.structure_map[self.case_y][self.case_x-1] !="w":
                self.case_x -= 1
        if direction == "up":
            if self.structure.structure_map[self.case_y-1][self.case_x] !="w":
                self.case_y -= 1
        if direction == "down":
            if self.structure.structure_map[self.case_y+1][self.case_x] !="w":
                self.case_y += 1


start_game = 1
mac_case_x = 0
mac_case_y = 0
items = 0

while start_game:

    if start_game == 1:
        #create the maze and display
        maze = Niveau()
        mac = Macgyver(mac_case_x, mac_case_y, maze)


    continue_game = 1
    direction = input("direction?")

    while continue_game:

        if direction == "right":
            mac.move("right")
        if direction == "left":
            mac.move("left")
        if direction == "up":
            mac.move("up")
        if direction == "down":
            mac.move("down")

    if maze.structure_map[mac.mac_case_y][mac_case_x] == "S":
        items += 1# increase inventory
        print(items)#display number of items

    if maze.structure_map[mac.mac_case_y][mac_case_x] == "A":
        items += 1
        print(items)

    if maze.structure_map[mac.mac_case_y][mac_case_x] == "P":
        items += 1
        print(items)

    if maze.structure_map[mac.mac_case_y][mac_case_x] == "g":
        if items >= 3:
            maze.structure_map[mac.mac_case_y][mac_case_x] = "o"
            print("Bravo!")

        else:
            print("Perdu!")
