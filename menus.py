import random
import pygame
import styling
import system
import window
import icons

class Background:
  def render(self, screen, is_colour):
    if is_colour:
      screen.fill(styling.BACKGROUNDS['moron'])
    logo_image = pygame.image.load('images/old_logo.png')
    logo_image = pygame.transform.scale(logo_image, (550, 450))
    screen.blit(logo_image, (window.window_size[0] - 450, window.window_size[1] - 325, 100, 100))

class ErrorMenu:
  def render(self, screen):
    screen.fill((0, 0, 0))
    error_message = system.FONTS['header italic'].render("ERROR", 1, (255, 255, 255))
    screen.blit(error_message, (window.window_size[0] / 2 - 175, window.window_size[1] / 2 - 100))
    error_message = system.FONTS['paragraph'].render("try again?", 1, (255, 255, 255))
    screen.blit(error_message, (window.window_size[0] / 2 - 175, window.window_size[1] / 2 + 5))
    error_message = system.FONTS['small paragraph'].render("error code: #" + str(random.randrange(1, 9999999999999999999999999)), 1, (255, 255, 255))
    screen.blit(error_message, (window.window_size[0] / 2 - 150, window.window_size[1] / 2 + 50))

class MainMenu:
  power_icon = icons.PowerButton()

  def render(self, screen):
    pygame.draw.rect(screen, styling.TASKBAR['border'],
                     (window.window_size[0] / 2 - 195, window.window_size[1] / 2 - 79, 100, 75))
    pygame.draw.rect(screen, styling.TASKBAR['menu wheel'],
                     (window.window_size[0] / 2 - 190, window.window_size[1] / 2 - 74, 88, 65))

    self.power_icon.render(screen, (window.window_size[0] / 2 - 145, window.window_size[1] / 2 - 41))
