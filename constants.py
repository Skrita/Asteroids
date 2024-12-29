SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
# ASTEROID_SPEED = 100

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500

button_width, button_height = 150, 50
button_y = SCREEN_HEIGHT - 100  # Place near the bottom
button_color = (0, 128, 255)  # Blue
button_hover_color = (0, 200, 255)
button_text_color = (255, 255, 255)
button_x = (SCREEN_WIDTH - button_width) // 2  # Center horizontally