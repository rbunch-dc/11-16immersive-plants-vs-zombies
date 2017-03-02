# import pygame;
import pyjsdl as pygame

from pygame.sprite import Sprite;
from plant import Plant;

class Gatling(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 1;
		self.health = 6;
		self.image_file = 'images/Gatling_Pea_Fixed.png';
		self.screen = screen;
		self.square = square;
		self.name = "gatling";
		self.can_shoot = True;
		self.can_make_sun = False;
		self.sun_speed = 0;

		super(Gatling, self).__init__();