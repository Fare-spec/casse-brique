import brique
from constantes import *


class Murdebrique:
    """
    definie un mur compose de briques 15 en largeur et 5 rangees
    Les briques ont une largeur de LARGEUR_ECRAN//15 et une hauteur de 20
    Il doit y avoir 50 px au dessus du mur.
    La rangée du haut contient des briques ayant 2 vies
    Attributs : mur de type liste
    Méthodes : collision(balle), affiche(ecran)
    """

    def __init__(self, bricks):
        self.mur = []
        ligne = []
        for i in range(len(bricks)):
            for j in range(len(bricks[i])):
                ligne.append(brique.Brique((LARGEUR_ECRAN // 15) * j, 70 + 20 * i, 1))
            self.mur.append(ligne)

    def collision(self, balle):
        for i in range(len(self.mur)):
            for j in range(len(self.mur[i])):
                self.mur[i][j].collision(balle)

    def affiche(self, ecran):
        for i in range(len(self.mur)):
            for j in range(len(self.mur[i])):
                self.mur[i][j].affiche(ecran)
