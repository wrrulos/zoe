import time
import pyautogui

from typing import Union

from pyscreeze import Box
from easyjsonpy import get_config_value
from ...constants import DEFAULT_SEARCH_INTERVAL


class GameAcceptor:
    def __init__(self) -> None:
        self.searching: bool = False

    def run_acceptor(self) -> None:
        """
        Run the game acceptor.
        """

        while True:
            try:
                time.sleep(int(get_config_value(key='search.interval')))

            except ValueError:
                time.sleep(DEFAULT_SEARCH_INTERVAL)

            if self.searching == 'stop':
                break

            if not self.searching:
                continue

            accept_button: Union[Box, None] = self.search_accept_button()

            if accept_button is None:
                continue

            pyautogui.click(pyautogui.center(accept_button))

    def stop_acceptor(self) -> None:
        """
        Stop the game acceptor.
        """

        self.searching = 'stop'

    def search_accept_button(self) -> Union[Box, None]:
        """
        Search for the accept button on the screen.

        Returns:
            Union[Box, None]: The accept button box or None
        """

        try:
            image: Box = pyautogui.locateOnScreen(image=get_config_value(key='search.imagePath'), confidence=get_config_value(key='search.confidence'))

        except pyautogui.ImageNotFoundException:
            return None

        return image
