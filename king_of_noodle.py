import arcade

screen_w = 1280
screen_h = 1080
class SpaceGameWindow(arcade.Window):
    def init(self,screen_w,creen_h):
        super.init(screen_w,screen_h)
        arcade.set_background_color(arcade.color.WHITE)


def main():
    window = SpaceGameWindow(screen_w,screen_h)
    arcade.run()

main()
