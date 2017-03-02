import pygame;
from settings import Settings;
from background import Background;
import game_functions as gf;
from pygame.sprite import Group, groupcollide
from zombie import Zombie;
from square import Square;
from plant_icon import Plant_Icon;

pygame.init();
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("DC PvZ clone");
background = Background(game_settings);
peashooter_icon = Plant_Icon(game_settings,'peashooter-icon.png',1);
gatling_icon = Plant_Icon(game_settings,'gatling-icon.png',2);
sunflower_icon = Plant_Icon(game_settings,'sunflower.png',3);
icons = [peashooter_icon,gatling_icon,sunflower_icon];

# All our groups
zombies = Group();
plants = Group();
squares = Group();
bullets = Group()

# Load up squares with our vars
for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen,game_settings,i, j));

def run_game():
	tick = 0;
	while 1:
		if game_settings.game_active:
			gf.check_events(screen,game_settings, squares, plants,bullets,icons);
			tick += 1;
			if tick % 30 == 0:
				zombies.add(Zombie(screen,game_settings));

			zombies_hit = groupcollide(zombies, bullets, False, False);
			# print zombies_hit;
			for zombie in zombies_hit:
				# print zombie;
				# print zombies_hit[zombie];
				if zombie.yard_row == zombies_hit[zombie][0].yard_row:
					# print "Same row!!!";
					bullets.remove(zombies_hit[zombie][0]);
					zombie.hit(1);
					if(zombie.health <= 0):
						zombies.remove(zombie);
						game_settings.zombie_in_row[zombie.yard_row] -= 1;
						game_settings.zombies_killed += 1;

		gf.update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons);		
		pygame.display.flip();



run_game();