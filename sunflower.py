import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Sunflower(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 0;
		self.health = 5;
		self.image_file = 'images/sunflower.png';
		self.screen = screen;
		self.square = square;
		self.name = "sunflower";
		self.can_shoot = False;
		self.can_make_sun = True;
		self.last_sun = 0;
		self.sun_speed = 5;
		self.sun_cost = 50;
		super(Sunflower, self).__init__();

	def make_sun(self,game_settings):
		game_settings.total_sun += 25;