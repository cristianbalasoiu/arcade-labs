import arcade
from menu import MenuPrincipal

def main():
    # Crear ventana en pantalla completa
    window = arcade.Window(fullscreen=True, title="Juego")

    menu = MenuPrincipal()
    window.show_view(menu)

    arcade.run()

if __name__ == "__main__":
    main()