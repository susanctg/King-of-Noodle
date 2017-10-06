import arcade
import arcade.key
from noodle import World#,Noodle,Water

SCREEN_WIDTH = 1191
SCREEN_HEIGHT = 670

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        self.ndworld = World(width,height)
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
        self.bg = arcade.Sprite('image/full.jpg')
        self.bg.set_position(width//2,height//2)
        self.bowl = arcade.Sprite('image/bowl.png',0.8)
        self.bowl.set_position(width-400,200)
        self.noodleS = arcade.Sprite('image/noodles.png',0.8)
        self.noodleS.set_position(width-400,200)
        self.waterS = arcade.Sprite('image/water.png',0.8)
        self.waterS.set_position(width-400,200)
        self.boilS = arcade.Sprite('image/boil.png',0.8)
        self.boilS.set_position(width-400,200)
        
        
    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.bowl.draw()
        if(self.ndworld.outkey == 'n'):
            self.noodleS.draw()
        if(self.ndworld.outkey == 'w'):
            self.waterS.draw()
        if(self.ndworld.outkey == 'b'):
            self.boilS.draw()
        
    def on_key_press(self, key, key_modifiers):
        self.ndworld.on_key_press(key, key_modifiers)
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
