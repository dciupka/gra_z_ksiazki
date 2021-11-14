import pygame

class Ship:
    '''Klasa przeznaczona do zarządzania statkiem'''

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jeog położenie początkowe"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Wczytanie obrazu statku
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Każdy nowy statek pojawi sie na dole ekranu
        self.rect.midbottom  = self.screen_rect.midbottom

    def blitme(self):
        """Wyświetlanie statku w jego aktualnym połozeniu nad tłem"""
        self.screen.blit(self.image,self.rect)