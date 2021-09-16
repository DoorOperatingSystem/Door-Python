import system
import window
import collision

class ButtonDetection:
  def left_click(self, mouse_position):
    print("mouse clicked at: " + str(mouse_position))
    if collision.detect_collision(mouse_position, collision.MAIN_MENU_BUTTON):
      system.current_menu = "main menu"

    elif system.current_menu == "main menu" and collision.detect_collision(mouse_position, collision.POWER_BUTTON):
      #pygame.draw.rect(screen, (100, 100, 100), (5, window.window_size[1] - 308, 170, 150))
      print("Shutting down")
      #time.sleep(5)
      system.running = False

    else:
      system.current_menu = "none"

  def mouse_hover(self, mouse_position):
    if collision.detect_collision(mouse_position, collision.MAIN_MENU_BUTTON):
      system.menu_hovered = True
    else:
      system.menu_hovered = False
