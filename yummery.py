# Build a sandwich game
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