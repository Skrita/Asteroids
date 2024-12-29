from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius)

    def update(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # self.position += forward * self.velocity *dt
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS : return
        random_angle = random.uniform(20,50)
        
        babyast1=Asteroid(self.position.dot(pygame.Vector2(1,0)), self.position.dot(pygame.Vector2(0,1)), self.radius - ASTEROID_MIN_RADIUS)
        babyast1.velocity=self.velocity.rotate(random_angle)*1.2
        babyast2=Asteroid(self.position.dot(pygame.Vector2(1,0)), self.position.dot(pygame.Vector2(0,1)), self.radius - ASTEROID_MIN_RADIUS)
        babyast2.velocity=self.velocity.rotate(-random_angle)*1.2