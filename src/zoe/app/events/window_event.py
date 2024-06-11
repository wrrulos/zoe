import flet as ft
import threading

from ...utilities.lol.game_acceptor import GameAcceptor


def window_event(e: ft.ControlEvent, page: ft.Page) -> None:
    """
    Handles the window event.

    Args:
        e (ControlEvent): The window event
    """

    if e.data == 'close':
        page.game_acceptor.stop_acceptor()
        page.game_acceptor_thread.join()
        page.window_destroy()