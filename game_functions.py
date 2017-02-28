
import sys;
import pygame;

def check_events(screen, game_settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def update_screen(screen,game_settings,background,zombies):
	screen.blit(background.image, background.rect);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();