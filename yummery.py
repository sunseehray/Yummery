import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Yummery"
SCALING = 2.0

# Build a sandwich game

class Yummery(arcade.Window):
    """Build a sandwich game
    Player starts at the center, sandwich order pops up
    Player can move anywhere, but not off screen
    Player can hold up to two bread slices, and only one for each of the rest
    Player builds the bread to feed the monster within 30 seconds.
    If it feeds the wrong sandwich, the game ends.
    Player can discard sandwich in a bin to restart.
    Press ESC to exit game.
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)
        self.monster_list = arcade.SpriteList()
        self.ingredients_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

# Ingredients - Bread slice, cheese, lettuce, tomatoes, burger patty
# Server - movable object
# Goal of the game is to build a sandwich according to random directions

# Assets needed:
# Background image
# Background sound
# Sound effect stacking ingredients
# Sound effect for successful sandwich
# Sound effect for failed sandwich
# Final sandwich images
# Partial sandwich images
# Ingredient images
# Server image
# Garbage bin

# Build the MVP
# Sprite for player
# Y position is constant, only X changes left to right within bounds
# at certain X-positions, ingredients are placed
# If player presses enter on an x-position, he will fill his plate with the ingredient from that position
# Plate sprite updates with image of ingredient
# Ingredient can only be added once, no double patties, etc
# When player presses enter on the delivery counter, game verifies if correct order.
# If order is correct, plate becomes empty.
# If order is incorrect, error sound.
# If player presses enter on the garbage counter, sandwich is automatically destoryed, plate becomes empty.

# Maybe ingredients should have an index, so sandwich combos are like:
# 0 - bread
# 1 - burger patty
# 2 - cheese
# 3 - tomato
# 4 - lettuce

# 3 Combos for now - 012340, 010, 0120

# GAME ASSETS
# PLAYER SPRITE MOVEMENT
# INGREDIENTS
# SANDWICH BUILDING
# DELIVERY
# GARBAGE BIN
# DEBUG
# DEMO
# SOUND EFFECTS
# FINAL REPORT