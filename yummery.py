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

        # monster at top center
        self.monster_sprite = arcade.Sprite("images/monster.png", scale=0.6)
        self.monster_sprite.center_x = WINDOW_WIDTH/2
        self.monster_sprite.bottom = 450
        self.all_sprites.append(self.monster_sprite)

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

        # floating order near monster
        self.order_sprite = None

        # player sprite starts at the center
        self.player_sprite = arcade.Sprite("images/player.png")
        self.player_sprite.position = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
        self.all_sprites.append(self.player_sprite)
        
        # the sandwich being updated
        self.sandwich_sprite = arcade.SpriteList()
        # space between ingredients for the sandwich being built
        self.ingredient_height = 10
        
        # garbage bin at lower right
        self.garbage_sprite = arcade.Sprite("images/garbage.png")
        self.garbage_sprite.position = (500,50)
        self.all_sprites.append(self.garbage_sprite)

        # sandwich code list
        self.sandwich_code = []

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
        self.sandwich_sprite.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        sandwich_x = self.player_sprite.center_x + 5
        sandwich_y = self.player_sprite.center_y

        for index, ingredient in enumerate(self.sandwich_sprite):
            ingredient.center_x = sandwich_x # off-center
            ingredient.center_y = sandwich_y + index * self.ingredient_height # stacking up

        self.all_sprites.update()

        if self.player_sprite.top > WINDOW_HEIGHT:
            self.player_sprite.top = WINDOW_HEIGHT
        if self.player_sprite.right > WINDOW_WIDTH:
            self.player_sprite.right = WINDOW_WIDTH
        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.Q:
            # Quit
            arcade.close_window()

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        
        if key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        if key == arcade.key.ENTER:
            if self.player_sprite.collides_with_sprite(self.monster_sprite) == True:
                print("Sandwich delivered?")
                self.reset_sandwich()
            if self.player_sprite.collides_with_sprite(self.bread_sprite) == True:
                self.add_ingredient("images/bread.png", 0)
            if self.player_sprite.collides_with_sprite(self.patty_sprite) == True:
                self.add_ingredient("images/patty.png", 1)
            if self.player_sprite.collides_with_sprite(self.cheese_sprite) == True:
                self.add_ingredient("images/cheese.png", 2)
            if self.player_sprite.collides_with_sprite(self.lettuce_sprite) == True:
                self.add_ingredient("images/lettuce.png", 3)
            if self.player_sprite.collides_with_sprite(self.tomato_sprite) == True:
                self.add_ingredient("images/tomato.png", 4)
            if self.player_sprite.collides_with_sprite(self.garbage_sprite) == True:
                self.reset_sandwich()
        pass


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """

        if (
            key == arcade.key.UP
            or key == arcade.key.DOWN
            
        ):
            self.player_sprite.change_y = 0

        if (
            key == arcade.key.LEFT
            or key == arcade.key.RIGHT
        ):
            self.player_sprite.change_x = 0

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

    def monster_order():
        """
        Random orders for a sandwich
        """
        pass

    def is_sandwich_matched(self):
        """
        Check to see if the sandwich delivered is the sandwich ordered
        """
        pass

    def add_ingredient(self, ingredient_texture, code):
        """
        Add ingredient to sandwich
        """
        ingredient = arcade.Sprite(
            ingredient_texture, 
            scale=0.5,
            center_x = self.player_sprite.center_x + 5, 
            center_y = self.player_sprite.center_y
        )
        self.sandwich_sprite.append(ingredient)
        self.sandwich_code.append(code)
        print(self.sandwich_code)
    
    def reset_sandwich(self):
        """
        reset sandwich
        """
        self.sandwich_sprite.clear()
        self.sandwich_code = []

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
# NOTES
# 3 Combos for now - 010, 0120, 012340

# TO DO
# GAME ASSETS - done
# PLAYER SPRITE MOVEMENT - done
# INGREDIENTS - done
# SANDWICH BUILDING - done
# DELIVERY
# GARBAGE BIN - done
# DEBUG
# DEMO
# SOUND EFFECTS
# FINAL REPORT