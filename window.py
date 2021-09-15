import pygame
pygame.init()

pc_info = pygame.display.Info()
window_size = [pc_info.current_w, pc_info.current_h]

# Creates the OS screen
def create():
    #screen = pygame.display.set_mode(window_size)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # Set the window name
    pygame.display.set_caption('DoorOS')
    # Sets the window icon
    icon = pygame.image.load('images/icon.jpg')
    pygame.display.set_icon(icon)

    return screen