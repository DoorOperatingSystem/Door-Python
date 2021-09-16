import window

ERROR = [
  (0, 0),
  (5, 5)
]

MAIN_MENU_BUTTON = [
  (window.window_size[0] / 2 - 75, window.window_size[1] - 90),
  (window.window_size[0] / 2 + 40, window.window_size[1])
]

POWER_BUTTON = [
  (window.window_size[0] / 2 - 194, window.window_size[1] / 2 - 80),
  (window.window_size[0] / 2 - 95, window.window_size[1] / 2 - 4)
]

def detect_collision(colliding, collider):
  if colliding[0] > collider[0][0] and colliding[0] < collider[1][0] and colliding[1] > collider[0][1] and colliding[1] < collider[1][1]:
    return True
  else:
    return False
