import arcade.key
class World:
    def __init__(self,width,height):
        self.outkey = ''
    
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
        elif key == arcade.key.ESCAPE:
            self.outkey = 'esc'
        else:
            self.outkey = ''
    