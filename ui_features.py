import pygame

import system
import window
import styling

class MenuButton:
  bar_size = 0
  animation_frame = 20
  start_position = window.window_size[1] - bar_size + 13
  start_speed = 1
  position = start_position
  acceleration = start_speed

  def render_background(self, screen):
    pygame.draw.circle(screen, styling.TASKBAR['shadow'],
                       (window.window_size[0] / 2 - 20, self.position - 50), 63)
    pygame.draw.circle(screen, styling.TASKBAR['border'],
                       (window.window_size[0] / 2 - 20, self.position - 50), 60)

  def render_foreground(self, screen):
    pygame.draw.circle(screen, styling.TASKBAR['menu wheel'],
                       (window.window_size[0] / 2 - 20, self.position - 50), 55)

    if system.menu_hovered == False:
      menu_button_image = pygame.image.load('images/old_menu_icon.png')
    elif system.menu_hovered == True:
      menu_button_image = pygame.image.load('images/icon.png')

    if system.current_menu == "main menu":
      menu_button_image = pygame.image.load('images/icon.png')

    menu_button_image = pygame.transform.scale(menu_button_image, (65, 65))
    screen.blit(menu_button_image,
                (window.window_size[0] / 2 - 52, self.position - 85, 10, 10))

    if system.current_menu == "main menu" and self.position >= (window.window_size[1] / 2 + 20):
      self.position -= self.acceleration
      if self.position >= (window.window_size[1] - 300):
        self.acceleration += 5
      elif self.position <= (window.window_size[1] / 2 + 150) and self.acceleration > 1:
        self.acceleration -= 5
      if self.acceleration < 1:
        self.acceleration = 1
    elif system.current_menu != "main menu":
      self.position = self.start_position
      self.acceleration = self.start_speed

    if not self.position >= (window.window_size[1] / 2 + 20):
      system.main_menu_open = True
    else:
      system.main_menu_open = False

class TaskBar:
  bar_size = 53
  menu_button = MenuButton()
  menu_button.bar_size = bar_size

  def render(self, screen):
    pygame.draw.rect(screen, styling.TASKBAR['shadow'],
                     (0, window.window_size[1] - self.bar_size - 3, window.window_size[0], 3))
    self.menu_button.render_background(screen)
    pygame.draw.rect(screen, styling.TASKBAR['border'],
                     (0, window.window_size[1] - self.bar_size, window.window_size[0], 5))
    pygame.draw.rect(screen, styling.TASKBAR['main'],
                     (0, window.window_size[1] - self.bar_size + 5, window.window_size[0], self.bar_size - 5))
    self.menu_button.render_foreground(screen)
