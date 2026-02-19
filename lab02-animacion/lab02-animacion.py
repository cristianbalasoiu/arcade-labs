import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.CHARLESTON_GREEN)
    
    def on_draw(self):
        self.clear()

        arcade.draw_circle_filled(140, 470, 90, arcade.color.ASH_GREY)
        for i in range (20):

            puntos += [(random.randint(0, 800), random.randint(0, 600))]

        arcade.draw_points(puntos, arcade.color.WHITE, 5)

        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
