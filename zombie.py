import pygame;
from pygame.sprite import Sprite;

class Zombie(Sprite):
	def __init__(self, screen, speed, health):
		super(Zombie,self).__init__();
		self.speed = speed;
		self.health = health;
		self.image = pygame.image.load('./images/Crazyzombie.gif')
		self.image = pygame.transform.scale(self.image,(127,148));
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right;

		self.x = float(self.rect.x);

	def update_me(self):
		self.x -= self.speed * 5;
		# right now, zombies can only move on the x axis
		self.rect.x = self.x;

	def draw_me(self):
		self.screen.blit(self.image, self.rect);
