import arcade
import arcade.key
import sys
from random import randint
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
timetostir = False

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
        self.soup = arcade.Sprite('image/stir_sauce.png',0.8)
        self.soup.set_position(width-400,200)
        
        #bar
        self.ndbar = arcade.Sprite('image/noodle_bar.png',0.8)
        self.ndbar.set_position(width-400,480)
        self.waterbar = arcade.Sprite('image/water_bar.png',0.8)
        self.waterbar.set_position(width-400,480)
        self.saucebar = arcade.Sprite('image/sauce_bar.png',0.8)
        self.saucebar.set_position(width-400,480)
        self.ingdbar = arcade.Sprite('image/ingd_bar.png',0.8)
        self.ingdbar.set_position(width-400,480)
        self.donebar = arcade.Sprite('image/done_bar.png',0.8)
        self.donebar.set_position(width-400,480)
        self.boil = arcade.Sprite('image/boil_bar.png',0.8)
        self.boil.set_position(width-400,480)
        self.stir = arcade.Sprite('image/stir_bar.png',0.8)
        self.stir.set_position(width-400,480)        
        #block
        self.block = arcade.Sprite('image/block1.png',0.8)  
        #key
        self.r = arcade.Sprite('image/right.png',0.2)
        self.r.set_position(block_x+35,block_y-75)      
        self.l = arcade.Sprite('image/left.png',0.2)
        self.l.set_position(block_x-35,block_y-75)      
        self.spb = arcade.Sprite('image/space.png',0.8)
        self.spb.set_position(block_x,block_y)     

        self.num = []
        self.num.append(arcade.Sprite('image/one.png',0.8))
        self.num.append(arcade.Sprite('image/two.png',0.8))
        self.num.append(arcade.Sprite('image/three.png',0.8))
        self.num.append(arcade.Sprite('image/four.png',0.8))
        self.num.append(arcade.Sprite('image/five.png',0.8))

    def addblock(self,num):
        i = num
        j = 0
        while j <= i and i < 7:
            self.block.set_position(block_x+(j*48),block_y)
            self.block.draw()
            j += 1        

    def on_draw(self):
        global N,W,B,S,I,timetoboil,timetostir
        #block = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7]

        if self.ndworld.outkey == 'n':
            N = True
        if self.ndworld.outkey == 'w':
            W = True
            timetoboil = True 
        if self.ndworld.outkey == 's':
            timetostir = True
        if self.ndworld.outkey == 'i':
            I = True
        if self.ndworld.outkey == 'delete':
            W = False
            N = False
            S = False
            I = False
            timetoboil = False
            timetostir = False
            self.ndworld.countboil = -1
            self.ndworld.countstir = -1                
        if self.ndworld.outkey == 'esc':
            sys.exit()
        
        #start render
        arcade.start_render()
        self.bg.draw()
        self.bowl.draw()
        self.ndbar.draw()

        x = self.num[self.ndworld.numsauce-1]
        x.set_position(225,124)
        x.draw()

        y = self.num[self.ndworld.numingd-1]
        y.set_position(225,58)
        y.draw()
    
        if N:
            self.waterbar.draw()
        if W:
            self.saucebar.draw()
            self.waterS.draw()

        if S:
            self.soup.draw()
            self.ingdbar.draw()

        if timetoboil and self.ndworld.countboil<7:
            self.boil.draw()
            self.spb.draw()
            self.addblock(self.ndworld.countboil)
            
        if N:
            self.noodleS.draw()    

        if timetostir and self.ndworld.countstir<7:
            self.stir.draw()
            self.l.draw()
            self.r.draw()
            self.sauceS.draw()
            self.addblock(self.ndworld.countstir)
        elif timetostir:
            S = True

        if I:
            self.ingd.draw()
            self.donebar.draw()
        
    def on_key_press(self, key, key_modifiers):
        self.ndworld.on_key_press(key, key_modifiers)
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
