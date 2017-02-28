import pygame;
from pygame.sprite import Sprite;

class Plant(Sprite):
	def __init__(self):
		super(Plant, self).__init__();
		# self.screen = screen;
		self.screen_rect = self.screen.get_rect();

		self.image = pygame.image.load(self.image_file);
		self.image = pygame.transform.scale(self.image, (99,96));
		self.rect = self.image.get_rect();

		# child is setting the square so parent doesn't need to do it as well
		# self.square = square;
		self.rect.left = self.square.rect.left + 10;
		self.rect.top = self.square.rect.top;

	def draw_me(self):
		self.screen.blit(self.image, self.rect);