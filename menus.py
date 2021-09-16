import pygame
import styling
import window

class Background:
  def render(self, screen, is_colour):
    if is_colour:
      screen.fill(styling.BACKGROUNDS['moron'])
    logo_image = pygame.image.load('images/old_logo.png')
    logo_image = pygame.transform.scale(logo_image, (550, 450))
    screen.blit(logo_image, (window.window_size[0] - 450, window.window_size[1] - 325, 100, 100))


class MainMenu:
  def render(self, screen):
    pygame.draw.rect(screen, styling.TASKBAR['border'],
                     (window.window_size[0] / 2 - 195, window.window_size[1] / 2 - 79, 100, 75))
    pygame.draw.rect(screen, styling.TASKBAR['menu wheel'],
                     (window.window_size[0] / 2 - 190, window.window_size[1] / 2 - 74, 88, 65))
    #power_button_image = pygame.image.load('images/power_button.png')
    #power_button_image = pygame.transform.scale(power_button_image, (200, 200))
    #screen.blit(power_button_image,
    #            (-12, window.window_size[1] - 248, 100, 100))
