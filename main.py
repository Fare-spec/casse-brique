import sys, pygame
import bouton
import constantes
import pygame.freetype
import jeu, highscore

def affiche_menu(ecran):
	b1.affiche(ecran)
	b2.affiche(ecran)
	b3.affiche(ecran)
	return 0
	

pygame.init()	#initialisation des modules de pygame

# Creation de la fenetre
ecran = pygame.display.set_mode((constantes.LARGEUR_ECRAN, constantes.HAUTEUR_ECRAN))
ecran.fill(constantes.BLANC) 
pygame.display.set_caption('Casse Brique')

clock = pygame.time.Clock()

b1 = bouton.Bouton((100, 100, 400, 100), "Jouer", (255,0,0))
b2 = bouton.Bouton((100, 300, 400, 100), "Highscore", (255,0,0))
b3 = bouton.Bouton((100, 500, 400, 100), "Quitter", (255,0,0))
hs1 = highscore.Highscore()
j1 = jeu.Jeu()
etat = 0




while True:		#Demarrage de la boucle infinie
	if etat == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#Evt de sortie de boucle
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				if b1.zone_cliquable.collidepoint(event.pos):
					etat = 1
				elif b2.zone_cliquable.collidepoint(event.pos):
					etat = 2
				elif b3.zone_cliquable.collidepoint(event.pos):
					sys.exit()

	ecran.fill(constantes.BLANC) 
	
	if etat == 0:
		etat = affiche_menu(ecran)
	elif etat == 1:
		etat = j1.gereJeu(ecran)
	elif etat == 2:
		etat = hs1.gereHighScore(ecran)
	

	pygame.display.update() #rafraichissement
	clock.tick(60)

