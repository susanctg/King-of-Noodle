import arcade.key
from random import randint
w = False
s = False
i = False
space = False
lr = False
sauce_amount = randint(1,5)
ingd_amount = randint(1,5)
add_sauce = 0
add_ingd = 0
print('s : ',sauce_amount)
print('i : ',ingd_amount)
#sauce_amount = 2
#ingd_amount = 3

class World:
    global add_ingd,add_sauce,sauce_amount,ingd_amount
    def __init__(self,width,height):
        #global add_ingd,add_sauce
        self.outkey = ''
        self.countboil = -1
        self.countstir = -1
        self.numsauce = sauce_amount
        self.numingd = ingd_amount
        self.addsauce = add_sauce
        self.addingd = add_ingd
        self.score = 0
    def check_score(self,s,i):
        self.score = 50
        if sauce_amount == s :
            self.score += 50
        if ingd_amount == i:
            self.score += 50
        #if self.remain_time >= 0:
        #    self.score += self.remain_time 
        print('sauce amount : ',sauce_amount)
        print('add sauce : ',s)
        print('ingd amount : ',ingd_amount)
        print('add ingd : ',i)

    def on_key_press(self,key,key_modifiers):
        global w,s,i,space,lr,add_sauce,add_ingd
        if key == arcade.key.N:
            self.outkey = 'n'
            w = True
        elif key == arcade.key.W and w:
            self.outkey = 'w'
            space = True
            s = True
        elif key == arcade.key.S and s and self.countboil >= 7:
            if add_sauce < 9:
                add_sauce += 1
            else:
                add_sauce = 9
            
        elif key == arcade.key.ENTER and s and self.countboil>=7:
            print("sauce : ",add_sauce)
            lr = True
            i = True
            self.outkey = 's'
            s = False
        elif key == arcade.key.I and i and self.countstir >= 7:
            if add_ingd < 9:
                add_ingd += 1
            else:
                add_ingd = 9
            
        elif key == arcade.key.ENTER and i and self.countstir>=7:
            print("ingd : ",add_ingd)
            self.outkey = 'i' 
            self.check_score(add_sauce,add_ingd)
   
        elif key == arcade.key.SPACE and space:       
            self.countboil += 1
        elif (key == arcade.key.LEFT or key == arcade.key.RIGHT) and lr:
            self.countstir += 1
        elif key == arcade.key.BACKSPACE:
            self.outkey = 'delete'
            w = False
            s = False
            i = False
            space = False
            lr = False
            add_ingd = 0
            add_sauce = 0
        elif key == arcade.key.ESCAPE:
            self.outkey = 'esc'
        else:
            self.outkey = ''
        self.addsauce = add_sauce
        self.addingd = add_ingd