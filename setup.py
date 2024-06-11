import sys

from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':  # Set base to Win32GUI if the platform is Windows
    base = 'Win32GUI'


class AppSettings:
    PYTHON_SCRIPT = './main.pyw'
    PRODUCT_NAME = 'Zoe'
    PRODUCT_VERSION = '1.0.3'
    COMPANY_NAME = 'Zoe'
    PRODUCT_DESCRIPTION = 'An open-source program to make life easier for League of Legends players'
    UPGRADE_CODE = '{2227b4ab-197e-4a33-966e-b6859122bea4}'
    AUTHOR_EMAIL = 'vegapedroagustin2004@gmail.com'
    COPYRIGHT = 'Copyright (C) 2024 cx_Freeze'
    ICON = './assets/icon.ico'


# Executable settings
executables = [
    Executable(
        script=AppSettings.PYTHON_SCRIPT,
        base=base,
        target_name='Zoe.exe',
        icon=AppSettings.ICON,
        copyright=AppSettings.COPYRIGHT,
        shortcut_name=AppSettings.PRODUCT_NAME,
    )
]


# cx_Freeze setup
setup(
    name=AppSettings.PRODUCT_NAME,
    version=AppSettings.PRODUCT_VERSION,
    description=AppSettings.PRODUCT_DESCRIPTION,
    executables=executables,
    options={
        'build_exe': {
            'packages': ['flet', 'easyjsonpy', 'pyautogui', 'PIL'],
            'includes': [],
            'include_files': [
                ('./assets/icon.ico', 'assets/icon.ico'),
                ('./config.json', 'config.json'),
                ('./assets/images/accept_button.png', 'assets/images/accept_button.png'),
                ('./assets/images/zoe-bw.jpg', 'assets/images/zoe-bw.jpg'),
                ('./assets/images/zoe-color.jpg', 'assets/images/zoe-color.jpg'),
                ('./assets/languages/en.json', 'assets/languages/en.json'),
                ('./assets/languages/es.json', 'assets/languages/es.json'),
                ('./assets/languages/pt.json', 'assets/languages/pt.json')
            ],
        },
        'bdist_msi': {
            'upgrade_code': f'{AppSettings.UPGRADE_CODE}',
            'add_to_path': False,
            'all_users': True,
            'initial_target_dir': r'[AppDataFolder]\%s' % AppSettings.COMPANY_NAME,
            'data': {
                'Shortcut': [
                    ('DesktopShortcut', 'DesktopFolder', AppSettings.PRODUCT_NAME, 'TARGETDIR', '[TARGETDIR]Zoe.exe', None, None, None, None, None, None, 'TARGETDIR'),
                    ("StartMenuShortcut", "StartMenuFolder", AppSettings.PRODUCT_NAME, "TARGETDIR", "[TARGETDIR]Zoe.exe", None, None, None, None, None, None, "TARGETDIR")
                ],
                "Icon": [
                    ('IconId', AppSettings.ICON),
                ],
            }
        }
    },
    author=AppSettings.COMPANY_NAME,
    author_email=AppSettings.AUTHOR_EMAIL,
)
