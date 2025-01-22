import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position+=(self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randomangle = random.uniform(20,50)
        vel1 = self.velocity.rotate(randomangle)
        vel2 = self.velocity.rotate(-randomangle)
        smallasteroidr = self.radius - ASTEROID_MIN_RADIUS
        newobj1 = Asteroid(self.position.x,self.position.y,smallasteroidr)
        newobj2 = Asteroid(self.position.x,self.position.y,smallasteroidr)
        newobj1.velocity= vel1 * 1.2
        newobj2.velocity= vel2 * 1.2