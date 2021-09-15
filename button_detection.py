import system
import window

class ButtonDetection:
  open_dialogue = "none"

  def left_click(self, mouse_position, screen):
    if mouse_position[0] < 50 and mouse_position[1] > (window.window_size[1] - 50):
      self.open_dialogue = "main menu"

    elif self.open_dialogue == "main menu" and mouse_position[0] < 175 and mouse_position[0] > 5 and mouse_position[1] > (window.window_size[1] - 210) and mouse_position[1] < (window.window_size[1] - 60):
      #pygame.draw.rect(screen, (100, 100, 100), (5, window.window_size[1] - 308, 170, 150))
      print("Shutting down")
      #time.sleep(5)
      system.running = False

    else:
      self.open_dialogue = "none"
