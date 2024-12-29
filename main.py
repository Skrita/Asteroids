import pygame

from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *
from shots import * 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    

    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (drawable, updatable, asteroids)
    
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Shot.containers = (drawable, updatable,shots)

    dt = 0 # delta time - to track how much time has passed
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for drawing in drawable :
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000
        for object in updatable :
            object.update(dt)
        # collision
        for asteroid in asteroids :
            if asteroid.collision(player) : 
                print ("Game over!")
                return

           
        

if __name__ == "__main__":
    main()
