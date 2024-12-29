import pygame

from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *
from shots import * 
# from buttons import *


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

    Shot.containers = (drawable, updatable, shots)

    font = pygame.font.Font(None, 36)  # None uses the default font, and 36 is the font size
    lives = 3
    dt = 0 # delta time - to track how much time has passed
    max_score = 0

    while True :
        while lives > 0 :
            player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            asteroidfield = AsteroidField()
            current_life =1
            score = 0
            while current_life > 0 :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                screen.fill((0,0,0))

                #score display
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color text
                screen.blit(score_text, (10, 10))
                lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))  # White color text
                screen.blit(lives_text, (10, 40))
                high_score_text = font.render(f"High score: {max_score}", True, (255, 255, 255))  # White color text
                screen.blit(high_score_text, (10, 70))


                for drawing in drawable :
                    drawing.draw(screen)
                pygame.display.flip()
                dt = clock.tick(60) /1000

                for object in updatable :
                    object.update(dt)

                # collision
                for asteroid in asteroids :
                    if asteroid.collision(player) : 
                        # print (f"Game over! Final score :{score}")
                        final_text = font.render(f"Final score: {score}", True, (255, 255, 255))  # White color text
                        screen.blit(final_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                        current_life -=1 
                        # return
                    for shot in shots :
                        if asteroid.collision(shot) :
                            shot.kill()
                            asteroid.split()
                            score+=asteroid.radius//20
            if score>max_score : max_score = score
            lives -=1
            for object in updatable :
                object.kill()
            
            # mouse_pos = pygame.mouse.get_pos()
            # if button_rect.collidepoint(mouse_pos):
            #     pygame.draw.rect(screen, button_hover_color, button_rect)  # Hover color
            # else:
            #     pygame.draw.rect(screen, button_color, button_rect)  # Normal color

            # # Draw button text
            # button_text = font.render("Restart", True, (255, 255, 255))  # White text
            # text_rect = button_text.get_rect(center=button_rect.center)  # Center the text
            # screen.blit(button_text, text_rect)
            # # button = pygame.Rect(button_x, button_y, button_width, button_height)
            # draw_button(screen)
        return    

 

if __name__ == "__main__":
    main()
