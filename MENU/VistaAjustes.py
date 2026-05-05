import arcade

class VistaAjustes(arcade.View):

    def __init__(self):
        super().__init__()

        self.wasd_texture = arcade.load_texture("MENU/assets/wasd.png")

        self.wasd_x = self.window.width // 2
        self.wasd_y = 120

        self.scale = 0.5

    def on_draw(self):
        self.clear()
        arcade.draw_text("AJUSTES", 400, 300, arcade.color.WHITE, 40, anchor_x="center")

        width = self.wasd_texture.width * self.scale
        height = self.wasd_texture.height * self.scale

        arcade.draw_texture_rect(
        self.wasd_texture,
        arcade.XYWH(self.wasd_x, self.wasd_y, width, height))

        # BOTÓN VOLVER
        left = 20
        right = 200
        top = self.window.height - 20
        bottom = self.window.height - 80

        arcade.draw_lrbt_rectangle_filled(
            left, right, bottom, top,
            arcade.color.SMOKY_BLACK
        )

        arcade.draw_lrbt_rectangle_outline(
            left, right, bottom, top,
            arcade.color.RED, 3
        )

        arcade.draw_text(
            "VOLVER",
            (left + right) / 2,
            (bottom + top) / 2,
            arcade.color.GOLDENROD,
            25,
            anchor_x="center",
            anchor_y="center",
            font_name = "Times New Roman"
        )

    def on_mouse_press(self, x, y, button, modifiers):

        left = 20
        right = 200
        top = self.window.height - 20
        bottom = self.window.height - 80

        if left <= x <= right and bottom <= y <= top:
            from menu import MenuPrincipal
            self.window.show_view(MenuPrincipal())

    