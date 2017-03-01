import sys;
import pygame;
# from plant import Plant;
from peashooter import Peashooter;
from bullet import Bullet;
# from pygame.sprite import groupcollide;

def check_events(screen, game_settings,squares,plants,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# we're trying to find out the position of the green squares to make the squares clickable
			mouse_x,mouse_y = pygame.mouse.get_pos();
			# print mouse_x;
			# print mouse_y;
			for square in squares:
				if square.rect.collidepoint(mouse_x,mouse_y):
					print "Square: ",square.square_number;
					plants.add(Peashooter(screen,square));
		elif event.type == pygame.MOUSEMOTION:
			# print event.pos;
			for square in squares:
				if square.rect.collidepoint(event.pos):
					# when a mouse moves on top of a square, it turns into a sprite
					game_settings.highlighted_square = square;
					# print game_settings.highlighted_square;	

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick):
	screen.blit(background.image, background.rect);

	if game_settings.highlighted_square != 0:
		# params for draw...
		# 1) where (the screen)
		# 2) color (tuple in rgb format)
		# 3) coords (tuple, left, top, width, height)
		# this will make a yellow box highlighting where you're clicking
		pygame.draw.rect(
			screen, 
			(255, 215,0), 
			(game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'], game_settings.squares['square_height']), 5
		);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();

	for plant in plants:
		plant.draw_me();
		# as long as plant is still alive. as long as there is a plant in the group
		# it would be in the group if the user clicked in the group
		# print yard_row;
		if tick % 20 == 0:
			if game_settings.zombie_in_row[plant.yard_row] > 0:
				bullets.add(Bullet(screen,plant));
				# only add a bullet to this plant if if there is a zombie in the current row, so we need to know the current row and the row the zombie is in

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();

