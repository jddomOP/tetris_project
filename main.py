import pygame
from pygame.examples.headless_no_windows_needed import screen

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python tetris")

clock = pygame.time.Clock()

while True:
    for event in pyfame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update

