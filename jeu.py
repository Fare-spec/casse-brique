import sys, pygame
import niveau
from constantes import *


class Jeu:
	"""gère les différents états d'un jeu"""

	def __init__(self):
		self.n1 = niveau.Niveau()
		self.vie = 3
		self.bouge = False
		self.etatJeu = 1
		
	def gereJeu(self, ecran):
		if self.etatJeu == 1: #Debut de niveau
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	#Evt de sortie de boucle
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.bouge = True
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.bouge = True
			self.n1.affiche(ecran)
			if self.bouge:
				self.etatJeu = 2
		elif self.etatJeu == 2: #Niveau en cours
			self.etatJeu = self.n1.gereNiveau(ecran)
		elif self.etatJeu ==3: #Changement de niveau
			pass
			
		return 1
			
		


"""
while True:		#Demarrage de la boucle infinie
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	#Evt de sortie de boucle
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			bouge = not bouge
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			bouge = not bouge		
	if pygame.key.get_pressed()[pygame.K_q] == True:
		r1.deplaceGauche()
	if pygame.key.get_pressed()[pygame.K_d] == True:
		r1.deplaceDroite()

	ecran.fill(BLANC)
	
	if bouge:
		b1.deplace(r1)
	m1.collision(b1)
	
	b1.affiche(ecran)
	r1.affiche(ecran)
	m1.affiche(ecran)
	

	
	pygame.display.update() #rafraichissement
	clock.tick(60)
"""
