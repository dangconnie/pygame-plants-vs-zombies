import pygame;
from settings import Settings;
import sys;
from background import Background;
import game_functions as gf;
from pygame.sprite import Group, groupcollide;
from zombie import Zombie;
from square import Square;

# def init_vars():
pygame.init();
# create game_settings object
game_settings = Settings();
# create screen object
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption ("DC Plants vs. Zombies Clone");
background = Background(game_settings);

# All our groups
zombies = Group();
plants = Group();
squares = Group();
bullets = Group();

# load up squares with our vars
# we have 5 rows 
for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen, game_settings, i, j));

def run_game():
	tick = 0;
	while 1:
		gf.check_events(screen, game_settings);
		gf.update_screen(screen, game_settings, background, zombies);
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()
		# screen.fill(game_settings.bg_color);
		tick += 1;
		if tick % 30 == 0:
			zombies.add(Zombie(screen, game_settings.zombie_speed, game_settings.zombie_health));
		pygame.display.flip();

# init_vars();
run_game();