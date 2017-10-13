import arcade.key
w = False
s = False
i = False
space = False
lr = False
class World:
    def __init__(self,width,height):
        self.outkey = ''
        self.countboil = -1
        self.countstir = -1
    def update(self,delta):
        self.ship.update(delta)
    
    def on_key_press(self,key,key_modifiers):
        global w,s,i,space,lr
        if key == arcade.key.N:
            self.outkey = 'n'
            w = True
        elif key == arcade.key.W and w:
            self.outkey = 'w'
            space = True
            s = True
        elif key == arcade.key.S and s:
            self.outkey = 's'
            lr = True
            i = True
        elif key == arcade.key.I and i:
            self.outkey = 'i'
        elif key == arcade.key.SPACE and space:       
            self.countboil += 1
        elif key == arcade.key.LEFT and lr:
            self.countstir += 1
        elif key == arcade.key.RIGHT and lr:
            self.countstir += 1
        elif key == arcade.key.BACKSPACE:
            self.outkey = 'delete'
            w = False
            s = False
            i = False
            space = False
            lr = False
        elif key == arcade.key.ESCAPE:
            self.outkey = 'esc'
        else:
            self.outkey = ''
    