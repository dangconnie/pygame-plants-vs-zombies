import pygame;
from pygame.sprite import Sprite;

class Plant_Icon(Sprite):
	def __init__(self, game_settings, icon, slot):
		super(Plant_Icon, self).__init__();
		self.image = pygame.image.load('./images/' + icon);
		self.image = pygame.transform.scale(self.image,(100, 100));
		self.rect = self.image.get_rect();
		# put icons at top of screen in a tray
		self.rect.left = 300+(110 * slot);
		self.rect.top = 30;
		self.slot = slot;
