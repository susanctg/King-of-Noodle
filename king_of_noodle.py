import arcade
 
SCREEN_WIDTH = 1191
SCREEN_HEIGHT = 670

class SpaceGameWindow(arcade.Window):

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.title.draw()

    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)

        self.bg = arcade.Sprite('image/kitchen.png')
        self.bg.set_position(width//2,height//2)
        self.title = arcade.Sprite('image/kon_6.png')
        self.title.set_position(width-400,height-85)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
