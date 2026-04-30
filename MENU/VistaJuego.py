import arcade

class VistaJuego(arcade.View):
    def on_draw(self):
        self.clear()
        arcade.draw_text("JUEGO", 400, 300, arcade.color.WHITE, 40, anchor_x="center")