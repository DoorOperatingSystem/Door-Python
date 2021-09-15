import pygame
import ui_features as ui
import menus as menu
import window
import button_detection
import system

pygame.init()
screen = window.create()

button_thing = button_detection.ButtonDetection()
taskbar = ui.TaskBar()
power_options = menu.PowerMenu()
background = menu.Background()

while system.running:
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            system.running = False
        # Mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_thing.left_click(pygame.mouse.get_pos(), screen)
    
    background.render(screen)

    # Draw window features
    taskbar.render(screen)

    if button_thing.open_dialouge == "power menu":
        power_options.render(screen)

    # Flips the screen because for some reason it needs to to that to display stuff
    pygame.display.flip()

pygame.quit()