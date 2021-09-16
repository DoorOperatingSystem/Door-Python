import pygame
import styling

class PowerButton:
  def render(self, screen, position):
    pygame.draw.circle(screen, styling.ICONS['main'],
                       position, 25)
    pygame.draw.circle(screen, styling.ICONS['menu wheel'],
                       position, 18)
    pygame.draw.line(screen, styling.ICONS['main'],
                     (position[0], position[1] - 20),
                     position,
                     7)
