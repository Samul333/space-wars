
from game import GameManger
from constants import WIDTH,HEIGHT
import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Space Shooter Game")
    clock = pygame.time.Clock()
    game = GameManger(window,clock)
    game.start()


main()