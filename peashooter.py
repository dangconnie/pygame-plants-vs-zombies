# this will be a subclass of "plants". It's a child class! You're passing self.image_file to the parent file, plant.py
import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Peashooter(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 2;
		self.health = 5;
		self.image_file = 'images/peashooter.png';
		self.screen = screen;
		self.square = square;
		
		# super needs to be at the bottom
		super(Peashooter, self).__init__();