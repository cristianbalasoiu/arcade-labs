import arcade
from boton import Boton

class MenuPrincipal(arcade.View):

    def __init__(self):
        super().__init__()

        # Cargar fondo
        self.fondo = arcade.load_texture("assets/fondos/fondo.png")

        # Botones
        self.botones = []

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

        ancho = self.window.width
        alto = self.window.height

        # Crear botones centrados
        self.botones = [
            Boton(ancho/2 - 150, alto/2 + 50, 300, 60, "JUGAR"),
            Boton(ancho/2 - 150, alto/2 - 30, 300, 60, "HISTORIA"),
            Boton(ancho/2 - 150, alto/2 - 110, 300, 60, "AJUSTES"),
        ]

    def on_draw(self):
        self.clear()

        # Dibujar fondo a pantalla completa
        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            self.window.width,
            self.window.height,
            self.fondo
        )

        # Oscurecer un poco (como en tu imagen)
        arcade.draw_lrtb_rectangle_filled(
            0, self.window.width,
            self.window.height, 0,
            (0, 0, 0, 120)
        )

        # Título
        arcade.draw_text(
            "MUNDO CAÍDO",
            self.window.width / 2,
            self.window.height - 150,
            arcade.color.WHITE,
            60,
            anchor_x="center"
        )

        # Dibujar botones
        for boton in self.botones:
            boton.dibujar()

    def on_mouse_press(self, x, y, button, modifiers):
        for boton in self.botones:
            if boton.esta_pulsado(x, y):
                print(f"Has pulsado: {boton.texto}")