import random

class Niveau:
#générer le labyrinthe à partir du fichier lab1
    def __init__(self):
        self.structure = 0
        self.inventory = 0

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
                    structure_niveau[y_potion][x_potion] == "S" #sword
                elif self.inventory == 1:
                    structure_niveau[y_potion][x_potion] == "A" #armor
                elif self.inventory == 2:
                    structure_niveau[y_potion][x_potion] == "P" #potion

        self.structure = structure_niveau#permet de recuperer "structure" pour une utilisation pour une autre methode apr exemple

        print(structure_niveau)

class Macgyver(Niveau):
    def __init__(self):
        Niveau.__init__(self)

    def deplacer(self):
        #on établi les positions par défaut de x et y
        self.case_x = 0
        self.case_y = 0
        Mac = self.structure.index("m")

        #déplacement à droite
        if self.direction == "droite":
            if self.structure[self.case_y][self.case_x+1] !="w":
                self.structure[self.case_y][self.case_x], self.structure[self.case_y][self.case_x+1] = self.structure[self.case_y][self.case_x+1], self.structure[self.case_y][self.case_x]

        if self.direction == "gauche":
            if self.structure[self.case_y][self.case_x-1] !="w":
                self.structure[self.case_y][self.case_x], self.structure[self.case_y][self.case_x-1] = self.structure[self.case_y][self.case_x-1], self.structure[self.case_y][self.case_x]

        if self.direction == "haut":
            if self.structure[self.case_y-1][self.case_x] !="w":
                self.structure[self.case_y][self.case_x], self.structure[self.case_y-1][self.case_x] = self.structure[self.case_y-1][self.case_x], self.structure[self.case_y][self.case_x]

        if self.direction == "bas":
            if self.structure[self.case_y+1][self.case_x] !="w":
                self.structure[self.case_y][self.case_x], self.structure[self.case_y+1][self.case_x] = self.structure[self.case_y+1][self.case_x], self.structure[self.case_y][self.case_x]

labyrinthe = Niveau()
labyrinthe.generer()




#afficher ce labyrinthe
#print(self.fichier())
#localiser macgyver sur le labyrinthe
#if "m" dans la liste alors position du joueur
#macgyver peut mourir
#if déplacement "m" sur position liste m+1, m-1, m+15, m-15 == "g" sans les objets alors game over"""

#macgyver doit récupérer des objets pour sortir
#placer aléatoirement dans la liste du labyrinthe les objets"""
#"""récupérer les objets est les mettre dans un inventaire(afficher le nombre d'objet)"""
#"""faire disparaître les objets de la liste"""

#localiser le gardien sur le labyrinthe

#terminer la partie
#"""if déplacement "m" sur position liste m+1, m-1, m+15, m-15 == "g" avec les objets alors gagné sinon perdu"""

#class macgyver: # class permettant de créer le personnage

	#def __init__(self):

		#self.case_x = 0
		#self.case_y = 0
		#macgyver = "m"

		#def deplacer(self):
		#if deplacement == "haut"(m-15)


		#if deplacement == "bas"(m+15)


		#if deplacement == "gauche"(m-1)


		#if deplacement == "droite"(m+1)

	#récupérer des objets

#class objets:

	#def __init__(self): # objets à récupérer
	# se faire récolter et disparaître
