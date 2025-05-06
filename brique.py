import pygame
from constantes import *

class Brique:
	"""
	Definie l'objet brique immobile dans le jeu.
	Attributs : xpos, ypos, vie, largeur, hauteur tous de type int
	Methodes : enVie(), collisionVerticale(balle), collisionHorizontale(balle),
	collision(balle), affiche()
	"""

	def __init__(self, xpos, ypos, vie):
		self.xpos = xpos
		self.ypos = ypos
		self.vie = vie
		self.largeur = LARGEUR_ECRAN // 15
		self.hauteur = 20
		

	def enVie(self):
		""" indique si la brique à un nombre de vie strictement positif
		Paramètres :
			une brique mais utiliser br.enVie()
		Return :
			True si self.vie > 0
			False sinon
		"""
		return self.vie > 0

	def collisionVerticale(self, balle):
		return balle.xpos > self.xpos and balle.xpos < self.xpos + self.largeur and \
			((balle.ypos < self.ypos and balle.ypos + balle.rayon > self.ypos) or \
			(balle.ypos > self.ypos + self.hauteur and balle.ypos - balle.rayon < self.ypos + self.hauteur))

	def collisionHorizontale(self, balle):
		return balle.ypos > self.ypos and balle.ypos < self.ypos + self.hauteur and \
			((balle.xpos < self.xpos and balle.xpos + balle.rayon > self.xpos) or \
			(balle.xpos > self.xpos + self.largeur and balle.xpos - balle.rayon < self.xpos + self.largeur))
				
	def collision(self, balle):
		if self.enVie():
			if self.collisionVerticale(balle):
				balle.yvit = -balle.yvit
				self.vie -= 1
				balle.xpos += balle.xvit
				balle.ypos += balle.yvit
			elif self.collisionHorizontale(balle):
				balle.xvit = -balle.xvit
				self.vie -= 1
				balle.xpos += balle.xvit
				balle.ypos += balle.yvit

	def affiche(self, ecran):
		if self.enVie():
			pygame.draw.rect(ecran, (0,0,0), (self.xpos, self.ypos, self.largeur, self.hauteur))
			if self.vie > 1:
				pygame.draw.rect(ecran, (255,0,0), (self.xpos+1, self.ypos+1, self.largeur-2, self.hauteur-2))
			else :
				pygame.draw.rect(ecran, (0,255,0), (self.xpos+1, self.ypos+1, self.largeur-2, self.hauteur-2))
