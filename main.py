
import pygame;
from settings import Settings;
from background import Background;
import game_functions as gf;
from pygame.sprite import Group, groupcollide
from zombie import Zombie;
from square import Square;
from plant_icon import Plant_Icon;

# def init_vars():
pygame.init();
# create game_settings object
game_settings = Settings();
# create screen object
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption ("DC Plants vs. Zombies Clone");
background = Background(game_settings);
peashooter_icon = Plant_Icon(game_settings,'peashooter-icon.png',1);
gatling_icon = Plant_Icon(game_settings,'gatling-icon.png',2);
sunflower_icon = Plant_Icon(game_settings,'sunflower.png',3);
icons = [peashooter_icon,gatling_icon,sunflower_icon];
# All our groups
zombies = Group();
plants = Group();
squares = Group();
bullets = Group();

# plants.add(Plant(screen));

# load up squares with our vars
# we have 5 rows 
for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen,game_settings,i, j));

def run_game():
	tick = 0;
	while 1:
		gf.check_events(screen, game_settings, squares, plants,bullets, icons);
		if game_settings.game_active:
			# for event in pygame.event.get():
			# 	if event.type == pygame.QUIT:
			# 		sys.exit()
			# screen.fill(game_settings.bg_color);
			tick += 1;
			if tick % 30 == 0:
				zombies.add(Zombie(screen,game_settings));
			# for plant in plants:
			# 	plant.draw_me();

			zombies_hit = groupcollide(zombies, bullets, False, False);
			# we might collide with a zombie but we don't want to remove the bullet unless we're sure that that zombie is in our row. As a result, we changed the last arg to false.
			# check to see when zombies hit a bullet. zombies_hit is a dictionary (hence bracket notation). zombie itself is a key.
			# print zombies_hit;
			for zombie in zombies_hit:
				# look at which zombies are hit. in the beginning, zombies_hit is an empty dictionary. you would print of zombies_hit sprite objects.
				# print zombie;
				# print zombies_hit[zombie];
				if zombie.yard_row == zombies_hit[zombie][0].yard_row:
					print "Same row!";
					bullets.remove(zombies_hit[zombie][0]);
				zombie.hit(1);
				# take 1 damage point
				if (zombie.health <= 0):
					zombies.remove(zombie);
					# when zombies die, remove them
					game_settings.zombie_in_row[zombie.yard_row] -= 1;
					game_settings.zombies_killed += 1;	
		gf.update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons);
		pygame.display.flip();

# init_vars();
run_game();