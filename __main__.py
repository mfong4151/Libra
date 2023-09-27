from file_parsing.extract import extract_file_body, extract_file_tree
from file_parsing.estimate_tokens import estimate_tokens, warn_excession
from file_parsing.copy_to_clipboard import copy_to_clipboard
from utils.colorize import colorize, CYAN, BOLD
from arg_parser import parser
from display_config.display_config import display_config
from sys import exit
from utils.open_json import open_json
from os import getcwd
from dotenv import load_dotenv
import os

load_dotenv()


##Should be able to support the following flags:
# 1. Optional folder tag, else defaults to cwd
# 2. Tree tag, reveals the file tree
# 3.

CONFIG_PATH = os.getenv('CONFIG_PATH')

if __name__ == "__main__":
    args = parser.parse_args()
    entry = args.source if args.source else getcwd()
    config = open_json(CONFIG_PATH)

    if args.config:
        display_config(config)
        exit()

    if args.ignore_folders or args.ignore_files: 
        exit()


    if args.files:
        file_contents = extract_file_body(config, entry)
        copy_to_clipboard(file_contents)
        num_tokens = estimate_tokens(file_contents)
        warn_excession(num_tokens)
        num_tokens = colorize(f"{CYAN}{BOLD}", num_tokens)
        print(f"Estimated tokens: {num_tokens}")

    # Handle tree arguments
    if args.tree:
        file_tree = extract_file_tree(config, entry)
        print(file_tree)



