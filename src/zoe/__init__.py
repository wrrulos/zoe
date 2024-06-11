import flet as ft
import threading

from .app.app import main
from .utilities.lol.game_acceptor import GameAcceptor

from easyjsonpy import set_language, load_languages, load_configuration, get_config_value, set_config_value


class Zoe:
    def __init__(self):
        load_languages(
            [
                {'name': 'en', 'path': 'assets/languages/en.json'},
                {'name': 'es', 'path': 'assets/languages/es.json'},
                {'name': 'pt', 'path': 'assets/languages/pt.json'}
            ]
        )

        load_configuration('default', 'config.json')
        set_language(get_config_value('language'))

    def run(self):
        """
        Run the Zoe application.
        """

        # Create the game acceptor and start the acceptor thread
        game_acceptor: GameAcceptor = GameAcceptor()
        thread: threading.Thread = threading.Thread(target=game_acceptor.run_acceptor)
        thread.start()

        # Create the app
        ft.app(target=lambda p: main(p, game_acceptor=game_acceptor, game_acceptor_thread=thread), assets_dir='assets')
