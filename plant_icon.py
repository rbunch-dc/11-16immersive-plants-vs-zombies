import pygame
from pygame.sprite import Sprite

class Plant_Icon(Sprite):
	def __init__(self,game_settings,icon,slot):
		super(Plant_Icon, self).__init__();		
		self.image = pygame.image.load('./images/'+icon);
		self.image = pygame.transform.scale(self.image,(40,40));
		self.rect = self.image.get_rect();
		self.rect.left = 300+(50 * slot);
		self.rect.top = 0;
		self.slot = slot;
