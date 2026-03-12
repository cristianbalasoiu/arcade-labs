import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.CHARLESTON_GREEN)

        self.puntos = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(100)]

        self.x1_motor_cuerpo = 500
        self.x2_motor_cuerpo = 700
        self.y1_motor_cuerpo = 125
        self.y2_motor_cuerpo = 225

        self.x1_motor= 700
        self.x2_motor= 725
        self.y1_motor = 140
        self.y2_motor = 210

        self.x1_ventana= 600
        self.y1_ventana = 175
        
        self.x1_ventana_cristal= 600
        self.y1_ventana_cristal = 175

        self.x1_punta = 500
        self.y1_punta = 115
        self.x2_punta = 500
        self.y2_punta = 235
        self.x3_punta = 400
        self.y3_punta = 175

        self.x1_fuego1 = 725
        self.y1_fuego1 = 160
        self.x2_fuego1 = 750
        self.y2_fuego1 = 190

        self.x1_fuego2 = 725
        self.y1_fuego2 = 165
        self.x2_fuego2 = 745
        self.y2_fuego2 = 185

        self.x1_luna = 140
        self.y1_luna = 470 
        



    

    def on_draw(self):
        self.clear()

        #ESTRELLAS Y LUNA 
        arcade.draw_circle_filled(140, 470, 90, arcade.color.ASH_GREY)
        arcade.draw_points(self.puntos, arcade.color.WHITE, 2)
        #CUERPO DEL MOTOR
        arcade.draw_lrbt_rectangle_filled(self.x1_motor_cuerpo, self.x2_motor_cuerpo, self.y1_motor_cuerpo, self.y2_motor_cuerpo, arcade.color.GHOST_WHITE)
        #MOTOR
        arcade.draw_lrbt_rectangle_filled(self.x1_motor, self.x2_motor, self.y1_motor, self.y2_motor,arcade.color.DARK_JUNGLE_GREEN)
        #VENTANA
        arcade.draw_circle_filled(self.x1_ventana, self.y1_ventana, 35, arcade.color.DARK_LAVA)
        arcade.draw_circle_filled(self.x1_ventana_cristal, self.y1_ventana_cristal, 27, arcade.color.CELESTE)
        #PUNTA
        arcade.draw_triangle_filled(self.x1_punta, self.y1_punta, self.x2_punta, self.y2_punta, self.x3_punta, self.y3_punta, arcade.color.RED)
        #FUEGO DEL MOTOR
        arcade.draw_lrbt_rectangle_filled(self.x1_fuego1, self.x2_fuego1, self.y1_fuego1, self.y2_fuego1, arcade.color.ORANGE)
        arcade.draw_lrbt_rectangle_filled(self.x1_fuego2, self.x2_fuego2, self.y1_fuego2, self.y2_fuego2, arcade.color.GOLD)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):

        self.x1_motor_cuerpo += dx
        self.x2_motor_cuerpo += dx
        self.y1_motor_cuerpo += dy
        self.y2_motor_cuerpo += dy

        self.x1_motor += dx
        self.x2_motor += dx
        self.y1_motor += dy
        self.y2_motor += dy

        self.x1_ventana += dx
        self.y1_ventana += dy
        
        self.x1_ventana_cristal += dx
        self.y1_ventana_cristal += dy

        self.x1_punta += dx
        self.y1_punta += dy
        self.x2_punta += dx
        self.y2_punta += dy
        self.x3_punta += dx
        self.y3_punta += dy

        self.x1_fuego1 += dx
        self.y1_fuego1 += dy
        self.x2_fuego1 += dx
        self.y2_fuego1 += dy

        self.x1_fuego2 += dx
        self.y1_fuego2 += dy
        self.x2_fuego2 += dx
        self.y2_fuego2 += dy

        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
    