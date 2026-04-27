import arcade
from boton import Boton

class MenuPrincipal(arcade.View):

    def __init__(self):
        super().__init__()
        self.botones = []
        arcade.set_background_color(arcade.color.DARK_RED)
        

    def on_show(self):

        ancho = self.window.width
        alto = self.window.height

        self.botones = [
            Boton(ancho/2 - 150, alto/2 + 50, 300, 60, "JUGAR"),
            Boton(ancho/2 - 150, alto/2 - 30, 300, 60, "HISTORIA"),
            Boton(ancho/2 - 150, alto/2 - 110, 300, 60, "AJUSTES"),
        ]

    def on_draw(self):
        self.clear()


        # Título
        arcade.draw_text(
            "MUNDO CAÍDO",
            self.window.width / 2,
            self.window.height - 150,
            arcade.color.WHITE,
            60,
            anchor_x="center",
            font_name="Arial"
        )

        # Botones
        for boton in self.botones:
            boton.dibujar()

    def on_mouse_press(self, x, y, button, modifiers):
        for boton in self.botones:
            if boton.esta_pulsado(x, y):
                print(f"Has pulsado: {boton.texto}")