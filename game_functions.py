import sys;
import pygame;
from peashooter import Peashooter;
from gatling import Gatling;
from sunflower import Sunflower
from bullet import Bullet;
import time;

def check_events(screen, game_settings,squares,plants,bullets,icons):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if game_settings.game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				# we're trying to find out the position of the green squares to make the squares clickable
				mouse_x,mouse_y = pygame.mouse.get_pos();
				# print mouse_x;
				# print mouse_y;
				for square in squares:
					if square.rect.collidepoint(mouse_x,mouse_y):
						# determine which square was clicked
						print "Square: ",square.square_number;
						if (game_settings.chosen_plant == 1):
							# chosen_plant 1 in icon was clicked, add a Peashooter to that square
							plants.add(Peashooter(screen, square));
						elif (game_settings.chosen_plant == 2):
							# chosen_plant 2 in icon was clicked, add a Gatling to that square
							plants.add(Gatling(screen, square));
						elif (game_settings.chosen_plant == 3):
							# chosen_plant 3 in icon was clicked, add a sunflower to that square
							plants.add(Sunflower(screen, square));

				for icon in icons:
					# determine which plant icon was clicked
					if icon.rect.collidepoint(mouse_x,mouse_y):
						game_settings.chosen_plant = icon.slot
						# print "You clicked: ",icon.image;
			elif event.type == pygame.MOUSEMOTION:
				# print event.pos;
				for square in squares:
					if square.rect.collidepoint(event.pos):
						# when a mouse moves on top of a square, it turns into a sprite
						game_settings.highlighted_square = square;
						# print game_settings.highlighted_square;	

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick, icons):

	screen.blit(background.image, background.rect);

	for icon in icons:
		screen.blit(icon.image, icon.rect);

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
		# only update the zombie's location if the game isn't over
		if game_settings.game_active:
			zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			# if the left side of the zombie reaches the left side of the screen, game is stopped
			game_settings.game_active = False;
			zombie.moving = True;

	for plant in plants:
		plant.draw_me();
		# as long as plant is still alive. as long as there is a plant in the group
		# it would be in the group if the user clicked in the group
		# print yard_row;

		# there needs to be a delay in the plants shooting
		should_shoot = time.time() - plant.last_shot > plant.shoot_speed;
		# print time.time() - plant.last_shot;
		# if tick % 20 == 0:
		can_shoot = plant.can_shoot;
		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0;
		if should_shoot and can_shoot and in_my_row:
			bullets.add(Bullet(screen,plant));
			# only add a bullet to this plant if if there is a zombie in the current row AND it is time to shoot, so we need to know the current row and the row the zombie is in
			plant.last_shot = time.time();
		can_make_sun = plant.can_make_sun;
		should_make_sun = (time.time() - plant.last_sun) > plant.sun_speed;
		if can_make_sun and should_make_sun:
			plant.make_sun(game_settings);
			plant.last_sun = time.time();

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();


	score_font = pygame.font.SysFont("monospace", 36);
	# Rendering a font takes 3 params: 
	# 1) What text
	# 2)
	# 3) color
	score_render = score_font.render("Zombies killed: " + str(game_settings.zombies_killed), 1, (255, 215,0));
	screen.blit(score_render, (100, 100));


	# let's make it 50px below the zombies killed score keep
	sun_render = score_font.render("Collected Sun: " + str(game_settings.total_sun), 1, (255, 215,0));
	screen.blit(sun_render, (100, 150));