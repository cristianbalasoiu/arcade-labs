import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.CHARLESTON_GREEN)
    
    def on_draw(self):
        self.clear()
        
        

        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
