import arcade
from menu import MenuPrincipal

ANCHO = 800
ALTURA = 600

def main():
    window = arcade.Window(ANCHO, ALTURA, title= "MUNDO CAIDO")

    menu = MenuPrincipal()
    window.show_view(menu)

    arcade.run()

if __name__ == "__main__":
    main()