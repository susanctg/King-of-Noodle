import arcade.key
'''
class Noodle:
    def __init__(self,world, x, y):
        self.x = x
        self.y = y

class Water:
    def __init__(self,world, wx, wy):
        self.wx = wx
        self.wy = wy

class sauce:
    def __init__(self,world, sx, sy):
        self.sx = sx
        self.sy = sy

'''
class World:
    def __init__(self,width,height):
        self.outkey = ''
#        self.width = width
#        self.height = height
#        self.noodle = Noodle(self,100,100)
#        self.water = Water(self,100,100)
    
    def update(self,delta):
        self.ship.update(delta)
    
    def on_key_press(self,key,key_modifiers):
        if key == arcade.key.N:
            self.outkey = 'n'
        elif key == arcade.key.W:
            self.outkey = 'w'
        elif key == arcade.key.S:
            self.outkey = 's'
        elif key == arcade.key.I:
            self.outkey = 'i'
        elif key == arcade.key.SPACE:
            self.outkey = 'b'
        elif key == arcade.key.ENTER:
            self.outkey = 'enter'
        else:
            self.outkey = ''
    