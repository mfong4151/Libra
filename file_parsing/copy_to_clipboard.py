from pyperclip import copy
from typing import List
from utils.colorize import colorize, BOLD, MAGENTA, RED




# def prepare_clipboard(text: str, args) -> str:
#     if not args.build and not args.promptify:
#         return text

#     if args.build and args.promptify:
#         print(colorize(RED, "You can't use both --build and --promptify at once, creating a promptify string instead"))
#         return create_query_prompt(text)
    
#     if args.build:
#         return create_build_prompt(text)
#     else:
#         return create_query_prompt(text)

def copy_to_clipboard(*args:List[str]) -> None:
    formatting = f"{BOLD}{MAGENTA}"
    copy('\n'.join(args))
    print(colorize(formatting, "Your files have been consolidated and copied to the clipboard"))