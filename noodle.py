import arcade.key
class World:
    def __init__(self,width,height):
        self.outkey = ''
        self.countboil = -1
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
#            self.outkey = 'b'        
            self.countboil += 1
            #print (self.countboil)
        elif key == arcade.key.LEFT:
            self.outkey = 'left'
        elif key == arcade.key.RIGHT:
            self.outkey = 'right'
        elif key == arcade.key.ENTER:
            self.outkey = 'enter'
        elif key == arcade.key.ESCAPE:
            self.outkey = 'esc'
        else:
            self.outkey = ''
    