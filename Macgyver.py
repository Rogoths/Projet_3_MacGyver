class Niveau:
#générer le labyrinthe à partir du fichier lab1

    def __init__(self):
        print("Affichage du labyrinthe")
        with open("lab1", "r") as self.structure:
            self.ouverture_fichier = self.structure.read()
            self.generation_liste = list(self.ouverture_fichier)

labyrinthe = Niveau()
print(labyrinthe.generation_liste)




#afficher ce labyrinthe
#print(self.fichier())
#localiser macgyver sur le labyrinthe
#"""if "m" dans la liste alors position du joueur"""
#macgyver peut mourir
#"""if déplacement "m" sur position liste m+1, m-1, m+15, m-15 == "g" sans les objets alors game over"""
#faire déplacer MacGyver avec les touches directionnelles
 #"""if "m" dans la liste récupérer sa position dans la liste"""
 #"""if les positions dans la liste m+1, m-1, m+15, m-15 == "0" alors peut se déplacer"""
 #"""if les positions dans la liste m+1, m-1, m+15, m-15 == "w" alors déplacement impossible"""
 #"""remplacer la position de "m" dans la liste par une nouvelle"""
#macgyver doit récupérer des objets pour sortir
#"""placer aléatoirement dans la liste du labyrinthe les objets"""
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
