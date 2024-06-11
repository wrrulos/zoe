import flet as ft
import webbrowser

from ...constants import ZOE_IMAGE_COLOR_PATH, ZOE_IMAGE_BW_PATH, GITHUB_URL, DISCORD_URL, YOUTUBE_URL
from ..components.settings_modal import SettingsModal
from ..components.about_modal import AboutModal

from easyjsonpy import get_config_value, translate_message


class Home:
    def __init__(self, page: ft.Page):
        """
        Initialize the Home page with the given page.

        Args:
            page (ft.Page): The page object
        """

        self.page = page

        # Page settings
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER

        # Load settings modal
        self.image_path: str = ZOE_IMAGE_BW_PATH
        self.settings_modal: SettingsModal = SettingsModal(self.page)
        self.about_modal: AboutModal = AboutModal(self.page)

        # UI components
        self.page.appbar = self.create_app_bar()
        self.circle_container = self.create_circular_container()
        self.acceptor_switch = self.create_switch_button()
        self.page.porofessor_button = self.create_porofessor_button()
        self.button_row = self.create_button_row()
        self.page.container1 = ft.Container(height=0)  # Default height
        self.page.container2 = ft.Container(height=0)  # Default height
        self.page.update_containers = self.update_containers

        self.page.add(
            ft.Column(
                controls=[
                    ft.Container(height=50),
                    self.circle_container,
                    ft.Container(height=30),
                    self.acceptor_switch,
                    self.page.container1,
                    self.page.porofessor_button,
                    self.page.container2,
                    self.button_row
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        self.page.update()

    def create_app_bar(self) -> ft.AppBar:
        """
        Creates the app bar with menu items.

        Returns:
            ft.AppBar: The app bar object
        """

        return ft.AppBar(
            leading=ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text=translate_message(key='appBar.settings.title'), on_click=self.settings_modal.open_settings_modal),
                    ft.PopupMenuItem(text=translate_message(key='appBar.about.title'), on_click=self.about_modal.open_about_modal)
                ]
            )
        )

    def create_circular_container(self) -> ft.Container:
        """
        Creates a circular container with an image.

        Returns:
            ft.Container: The container object
        """
        self.image_container: ft.Container = ft.Container(
            content=ft.Image(src=self.image_path, fit=ft.ImageFit.COVER),
            width=200,
            height=200,
            border_radius=100,
            clip_behavior=ft.ClipBehavior.HARD_EDGE
        )
        return self.image_container

    def create_switch_button(self) -> ft.Switch:
        """
        Creates a switch button.

        Returns:
            ft.Switch: The switch button object
        """

        return ft.Switch(
            value=False,
            on_change=self.switch_game_acceptor_state,
            active_color=ft.colors.GREEN,
            thumb_color=ft.colors.WHITE
        )

    def create_porofessor_button(self) -> ft.ElevatedButton:
        """
        Creates a button to enable the name exploit.

        Returns:
            ft.Button: The button object
        """

        return ft.ElevatedButton(
            text=translate_message(key='porofessorButton'),
            on_click=self.open_porofessor,
            visible=get_config_value('enablePorofessor')
        )

    def create_button_row(self) -> ft.Row:
        """
        Creates a row of buttons for GitHub, Discord, and YouTube.

        Returns:
            ft.Row: The row object
        """

        github_button: ft.IconButton = ft.IconButton(
            icon=ft.icons.WEB,
            icon_size=30,
            on_click=lambda e: self.page.launch_url(GITHUB_URL),
            icon_color=ft.colors.PINK_100
        )

        discord_button: ft.IconButton = ft.IconButton(
            icon=ft.icons.DISCORD,
            icon_size=30,
            on_click=lambda e: self.page.launch_url(DISCORD_URL),
            icon_color=ft.colors.BLUE_100
        )

        youtube_button: ft.IconButton = ft.IconButton(
            icon=ft.icons.VIDEO_STABLE,
            icon_size=30,
            on_click=lambda e: self.page.launch_url(YOUTUBE_URL),
            icon_color=ft.colors.RED_100
        )

        return ft.Row(
            controls=[github_button, discord_button, youtube_button],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def open_porofessor(self, e: ft.ControlEvent) -> None:
        """
        Opens the Porofessor website in the default browser.

        Args:
            e (ft.ControlEvent): The event object
        """

        url: str = f'https://porofessor.gg/live/{get_config_value("profile.region")}/{get_config_value("profile.username")}{get_config_value("profile.tag").replace("#", "-")}'
        webbrowser.open(url)

    def switch_game_acceptor_state(self, e: ft.ControlEvent):
        """
        Switches the image when the switch button is toggled.

        Args:
            e (ft.ControlEvent): The switch event
        """

        self.page.game_acceptor.searching = True if e.data == 'true' else False
        self.image_path = ZOE_IMAGE_COLOR_PATH if e.data == 'true' else ZOE_IMAGE_BW_PATH
        self.image_container.content = ft.Image(src=self.image_path, fit=ft.ImageFit.COVER)
        self.page.update()

    def update_containers(self) -> None:
        """
        Update the containers with the correct height based on the Porofessor button visibility.
        """

        container1_height: int = 5 if get_config_value('enablePorofessor') else 30
        container2_height: int = 25 if get_config_value('enablePorofessor') else 0
        self.page.container1.height = container1_height
        self.page.container2.height = container2_height
