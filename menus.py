import pygame
import window

class Background:
  def render(self, screen):
    screen.fill((100, 100, 255))
    logo_image = pygame.image.load('images/old_logo.png')
    logo_image = pygame.transform.scale(logo_image, (550, 450)).convert_alpha()
    screen.blit(logo_image, (window.window_size[0] - 450, window.window_size[1] - 325, 100, 100))


class MainMenu:

  def render(self, screen):
    pygame.draw.rect(screen, (100, 100, 100), (5, window.window_size[1] - 208, 170, 150))
    power_button_image = pygame.image.load('images/power_button.png')
    power_button_image = pygame.transform.scale(power_button_image, (200, 200))
    screen.blit(power_button_image, (-12, window.window_size[1] - 248, 100, 100))
