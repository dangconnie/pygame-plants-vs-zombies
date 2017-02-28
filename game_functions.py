import sys;
import pygame;

def check_events(screen, game_settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# we're trying to find out the position of the green squares to make the squares clickable
			mouse_x, mouse_y = pygame.mouse.get_pos();
			print mouse_x;
			print mouse_y;

def update_screen(screen, game_settings, background, zombies):
	screen.blit(background.image, background.rect);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();
