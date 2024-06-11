import flet as ft
import threading

from functools import partial
from .pages.home import Home
from .components.settings_modal import SettingsModal
from .events.window_event import window_event
from ..utilities.lol.game_acceptor import GameAcceptor
from ..utilities.icon.set_icon import Icon


class ZoeApp:
    def __init__(self, page: ft.Page, game_acceptor: GameAcceptor, game_acceptor_thread: threading.Thread):
        """
        Initialize the ZoeApp with the given page.

        Args:
            page (ft.Page): The page object
        """
        #! Add languae updated without restart app in the future
        self.page = page
        Icon.set_icon('assets/icon.ico')  # Set the icon of the window

        # App settings
        self.page.title = 'Zoe v1.0.3'
        self.page.window_width = 550
        self.page.window_height = 650
        self.page.window_icon = 'assets/images/zoe-bw.jpg'
        self.page.window_prevent_close = True  # Prevent the window from closing by default
        self.page.window_resizable = False

        # Add game acceptor to the page object
        self.page.game_acceptor = game_acceptor
        self.page.game_acceptor_thread = game_acceptor_thread

        # Window event
        self.page.on_window_event = partial(window_event, page=self.page)

        # Set dark mode
        self.page.theme_mode = ft.ThemeMode.DARK
        # Load home page
        self.home = Home(self.page)


def main(page: ft.Page, game_acceptor_thread: threading.Thread, game_acceptor: GameAcceptor):
    """
    Main function to create the ZoeApp.

    Args:
        page (ft.Page): The page object
    """

    app = ZoeApp(page, game_acceptor=game_acceptor, game_acceptor_thread=game_acceptor_thread)
