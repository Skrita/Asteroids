from circleshape import *
from constants import *

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