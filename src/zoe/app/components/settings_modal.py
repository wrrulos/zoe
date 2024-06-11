import flet as ft

from easyjsonpy import get_config_value, set_config_value, set_language, translate_message


class SettingsModal:
    def __init__(self, page: ft.Page):
        """
        Initialize the SettingsModal with the given page.

        Args:
            page (ft.Page): The page object
        """

        self.page = page
        self.enable_porofessor_checkbox = self.create_porofessor_checkbox()
        self.region_dropdown = self.create_region_dropdown()
        self.username_textfield = self.create_username_textfield()
        self.tag_textfield = self.create_tag_textfield()
        self.row = self.create_row()
        self.advanced_settings_checkbox = self.create_advanced_settings_checkbox()
        self.search_image_confidence_textfield = self.create_search_image_confidence_textfield()
        self.search_interval_textfield = self.create_search_interval_textfield()
        self.language_dropdown = self.create_language_dropdown()

        self.settings_modal = ft.AlertDialog(
            title=ft.Text(
                value=translate_message(key='appBar.settings.title'),
                width=300
            ),
            content=ft.Column([
                self.enable_porofessor_checkbox,
                self.region_dropdown,
                self.row,
                self.advanced_settings_checkbox,
                self.search_image_confidence_textfield,
                self.search_interval_textfield,
                self.language_dropdown
            ]),
            actions=[
                ft.TextButton(
                    text=translate_message(key='appBar.settings.close'),
                    on_click=self.close_settings_modal
                )
            ],
        )

    def create_porofessor_checkbox(self) -> ft.Checkbox:
        """
        Create an porofessor checkbox.

        Returns:
            ft.Checkbox: The porofessor checkbox object
        """

        return ft.Checkbox(
            label=translate_message(key='appBar.settings.enablePorofessor'),
            value=get_config_value(key='enablePorofessor'),
            on_change=self.toggle_porofessor
        )

    def create_region_dropdown(self) -> ft.Dropdown:
        """
        Create a region dropdown.

        Returns:
            ft.Dropdown: The region dropdown object
        """

        return ft.Dropdown(
            label=translate_message(key='appBar.settings.region'),
            options=[
                ft.dropdown.Option(text='NA', key='na'),
                ft.dropdown.Option(text='EUW', key='euw'),
                ft.dropdown.Option(text='EUNE', key='eune'),
                ft.dropdown.Option(text='LAN', key='lan'),
                ft.dropdown.Option(text='LAS', key='las'),
                ft.dropdown.Option(text='KR', key='kr'),
                ft.dropdown.Option(text='JP', key='jp'),
                ft.dropdown.Option(text='OCE', key='oce'),
                ft.dropdown.Option(text='BR', key='br'),
                ft.dropdown.Option(text='TR', key='tr'),
                ft.dropdown.Option(text='RU', key='ru'),
            ],
            value=get_config_value(key='profile.region'),
            on_change=self.update_region,
            visible=self.enable_porofessor_checkbox.value
        )

    def create_username_textfield(self) -> ft.TextField:
        """
        Create a username textfield.

        Returns:
            ft.TextField: The username textfield object
        """

        return ft.TextField(
            label=translate_message(key='appBar.settings.username'),
            value=get_config_value(key='profile.username'),
            width=150,
            on_change=self.update_username,
            visible=self.enable_porofessor_checkbox.value
        )

    def create_tag_textfield(self) -> ft.TextField:
        """
        Create a tag textfield.

        Returns:
            ft.TextField: The tag textfield object
        """

        return ft.TextField(
            label=translate_message(key='appBar.settings.tag'),
            value=get_config_value(key='profile.tag'),
            width=100,
            on_change=self.validate_tag_input,
            visible=self.enable_porofessor_checkbox.value
        )

    def create_row(self) -> ft.Row:
        """
        Create a row.

        Returns:
            ft.Row: The row object
        """

        return ft.Row(
            controls=[
                self.username_textfield,
                self.tag_textfield
            ],
            visible=self.enable_porofessor_checkbox.value
        )

    def create_advanced_settings_checkbox(self) -> ft.Checkbox:
        """
        Create an advanced settings checkbox.

        Returns:
            ft.Checkbox: The advanced settings checkbox object
        """

        return ft.Checkbox(
            label=translate_message(key='appBar.settings.enableAdvancedSettings'),
            value=get_config_value(key='enableAdvancedSettings'),
            on_change=self.toggle_advanced_settings
        )

    def create_search_image_confidence_textfield(self) -> ft.TextField:
        """
        Create a search image confidence textfield.

        Returns:
            ft.TextField: The search image confidence textfield object
        """

        return ft.TextField(
            label=translate_message(key='appBar.settings.searchImageConfidence'),
            value=str(get_config_value(key='search.confidence')),
            on_change=self.validate_float_input,
            visible=self.advanced_settings_checkbox.value,
            keyboard_type=ft.KeyboardType.NUMBER
        )

    def create_search_interval_textfield(self) -> ft.TextField:
        """
        Create a search interval textfield.

        Returns:
            ft.TextField: The search interval textfield object
        """

        return ft.TextField(
            label=translate_message(key='appBar.settings.searchInterval'),
            value=str(get_config_value(key='search.interval')),  # Convierte el valor inicial a cadena
            on_change=self.validate_integer_input,
            visible=self.advanced_settings_checkbox.value,
            keyboard_type=ft.KeyboardType.NUMBER
        )

    def create_language_dropdown(self) -> ft.Dropdown:
        """
        Create a language dropdown.

        Returns:
            ft.Dropdown: The language dropdown object
        """

        return ft.Dropdown(
            label=translate_message(key='appBar.settings.language'),
            options=[
                ft.dropdown.Option(text='English', key='en'),
                ft.dropdown.Option(text='Spanish', key='es'),
                ft.dropdown.Option(text='Portuguese', key='pt'),
            ],
            value=get_config_value(key='language'),
            on_change=self.update_language
        )

    def validate_float_input(self, e: ft.ControlEvent) -> None:
        """
        Validate the input of the search image confidence textfield.

        Args:
            e (ft.ControlEvent): The event object
        """

        try:
            float(e.control.value)
            e.control.error_text = None
            set_config_value(key='search.confidence', value=e.control.value)

        except ValueError:
            e.control.error_text = translate_message(key='appBar.settings.enterValidFloat')

        e.control.update()

    def validate_integer_input(self, e: ft.ControlEvent) -> None:
        """
        Validate the input of the search interval textfield.

        Args:
            e (ft.ControlEvent): The event object
        """

        try:
            int(e.control.value)
            e.control.error_text = None
            self.update_search_interval(e)

        except ValueError:
            e.control.error_text = translate_message(key='appBar.settings.enterValidInteger')

        e.control.update()

    def validate_tag_input(self, e: ft.ControlEvent) -> None:
        """
        Validate the input of the tag textfield.

        Args:
            e (ft.ControlEvent): The event object
        """

        if len(e.control.value) == 0:
            e.control.border_color = 'red'
            e.control.update()
            return

        if e.control.value[0] != '#':
            e.control.border_color = 'red'
            e.control.update()
            return

        e.control.border_color = None
        e.control.update()
        self.update_tag(e)

    def toggle_porofessor(self, e: ft.ControlEvent) -> None:
        """
        Toggle the porofessor settings

        Args:
            e (ft.ControlEvent): The event object
        """

        self.region_dropdown.visible = self.enable_porofessor_checkbox.value
        self.username_textfield.visible = self.enable_porofessor_checkbox.value
        self.tag_textfield.visible = self.enable_porofessor_checkbox.value
        self.row.visible = self.enable_porofessor_checkbox.value
        set_config_value(key='enablePorofessor', value=self.enable_porofessor_checkbox.value)
        self.page.update()

    def toggle_advanced_settings(self, e: ft.ControlEvent) -> None:
        """
        Toggle the advanced settings

        Args:
            e (ft.ControlEvent): The event object
        """

        self.search_interval_textfield.visible = self.advanced_settings_checkbox.value
        self.search_image_confidence_textfield.visible = self.advanced_settings_checkbox.value
        set_config_value(key='enableAdvancedSettings', value=self.advanced_settings_checkbox.value)
        self.page.update()

    def update_region(self, e: ft.ControlEvent) -> None:
        """
        Change the region setting.

        Args:
            e (ft.ControlEvent): The event object
        """

        set_config_value(key='profile.region', value=e.control.value)

    def update_username(self, e: ft.ControlEvent) -> None:
        """
        Update the username setting.

        Args:
            e (ft.ControlEvent): The event object
        """

        if len(e.control.value) == 0:
            e.control.border_color = 'red'
            e.control.update()
            return

        e.control.border_color = None
        e.control.update()
        set_config_value(key='profile.username', value=e.control.value)

    def update_tag(self, e: ft.ControlEvent) -> None:
        """
        Update the tag setting.

        Args:
            e (ft.ControlEvent): The event object
        """

        set_config_value(key='profile.tag', value=e.control.value)

    def update_search_interval(self, e: ft.ControlEvent) -> None:
        """
        Update the search interval setting.

        Args:
            e (ft.ControlEvent): The event object
        """

        set_config_value(key='search.interval', value=e.control.value)

    def update_language(self, e: ft.ControlEvent) -> None:
        """
        Update the language setting.

        Args:
            e (ft.ControlEvent): The event object
        """

        set_language(e.control.value)
        set_config_value(key='language', value=e.control.value)
        self.page.update()

    def open_settings_modal(self, e: ft.ControlEvent) -> None:
        """
        Open the settings modal.

        Args:
            e (ft.ControlEvent): The event object
        """
        self.page.dialog = self.settings_modal
        self.settings_modal.open = True
        self.page.update()

    def close_settings_modal(self, e: ft.ControlEvent) -> None:
        """
        Close the settings modal.

        Args:
            e (ft.ControlEvent): The event object
        """
        self.settings_modal.open = False
        self.page.porofessor_button.visible = self.enable_porofessor_checkbox.value
        self.page.update_containers()
        self.page.update()
