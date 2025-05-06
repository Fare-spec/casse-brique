import pygame
import math
from constantes import *


class Balle:
    """
    Definie une balle qui se deplace dans la fenetre ecran
    Attributs : rayon, xpos, ypos, xvit, yvit
    Methodes : deplace, doitRebondir(raquette), affiche
    """

    def __init__(self):
        self.rayon = 10
        self.xpos = LARGEUR_ECRAN / 2
        self.ypos = HAUTEUR_ECRAN / 2
        self.xvit = 4.5
        self.yvit = 3.0

    def doitRebondir(self, raquette):
        return (
            self.xpos >= raquette.xpos
            and self.xpos <= raquette.xpos + raquette.largeur
            and self.ypos >= HAUTEUR_ECRAN - 30
        )

    def deplace(self, raquette):
        self.xpos += self.xvit
        self.ypos += self.yvit
        if self.doitRebondir(raquette):
            angle_degre = 10 + 160 * (
                1 - (self.xpos - raquette.xpos) / raquette.largeur
            )
            angle_radian = angle_degre * math.pi / 180
            old_xvit = self.xvit
            self.xvit = math.sqrt(self.xvit**2 + self.yvit**2) * math.cos(angle_radian)
            self.yvit = -math.sqrt(old_xvit**2 + self.yvit**2) * math.sin(angle_radian)
            self.xpos += self.xvit
            self.ypos += self.yvit
        if self.xpos + self.rayon > LARGEUR_ECRAN or self.xpos - self.rayon < 0:
            self.xvit = -self.xvit
            self.xpos += self.xvit
            self.ypos += self.yvit
        elif self.ypos - self.rayon < 0:
            self.yvit = -self.yvit
            self.xpos += self.xvit
            self.ypos += self.yvit

    def affiche(self, ecran):
        pygame.draw.circle(
            ecran, (0, 0, 0), (int(self.xpos), int(self.ypos)), self.rayon
        )


if __name__ == "__main__":
    b1 = Balle()
    print(b1.xpos)
