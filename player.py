from circleshape import *
from constants import *
from shots import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cd = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "blue", self.triangle(),2)
    
    def rotate(self, dt):
        self.rotation+= PLAYER_TURN_SPEED*dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)    
        if keys[pygame.K_SPACE] and self.shoot_cd <= 0 :
            self.shoot()
        self.shoot_cd-=dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot=Shot(self.position.dot(pygame.Vector2(1,0)), self.position.dot(pygame.Vector2(0,1)))
        shot.velocity=pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
        self.shoot_cd = 0.3


