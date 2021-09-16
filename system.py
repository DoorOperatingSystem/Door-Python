import pygame

pygame.font.init()

FONTS = {
  "header italic": pygame.font.Font("fonts/Rubik-BoldItalic.ttf", 100),
  "header 1": pygame.font.Font("fonts/Rubik-Bold.ttf", 100),
  "header 2": pygame.font.Font("fonts/Rubik-Bold.ttf", 85),
  "header 3": pygame.font.Font("fonts/Rubik-Bold.ttf", 75),
  "header 4": pygame.font.Font("fonts/Rubik-Bold.ttf", 50),
  "paragraph": pygame.font.Font("fonts/Rubik-Bold.ttf", 20),
  "small paragraph": pygame.font.Font("fonts/Rubik-Bold.ttf", 13),
}

running = True
current_menu = "none"
menu_hovered = False
main_menu_open = False
show_error_restart_message = False
