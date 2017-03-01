import pygame;
from pygame.sprite import Sprite;


class Square(Sprite):
	def __init__(self, screen, game_settings,i,j):
		super(Square, self).__init__();
		self.screen = screen
		self.screen_rect = self.screen.get_rect();

		# dictionary --> use brackets
		self.width = game_settings.squares["square_width"];
		self.height = game_settings.squares["square_height"];
		self.rect = pygame.Rect(0,0,self.width, self.height);

		# i is the number of heights to use. How many rows down? 0 to 4.
		# j is the number of widths to use. How many columns over are we? 0 to 8.
		self.rect.left = (j * self.width) + game_settings.squares["start_left"];
		self.rect.top = (i * self.height) + game_settings.squares["start_top"];

		# we also want to know what square number this is
		self.square_number = (i*9) + (j+1);
		self.row_number = i;
		self.column = j;
		self.plant_here = False;


		print self.square_number;