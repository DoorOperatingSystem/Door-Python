import pygame
from pygame.constants import K_RSHIFT, K_ESCAPE
import menus
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
error_menu = menus.ErrorMenu()

while system.running:
  for event in pygame.event.get():
    # Quit event
    if event.type == pygame.QUIT:
      system.running = False
    # Mouse click event
    if event.type == pygame.MOUSEBUTTONDOWN:
      button_thing.left_click(pygame.mouse.get_pos(), screen)
    if event.type == pygame.MOUSEMOTION:
      button_thing.mouse_hover(pygame.mouse.get_pos())
    if event.type == pygame.KEYDOWN:
      pressed_keys = pygame.key.get_pressed()
      if pressed_keys[K_RSHIFT]:
        if system.current_menu != "error":
          if system.current_menu == "main menu":
            system.current_menu = "none"
          else:
            system.current_menu = "main menu"
      elif pressed_keys[K_ESCAPE]:
        system.running = False

  background.render(screen, True)

  # Draw window features
  taskbar.render(screen)

  if system.current_menu == "error":
    error_menu.render(screen)

  if system.show_error_restart_message:
    restart_message = system.FONTS['small paragraph'].render("(press 'esc' to shutdown the OS)", 1, (255, 255, 255))
    screen.blit(restart_message, (1, 1))

  if system.main_menu_open:
    main_menu.render(screen)

  # Flips the screen because for some reason it needs to do that to display stuff
  pygame.display.flip()

pygame.quit()
