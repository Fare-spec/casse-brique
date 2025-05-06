import sys, pygame
import bouton
from constantes import *


class Highscore:
	"""
	
	"""
	
	def __init__(self):
		self.fichier = "highscore.txt"
		self.bouton_quitter = bouton.Bouton((100, 100, 400, 100), "Retour au Menu", (255,0,0))
		
	def gereHighScore(self, ecran):
		pass
