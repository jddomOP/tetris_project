from grid import Grid
from blocks import *
import random
import pygame

class Game:
	def __init__(self):
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.score = 0
		self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

		pygame.mixer.music.load("Sounds/music.ogg")
		pygame.mixer.music.play(-1)

	def update_score(self, lines_cleared, move_down_points):
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		self.score += move_down_points
