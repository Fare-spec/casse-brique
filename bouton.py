import pygame
import pygame.freetype


class Bouton:
    """
    Définie un bouton composé :
    d'une zone cliquable : un Rect de pygame
    un texte : à afficher au centre de la zone cliquable
    une couleur de fond : (r,v,b)
    éventuellement une font :
    """

    def __init__(self, zone, texte, couleur):
        """
        Initialise une instance de bouton.
        Paramètres :
                zone : 4-uple (top, left, width, height)
                texte : String
                couleur : 3-uple (r,v,b)
        """
        self.zone_cliquable = pygame.Rect(zone)
        self.texte = texte
        self.couleur = couleur
        self.ma_Font = pygame.freetype.SysFont("digital-7.ttf", 20)

    def affiche(self, ecran):
        """
        Affiche dans la surface ecran la Surface associé au Rect
        avec le texte centré dans la Surface.
        """
        zone_aff = pygame.Surface(self.zone_cliquable.size)
        zone_aff.fill(self.couleur)
        ecran.blit(zone_aff, self.zone_cliquable)
        text_Surf, text_Rect = self.ma_Font.render(self.texte, (0, 0, 0))
        text_Rect.center = self.zone_cliquable.center
        ecran.blit(text_Surf, text_Rect)
