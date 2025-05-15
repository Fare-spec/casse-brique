import sys, pygame
import balle, raquette, murdebrique
from constantes import *


class Niveau:
    """gère le jeu d'un niveau"""

    def __init__(self):
        self.b1 = balle.Balle()
        self.r1 = raquette.Raquette()
        self.m1 = murdebrique.Murdebrique()
        self.vie = 3

    def is_alive(self):
        return self.vie >= 0

    def balle_perdue(self):
        if self.b1.ypos < HAUTEUR_ECRAN :
            self.vie -= 1
            self.replacer_balle()

    def replacer_balle(self):
        if self.is_alive():
            self.b1.xpos = LARGEUR_ECRAN / 2
            self.b1.ypos = HAUTEUR_ECRAN / 2 
            self.b1.xvit = 4.5
            self.b1.yvit = 3.0
        else:
            python.exit(0) 
            #Fo faire une fct pour la défaite
    
    def affiche_vie(self, ecran):
        ROSE = (255, 192,203)
        BLANC = (255,255,255)
        font = pygame.font.SysFont('Arial', 22)
        phrase = 'il reste ' + str(self.vie) + 'vies'
        text_surface = font.render(phrase, False, BLANC)
        ecran.blit(text_surface, (LARGEUR_ECRAN // 10, HAUTEUR_ECRAN //10))
    
    def affiche(self, ecran):
        ecran.fill(BLANC)
        self.b1.affiche(ecran)
        self.r1.affiche(ecran)
        self.m1.affiche(ecran)

    def gereNiveau(self, ecran):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Evt de sortie de boucle
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_q] == True:
            self.r1.deplaceGauche()
        if pygame.key.get_pressed()[pygame.K_d] == True:
            self.r1.deplaceDroite()

        self.b1.deplace(self.r1)
        self.m1.collision(self.b1)
        self.affiche(ecran)
        return 2
