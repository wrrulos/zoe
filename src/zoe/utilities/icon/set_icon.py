
import ctypes
import os


class Icon:
    @staticmethod
    def set_icon(icon_path: str):
        """
        Set the icon of the current window.

        Args:
            icon_path (str): The path to the icon file.
        """

        app_id: str = 'com.wrrulos.zoe'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        icon_path: str = os.path.abspath(icon_path)
        user32: ctypes.WinDLL = ctypes.WinDLL("user32")
        hwnd: int = user32.GetForegroundWindow()
        icon_small: int = 0
        icon_big: int = 1
        wm_seticon: int = 0x0080
        lr_loadfromfile: int = 0x00000010
        hinst: int = ctypes.windll.kernel32.LoadLibraryW(None)
        hicon = user32.LoadImageW(
            hinst, os.path.abspath(icon_path), 1, 0, 0, lr_loadfromfile
        )
        user32.SendMessageW(hwnd, wm_seticon, icon_small, hicon)
        user32.SendMessageW(hwnd, wm_seticon, icon_big, hicon)
