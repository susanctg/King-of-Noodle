import arcade
import arcade.key
import sys
from noodle import World

SCREEN_WIDTH = 1191
SCREEN_HEIGHT = 670
block_x = SCREEN_WIDTH - 400
block_y = 480
W = False
N = False
S = False
I = False
timetoboil = False
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        global block_x,block_y
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
        self.sauceS = arcade.Sprite('image/saucess.png',0.8)
        self.sauceS.set_position(width-400,200)
        self.ingd = arcade.Sprite('image/ingredient.png',0.8)
        self.ingd.set_position(width-400,200)

        self.boil = arcade.Sprite('image/boil_bar.png',0.8)
        self.boil.set_position(width-400,480)

        self.b1 = arcade.Sprite('image/block1.png',0.8)
        self.b1.set_position(block_x,block_y)      
        self.b2 = arcade.Sprite('image/block2.png',0.8)
        self.b2.set_position(block_x,block_y)      
        self.b3 = arcade.Sprite('image/block3.png',0.8)
        self.b3.set_position(block_x,block_y)      
        self.b4 = arcade.Sprite('image/block4.png',0.8)
        self.b4.set_position(block_x,block_y)      
        self.b5 = arcade.Sprite('image/block5.png',0.8)
        self.b5.set_position(block_x,block_y)      
        self.b6 = arcade.Sprite('image/block6.png',0.8)
        self.b6.set_position(block_x,block_y)      
        self.b7 = arcade.Sprite('image/block7.png',0.8)
        self.b7.set_position(block_x,block_y)      
          
        
    def on_draw(self):
        global N,W,B,S,I,timetoboil,block_x,block_y
        block = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7]
        i=1
        if self.ndworld.outkey == 'n':
            N = True
        if self.ndworld.outkey == 'w':
            W = True
            timetoboil = True
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
        if timetoboil and self.ndworld.countboil<7:
            self.boil.draw()
            if self.ndworld.countboil>=0:
                block[self.ndworld.countboil].draw()
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
