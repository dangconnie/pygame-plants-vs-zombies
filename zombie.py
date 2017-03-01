
import pygame;
from pygame.sprite import Sprite;
from random import randint;

class Zombie(Sprite):
	def __init__(self, screen, game_settings):
		super(Zombie,self).__init__();
		self.speed = game_settings.zombie_speed;
		self.health = game_settings.zombie_health;
		self.image = pygame.image.load('./images/Crazyzombie.gif')
		self.image = pygame.transform.scale(self.image,(127,148));
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();

		self.yard_row = randint(0,4);
		self.rect.centery = game_settings.squares["rows"][self.yard_row];
		# self.rect.bottom = bot_coords;
		self.rect.right = self.screen_rect.right;
		game_settings.zombie_in_row[self.yard_row] += 1;

		self.x = float(self.rect.x);

	def update_me(self):
		self.x -= self.speed * 1;
		# right now, zombies can only move on the x axis
		self.rect.x = self.x;

	def draw_me(self):
		self.screen.blit(self.image, self.rect);

	def hit(self, damage):
		self.health -= damage;

