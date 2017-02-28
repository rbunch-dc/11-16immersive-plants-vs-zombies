import sys;
import pygame;
from peashooter import Peashooter;

def check_events(screen, game_settings,squares,plants):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos();
			# print mouse_x;
			# print mouse_y;
			for square in squares:
				if square.rect.collidepoint(mouse_x,mouse_y):
					print "Square: ",square.square_number;
					plants.add(Peashooter(screen,square));

def update_screen(screen,game_settings,background,zombies,squares,plants):
	screen.blit(background.image, background.rect);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();

	for plant in plants:
		plant.draw_me();
