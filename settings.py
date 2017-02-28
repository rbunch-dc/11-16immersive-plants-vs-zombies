import pygame;

class Settings():
	def __init__(self):
		# Set the screen size dynamically
		display_info = pygame.display.Info();
		self.screen_size = (display_info.current_w, display_info.current_h);
		self.bg_color = (82,111,53);
		self.zombie_speed = 5;
		self.zombie_health = 5;
		# square stuff
		self.squares = {
			"start_left": 367,
			"start_top": 245,
			"square_width": 110,
			"square_height": 105,
			"rows": [
				245,
				350,
				455,
				560,
				665
			]
		}