import arcade

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Yummery"

PLAYER_MOVEMENT_SPEED = 10

# Build a sandwich game
# template taken from https://api.arcade.academy/en/latest/example_code/starting_template.html#starting-template

class GameView(arcade.View):
    """
    Main application class
    """
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

        # If you have sprite lists, you should create them here,
        self.all_sprites = arcade.SpriteList()

        self.monster_sprite = arcade.Sprite("images/monster.png", scale=0.6)
        self.monster_sprite.center_x = WINDOW_WIDTH/2
        self.monster_sprite.bottom = 450
        self.all_sprites.append(self.monster_sprite)

        self.player_sprite = arcade.Sprite("images/player.png")
        self.player_sprite.position = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
        self.all_sprites.append(self.player_sprite)

        self.sandwich_sprite = None
        
        self.garbage_sprite = arcade.Sprite("images/garbage.png")
        self.garbage_sprite.position = (500,50)
        self.all_sprites.append(self.garbage_sprite)

        self.bread_sprite = arcade.Sprite("images/bread.png")
        self.bread_sprite.position = (70,400)
        self.all_sprites.append(self.bread_sprite)

        self.patty_sprite = arcade.Sprite("images/patty.png")
        self.patty_sprite.position = (70, 250)
        self.all_sprites.append(self.patty_sprite)

        self.cheese_sprite = arcade.Sprite("images/cheese.png")
        self.cheese_sprite.position = (70, 100)
        self.all_sprites.append(self.cheese_sprite)

        self.tomato_sprite = arcade.Sprite("images/tomato.png")
        self.tomato_sprite.position = (530, 400)
        self.all_sprites.append(self.tomato_sprite)

        self.lettuce_sprite = arcade.Sprite("images/lettuce.png")
        self.lettuce_sprite.position = (530, 250)
        self.all_sprites.append(self.lettuce_sprite)
        
        self.order_sprite = None
    
        # and set them to None


    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.all_sprites.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
    
    
######


    # Set up the ingredient locations
    # Maybe use collisions for triggering when player approaches HITBOX of ingredient, MONSTER for feeding
    # BIN for resetting

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

# 3 Combos for now - 010, 0120, 012340

# TO DO
# GAME ASSETS - done
# PLAYER SPRITE MOVEMENT
# INGREDIENTS
# SANDWICH BUILDING
# DELIVERY
# GARBAGE BIN
# DEBUG
# DEMO
# SOUND EFFECTS
# FINAL REPORT