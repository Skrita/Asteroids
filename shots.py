from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # self.velocity = PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow",self.position,self.radius)

    def update(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # self.position += forward * self.velocity *dt
        self.position += self.velocity *dt