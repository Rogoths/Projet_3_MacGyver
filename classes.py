from pygame.locals import *
import pygame

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

macgyver = pygame.image.load("macgyver.png").convert_alpha() # charge l'image de macgyver
fenetre.blit(macgyver, (0,0))

pygame.display.flip() # permet d'avoir les images qui restent affichées


continuer = 1

while continuer: # permet d'avoir une fenêtre qui reste ouverte
	continue


class labyrinthe: # niveau du jeu

	def __init__(self):
		self.x = 15 # nombre de case en abscisse
		self.y = 15 # nombre de case en ordonnée
		self.labyrinthe = [ 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
							0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
							1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,] # le labyrinthe
				
	def afficher(self,afficher_mur):# afficher le labyrinthe

	    x = 0 # je définis la valeur de base qui servira à afficher mon labyrinthe
	    y = 0

	    for i in range(0,self.x*self.y):
	        if self.labyrinthe[ x + (y*self.x) ] == 1:
	               afficher_mur.blit("mur.png",( x * 15 , y * 15))
	 
	        x = x + 1
	        if x > self.x-1:
	            x = 0 
	            y = y + 1

#class macgyver:

	#def __init__(self): # personnage du jeu
		# déplacer macgyver
	# récupérer des objets
	#pass

#class objets:

	#def __init__(self): # objets à récupérer
	# se faire récolter et disparaître
	#pass