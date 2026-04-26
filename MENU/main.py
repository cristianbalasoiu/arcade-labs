import arcade
from menu import MenuPrincipal

def main():
    window = arcade.Window(800, 600, title="Juego")

    menu = MenuPrincipal()
    window.show_view(menu)

    arcade.run()

if __name__ == "__main__":
    main()