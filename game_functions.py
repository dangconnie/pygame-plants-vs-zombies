import sys;
import pygame;
from plant import Plant;
from peashooter import Peashooter;
from bullet import Bullet;


def check_events(screen, game_settings, squares, plants, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# we're trying to find out the position of the green squares to make the squares clickable
			mouse_x, mouse_y = pygame.mouse.get_pos();
			# print mouse_x;
			# print mouse_y;
			for square in squares:
				if square.rect.collidepoint(mouse_x, mouse_y):
					# check for collisions
					print "Square: ", square.square_number;
					plants.add(Peashooter(screen, square));

def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick):
	screen.blit(background.image, background.rect);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();

	for plant in plants:
		plant.draw_me();
		# as long as plant is still alive. as long as there is a plant in the group
		# it would be in the group if the user clicked in the group
		if tick % 30 == 0:
			bullets.add(Bullet(screen,plant));

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();
