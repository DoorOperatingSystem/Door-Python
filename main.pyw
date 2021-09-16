import pygame
from pygame.constants import K_RSHIFT
import ui_features as ui
import menus as menu
import window
import button_detection
import system

pygame.init()
screen = window.create()

button_thing = button_detection.ButtonDetection()
taskbar = ui.TaskBar()
main_menu = menu.MainMenu()
background = menu.Background()

while system.running:
  for event in pygame.event.get():
    # Quit event
    if event.type == pygame.QUIT:
      system.running = False
    # Mouse click event
    if event.type == pygame.MOUSEBUTTONDOWN:
      button_thing.left_click(pygame.mouse.get_pos())
    if event.type == pygame.MOUSEMOTION:
      button_thing.mouse_hover(pygame.mouse.get_pos())
    if event.type == pygame.KEYDOWN:
      pressed_keys = pygame.key.get_pressed()
      if pressed_keys[K_RSHIFT]:
        if system.current_menu == "main menu":
          pass
        else:
          system.current_menu = "main menu"

  background.render(screen, True)

  # Draw window features
  taskbar.render(screen)

  if system.main_menu_open:
    main_menu.render(screen)

  # Flips the screen because for some reason it needs to do that to display stuff
  pygame.display.flip()

pygame.quit()
