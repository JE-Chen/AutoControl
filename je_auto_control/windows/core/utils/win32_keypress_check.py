import sys

from je_auto_control.utils.je_auto_control_exception.exception_tag import windows_import_error
from je_auto_control.utils.je_auto_control_exception.exceptions import AutoControlException

if sys.platform not in ["win32", "cygwin", "msys"]:
    raise AutoControlException(windows_import_error)

import ctypes


def check_key_is_press(keycode: [int, str]):
    if type(keycode) is int:
        temp = ctypes.windll.user32.GetKeyState(keycode)
    else:
        temp = ctypes.windll.user32.GetKeyState(ord(keycode))
    if temp > 1:
        return True
    return False