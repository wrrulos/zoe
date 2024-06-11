import flet as ft

from ...constants import VERSION, GITHUB_URL

from easyjsonpy import get_config_value, set_config_value, set_language, translate_message


class AboutModal:
    def __init__(self, page: ft.Page):
        """
        Initialize the AboutModal with the given page.

        Args:
            page (ft.Page): The page object
        """

        self.page = page
        self.about_modal = ft.AlertDialog(
            title=ft.Text(
                value=translate_message(key='appBar.about.title')
            ),
            content=ft.Column([
                ft.Text(
                    value=translate_message(key='appBar.about.description')
                ),
                ft.Container(height=20),
                ft.Text(
                    value=translate_message(key='appBar.about.version')
                ),
                ft.Text(
                    value=VERSION
                ),
                ft.Container(height=20),
                ft.Text(
                    value=translate_message(key='appBar.about.sourceCode')
                ),
                ft.Text(
                    value=GITHUB_URL
                )
            ]),
            actions=[
                ft.TextButton(
                    text=translate_message(key='appBar.about.close'),
                    on_click=self.close_about_modal
                )
            ],
        )

    def open_about_modal(self, e: ft.ControlEvent) -> None:
        """
        Open the about modal.
        """

        self.page.dialog = self.about_modal
        self.about_modal.open = True
        self.page.update()

    def close_about_modal(self, e: ft.ControlEvent) -> None:
        """
        Close the about modal.
        """

        self.about_modal.open = False
        self.page.update()
