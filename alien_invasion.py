import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Ogolna kalasa przeznaczona do zarządzania zasobami i sposobem działania gry"""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #napis na pasku
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            #Odświeżanie ekranu w trakcie każdej iteracji pętli
            self._update_screen()

            #Wyswietlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()

    def _check_events(self):
        """Reakcja generowana  na zarzenie przez klawiature i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Odświeżanie ekranu w trakcie każdej iteracji pętli"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
