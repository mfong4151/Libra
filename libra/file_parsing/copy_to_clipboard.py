from pyperclip import copy
from typing import List
from utils.colorize import colorize, BOLD, MAGENTA



def copy_to_clipboard(*args:List[str]) -> None:
    formatting = f"{BOLD}{MAGENTA}"
    copy('\n'.join(args))
    print(colorize(formatting, "Your files have been consolidated and copied to the clipboard"))