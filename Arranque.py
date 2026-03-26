"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self): # el constructor donde se inicializan los atributos

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

    def setup(self): #seccion donde va el codigo del juego
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self): #seccion donde va el codigo de los dibujos del juego
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear() #llamar al principio

        # Code to draw other things will go here


def main(): #cuando se ejecuta un programa se busca la funcion main()
    """Main function"""
    window = GameView() #se crea el objeto ventana haciendo la llamada al __init__
    window.setup() #se inicializa el codigo de la ventana
    arcade.run() #inicia el programa


if __name__ == "__main__": #si Python ejecuta directamente este archivo, entonces el valor de __name__ será "__main__", y se llamará a la función main().
    main()