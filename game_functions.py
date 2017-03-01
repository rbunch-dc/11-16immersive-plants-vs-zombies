import sys;
import pygame;
from peashooter import Peashooter;
from gatling import Gatling;
from bullet import Bullet;
import time;

def check_events(screen, game_settings,squares,plants,bullets,icons):
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
					if(game_settings.chosen_plant == 1):
						plants.add(Peashooter(screen,square));
					elif(game_settings.chosen_plant == 2):
						plants.add(Gatling(screen,square));
			for icon in icons:
				if icon.rect.collidepoint(mouse_x,mouse_y):
					game_settings.chosen_plant = icon.slot
					print "You clicked: ",icon.image;
					# plants.add(Peashooter(screen,square));		
		elif event.type == pygame.MOUSEMOTION:
			# print event.pos
			for square in squares:
				if square.rect.collidepoint(event.pos):
					game_settings.highlighted_square = square;
					# print game_settings.highlighted_square;

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons):
	screen.blit(background.image, background.rect);

	for icon in icons:
		screen.blit(icon.image, icon.rect);


	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen, (255,215,0), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'],game_settings.squares['square_height']),5);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;

	for plant in plants:
		plant.draw_me();
		# print plant.yard_row;
		# if tick % 20 == 0:
		# is it time to shoot?
		should_shoot = time.time() - plant.last_shot > plant.shoot_speed
		# print time.time() - plant.last_shot;
		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
		if should_shoot and in_my_row:
			bullets.add(Bullet(screen,plant));
			plant.last_shot = time.time();

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();
