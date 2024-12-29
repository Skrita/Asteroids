import pygame
from constants import *

font = pygame.font.Font(None, 36)
def draw_button(screen):
        # Change color if hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        if button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button)
        else:
            pygame.draw.rect(screen, button_color, button)

        # Render and draw the button text
        button_text = font.render("Restart", True, button_text_color)
        text_rect = button_text.get_rect(center=button.center)
        screen.blit(button_text, text_rect)