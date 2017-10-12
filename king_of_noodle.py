import arcade
import arcade.key
import sys
from noodle import World#,Noodle,Water

SCREEN_WIDTH = 1191
SCREEN_HEIGHT = 670
W = False
N = False
S = False
I = False
B = False
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        self.ndworld = World(width,height)
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
        self.bg = arcade.Sprite('image/full.jpg')
        self.bg.set_position(width//2,height//2)
        self.bowl = arcade.Sprite('image/bowl.png',0.8)
        self.bowl.set_position(width-400,200)
        self.noodleS = arcade.Sprite('image/noodles2.png',0.8)
        self.noodleS.set_position(width-400,200)
        self.waterS = arcade.Sprite('image/water.png',0.8)
        self.waterS.set_position(width-400,200)
        self.boilS = arcade.Sprite('image/boil.png',0.8)
        self.boilS.set_position(width-400,200)
        self.sauceS = arcade.Sprite('image/saucess.png',0.8)
        self.sauceS.set_position(width-400,200)
        self.ingd = arcade.Sprite('image/ingredient.png',0.8)
        self.ingd.set_position(width-400,200)        
        
    def on_draw(self):
        global N,W,B,S,I
        if self.ndworld.outkey == 'n':
            N = True
        if self.ndworld.outkey == 'w':
            W = True
        if self.ndworld.outkey == 'b':
            B = True
        if self.ndworld.outkey == 's':
            S = True
        if self.ndworld.outkey == 'i':
            I = True
        if self.ndworld.outkey == 'esc':
            sys.exit()

        arcade.start_render()
        self.bg.draw()
        self.bowl.draw()
        if W:
            self.waterS.draw()
        if B:
            self.boilS.draw()
        if N:
            self.noodleS.draw()
        if S:
            self.sauceS.draw()
        if I:
            self.ingd.draw()
    def on_key_press(self, key, key_modifiers):
        self.ndworld.on_key_press(key, key_modifiers)
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
