import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	#grouping
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	playershots = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	Asteroid.containers = (asteroids, updatable,drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (playershots, updatable,drawable)
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	dt = 0
	asteroidfield = AsteroidField()

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for obj in updatable:
			obj.update(dt)
		for ast in asteroids:
			if player.collisions(ast):
				print("Game over!")
				exit()
			for bullet in playershots:
				if bullet.collisions(ast):
					bullet.kill()
					ast.split()
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		# 60 fps framerate
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
