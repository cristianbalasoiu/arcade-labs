import arcade
from boton import Boton



class MenuPrincipal(arcade.View):

    def __init__(self):
        super().__init__()
        self.botones = []
        arcade.set_background_color(arcade.color.BLACK_LEATHER_JACKET)
        

    def on_show(self):

        ancho = 800
        alto = 600

        self.botones = [
            Boton(ancho/2 - 150, alto/2 + 50, 300, 60, "JUGAR"),
            Boton(ancho/2 - 150, alto/2 - 30, 300, 60, "HISTORIA"),
            Boton(ancho/2 - 150, alto/2 - 110, 300, 60, "AJUSTES"),
        ]

    def on_draw(self):
        self.clear()

        center_x = self.window.width / 2
        center_y = self.window.height / 2
        half_width = self.window.width * 0.30
        half_height = self.window.height * 0.06

        # Título
        arcade.draw_text(
            "MUNDO CAÍDO",
            self.window.width / 2,
            self.window.height - 150,
            arcade.color.VENETIAN_RED,
            70,
            anchor_x="center",
            font_name="Georgia"
        )

        # BOTÓN 1 (JUGAR)

        bottom1 = center_y + self.window.height * 0.02 - half_height
        top1 = center_y + self.window.height * 0.10 + half_height

    
        arcade.draw_lrbt_rectangle_filled(
        center_x - half_width,
        center_x + half_width,
        center_y + self.window.height * 0.02 - half_height,
        center_y + self.window.height * 0.10 + half_height,
        arcade.color.SMOKY_BLACK)

        arcade.draw_lrbt_rectangle_outline(center_x - half_width, center_x + half_width, bottom1, top1, arcade.color.VENETIAN_RED, 3)

        # BOTÓN 2 (HISTORIA)

        bottom2 = center_y - self.window.height * 0.16 - half_height
        top2 = center_y - self.window.height * 0.14 + half_height

        arcade.draw_lrbt_rectangle_filled(
        center_x - half_width,
        center_x + half_width,
        center_y - self.window.height * 0.16 - half_height,
        center_y - self.window.height * 0.14 + half_height,
        arcade.color.SMOKY_BLACK)

        arcade.draw_lrbt_rectangle_outline(center_x - half_width, center_x + half_width, bottom2, top2, arcade.color.VENETIAN_RED, 3)

        # BOTÓN 3 (AJUSTES)

        bottom3 = center_y - self.window.height * 0.35 - half_height
        top3 = center_y - self.window.height * 0.32 + half_height

        arcade.draw_lrbt_rectangle_filled(
        center_x - half_width,
        center_x + half_width,
        center_y - self.window.height * 0.35 - half_height,
        center_y - self.window.height * 0.32 + half_height,
        arcade.color.SMOKY_BLACK)

        arcade.draw_lrbt_rectangle_outline(center_x - half_width, center_x + half_width, bottom3, top3, arcade.color.VENETIAN_RED, 3)

        # TEXTO BOTÓN 1 (JUGAR)
        arcade.draw_text(
        "JUGAR",
        center_x,
        center_y + self.window.height * 0.06,  # centro del rectángulo 1
        arcade.color.GOLDENROD,
        font_size=50,
        anchor_x="center",
        anchor_y="center",
        font_name="Times New Roman")

        # TEXTO BOTÓN 2 (HISTORIA)
        arcade.draw_text(
        "HISTORIA",
        center_x,
        center_y - self.window.height * 0.15,  # centro del rectángulo 2
        arcade.color.GOLDENROD,
        font_size=30,
        anchor_x="center",
        anchor_y="center",
        font_name="Times New Roman")

        # TEXTO BOTÓN 3 (CONTROLES)
        arcade.draw_text(
        "CONTROLES",
        center_x,
        center_y - self.window.height * 0.335,  # centro del rectángulo 3
        arcade.color.GOLDENROD,
        font_size=30,
        anchor_x="center",
        anchor_y="center",
        font_name="Times New Roman")

        # Botones
        for boton in self.botones:
            boton.dibujar()

    def on_mouse_press(self, x, y, button, modifiers):
        for boton in self.botones:
            if boton.esta_pulsado(x, y):
                print(f"Has pulsado: {boton.texto}")