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

		# square stuff
		self.squares = {
			"start_left": 367,
			"start_top": 246,
			"square_width": 110,
			"square_height": 105,
			"rows":[
				245,
				350,
				455, 
				560, 
				665
			]
		}

