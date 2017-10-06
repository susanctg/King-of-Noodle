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
        self.bg = arcade.Sprite('image/kitchen.png')
        self.bg.set_position(width//2,height//2)
        self.title = arcade.Sprite('image/kon_6.png')
        self.title.set_position(width-400,height-85)
        self.bowl = arcade.Sprite('image/bowl.png',0.65)
        self.bowl.set_position(width-400,250)
        self.noodleS = arcade.Sprite('image/noodles2.png',0.65)
        self.noodleS.set_position(width-400,250)
        self.waterS = arcade.Sprite('image/water.png',0.65)
        self.waterS.set_position(width-400,250)
        self.boilS = arcade.Sprite('image/boil.png',0.65)
        self.boilS.set_position(width-400,250)
        
        
    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.title.draw()
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
