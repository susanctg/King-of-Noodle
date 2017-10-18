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
timetosauce = False

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
        #num
        self.num = []
        self.num.append(arcade.Sprite('image/zero.png',1))
        self.num.append(arcade.Sprite('image/one.png',0.8))
        self.num.append(arcade.Sprite('image/two.png',0.8))
        self.num.append(arcade.Sprite('image/three.png',0.8))
        self.num.append(arcade.Sprite('image/four.png',0.8))
        self.num.append(arcade.Sprite('image/five.png',0.8))
        self.num.append(arcade.Sprite('image/six.png',1))
        self.num.append(arcade.Sprite('image/seven.png',1))
        self.num.append(arcade.Sprite('image/eight.png',1))
        self.num.append(arcade.Sprite('image/nine.png',1))

        self.x = arcade.Sprite('image/x.png',0.8)
        self.total_time = 0
        self.time = [0,0]

    def update(self,delta_time):
        self.total_time += (delta_time)%60
        print(int(self.total_time))
        self.time[0] = int(self.total_time%100)//10
        self.time[1] = int(self.total_time)%10
        print(self.time[0])
        print(self.time[1])
    def addblock(self,num):
        i = num
        j = 0
        while j <= i and i < 7:
            self.block.set_position(block_x+(j*48),block_y)
            self.block.draw()
            j += 1        

    def on_draw(self):
        global N,W,B,S,I,timetoboil,timetostir,timetosauce
        
        if self.ndworld.outkey == 'n':
            N = True
        if self.ndworld.outkey == 'w':
            W = True
            timetoboil = True 
        if self.ndworld.outkey == 's':
        #    W = False
            timetosauce = False
            timetostir = True
        #    print(timetosauce)
        if self.ndworld.outkey == 'i':
            I = True
        if self.ndworld.outkey == 'delete':
            W = False
            N = False
            S = False
            I = False
            timetoboil = False
            timetostir = False
            timetosauce = False
            self.ndworld.countboil = -1
            self.ndworld.countstir = -1                
        if self.ndworld.outkey == 'esc':
            sys.exit()
        #start render
        arcade.start_render()
        self.bg.draw()
        self.bowl.draw()
        self.ndbar.draw()

        s_num = self.num[self.ndworld.numsauce]
        s_num.set_position(225,124)
        s_num.draw()

        i_num = self.num[self.ndworld.numingd]
        i_num.set_position(225,58)
        i_num.draw()

        posx = 300
        posy = 205
        
        a_s_num = self.num[self.ndworld.addsauce]
        a_s_num.set_position(posx+50,posy+95)
        a_s_num.draw()

        a_i_num = self.num[self.ndworld.addingd]
        a_i_num.set_position(posx+50,posy)
        a_i_num.draw()
        
        
        x_1 = self.x
        x_1.set_position(posx,posy)
        x_1.draw()

        x_2 = self.x
        x_2.set_position(posx,posy+95)
        x_2.draw()

        time_1 = self.num[self.time[0]]
        time_1.set_position(300,500)
        time_1.draw()


        time_2 = self.num[self.time[1]]
        time_2.set_position(350,500)
        time_2.draw()

        if N:
            self.waterbar.draw()
        if W:
            self.waterS.draw()
            if not timetostir:
                timetosauce = True

        if S:
            self.soup.draw()
            if not I:
                self.ingdbar.draw()

        if timetoboil and self.ndworld.countboil<7:
            self.boil.draw()
           # self.spb.draw()
            self.addblock(self.ndworld.countboil)
        elif self.ndworld.countboil>=7 and timetosauce:
        #    print(timetosauce)
            self.saucebar.draw()
            
        if N:
            self.noodleS.draw()    

        if timetostir and self.ndworld.countstir<7:
            self.stir.draw()
            #self.l.draw()
            #self.r.draw()
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
