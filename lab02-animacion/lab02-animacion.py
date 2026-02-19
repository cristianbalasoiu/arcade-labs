import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.CHARLESTON_GREEN)

        self.puntos = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(100)]
    
    def on_draw(self):
        self.clear()

        #ESTRELLAS Y LUNA 
        arcade.draw_circle_filled(140, 470, 90, arcade.color.ASH_GREY)
        arcade.draw_points(self.puntos, arcade.color.WHITE, 2)
        #CUERPO DEL MOTOR
        arcade.draw_lrbt_rectangle_filled(500, 700, 125, 225, arcade.color.GHOST_WHITE)
        #MOTOR
        arcade.draw_lrbt_rectangle_filled(700, 725, 140, 210,arcade.color.DARK_JUNGLE_GREEN)
        #VENTANA
        arcade.draw_circle_filled(600, 175, 35, arcade.color.DARK_LAVA)
        arcade.draw_circle_filled(600, 175, 27, arcade.color.CELESTE)
        #PUNTA
        arcade.draw_triangle_filled(500, 115, 500, 235, 400, 175, arcade.color.RED)
        #FUEGO DEL MOTOR
        arcade.draw_lrbt_rectangle_filled(725, 750, 160, 190, arcade.color.ORANGE)
        arcade.draw_lrbt_rectangle_filled(725, 745, 165, 185, arcade.color.GOLD)

        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
