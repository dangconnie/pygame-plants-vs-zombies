import pygame;
from pygame.sprite import Sprite;


class Square(Sprite):
	def __init__(self,screen, game_settings, i, j):
		super(Square, self).__init__();
		self.screen = screen;
		self.screen_rect = self.screen.get_rect();

		# dictionary --> use brackets
		self.width = game_settings.squares["square_width"];
		self.height = game_settings.squares["square_height"];


		self.rect = pygame.Rect(0,0,self.width, self.height) #what about pygame?

