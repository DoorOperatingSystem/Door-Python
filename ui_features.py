import pygame
import window

class TaskBar:
  bar_size = 53

  def render(self, screen):
    pygame.draw.rect(screen, (128, 128, 135), (0, window.window_size[1] - self.bar_size, window.window_size[0], self.bar_size))
    pygame.draw.rect(screen, (90, 90, 90), (0, window.window_size[1] - self.bar_size, window.window_size[0], 5))

    menu_button = MenuButton()
    menu_button.render(screen, self.bar_size)

class MenuButton:
  def render(self, screen, bar_size):
    menu_button_image = pygame.image.load('images/old_menu_icon.png')
    screen.blit(menu_button_image, (-4, window.window_size[1] - (bar_size - 4), 10, 10))
