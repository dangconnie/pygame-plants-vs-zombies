import pygame;

class Settings():
	def __init__(self):
		# Set the screen_size dynamically. This will automatically make the game the size of our screen.
		# display_info checks size of screen
		display_info = pygame.display.Info();
		self.screen_size = (display_info.current_w, display_info.current_h);
		self.bg_color = (82,111,53);
		self.zombie_speed = 5;
		self.zombie_health = 5;
		self.game_active = True;
		self.chosen_plant = 1;
		self.zombies_killed = 0;
		self.total_sun = 50;

		# square stuff
		self.squares = {
			"start_left": 330,
			"start_top": 220,
			"square_width": 99,
			"square_height": 91,
			"rows":[
				220,
				311,
				402, 
				493, 
				584
			]
		};
		self.highlighted_square = 0;
		# there are no zombies in any row at the beginning
		self.zombie_in_row = [
			0,
			0,
			0,
			0,
			0
		];
		self.plant_list = [
			'Peashooter',
			'Gatling',
			'Sunflower'
		]

