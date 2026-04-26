import arcade

class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.texto = texto

    def dibujar(self):
        # Fondo del botón
        arcade.draw_lrtb_rectangle_filled(
            self.x,
            self.x + self.ancho,
            self.y + self.alto,
            self.y,
            (0, 0, 0, 200)
        )

        # Borde rojo
        arcade.draw_lrtb_rectangle_outline(
            self.x,
            self.x + self.ancho,
            self.y + self.alto,
            self.y,
            arcade.color.RED,
            2
        )

        # Texto centrado
        arcade.draw_text(
            self.texto,
            self.x + self.ancho / 2,
            self.y + self.alto / 2,
            arcade.color.WHITE,
            20,
            anchor_x="center",
            anchor_y="center"
        )

    def esta_pulsado(self, x, y):
        return (
            self.x <= x <= self.x + self.ancho and
            self.y <= y <= self.y + self.alto
        )