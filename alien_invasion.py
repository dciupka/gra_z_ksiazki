import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Ogolna kalasa przeznaczona do zarządzania zasobami i sposobem działania gry"""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #napis na pasku
        pygame.display.set_caption("Inwazja obcych")


    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            #Oczekiwanie na nacisnience klawiasza
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Odświeżanie ekranu w trakcie każdej iteracji pętli
            self.screen.fill(self.settings.bg_color)
            #Wyswietlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
