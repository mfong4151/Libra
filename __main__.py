#!/usr/bin/python3
from file_parsing.extract import extract_file_body, extract_file_tree
from file_parsing.estimate_tokens import estimate_tokens, warn_excession
from file_parsing.copy_to_clipboard import copy_to_clipboard, get_from_clipboard
from file_parsing.sanitize import sanitze_contents 
from utils.colorize import colorize, CYAN, BOLD, RED
from arg_parser import parser
from display_config.display_config import display_config
from sys import exit
from utils.open_json import open_json
from os import getcwd
from dotenv import load_dotenv

load_dotenv()

##Should be able to support the following flags:
# 1. Optional folder tag, else defaults to cwd
# 2. Tree tag, reveals the file tree
# 3.

CONFIG_PATH = ''

if __name__ == "__main__":
    args = parser.parse_args()
    entry = args.source if args.source else getcwd()
    config = open_json(CONFIG_PATH if CONFIG_PATH else './config.json')
    
    # Gets the child most file path for use in file path namings, we assume the last item is the cwd
    full_file_path    = getcwd()
    shortend_cwd = full_file_path[full_file_path.rfind('/'):]
    file_contents: str = ""
    
    if args.files and not args.sanitize:
        file_contents = extract_file_body(config, shortend_cwd, entry )
        # file_contents = prepare_clipboard(file_contents, args)
        copy_to_clipboard(file_contents)
        num_tokens = estimate_tokens(file_contents)
        warn_excession(num_tokens)
        num_tokens = colorize(f"{CYAN}{BOLD}", num_tokens)
        print(f"Estimated tokens: {num_tokens}")

    if args.sanitize:
        file_contents =  get_from_clipboard()
        
        if not file_contents:
            print(colorize(f"{RED}{BOLD}", "There are no file contents, please copy something to your clipboard and try again.")) 
            exit(1)
        else:
            sanitzed_file_contents = sanitze_contents(config, file_contents)
            copy_to_clipboard(sanitzed_file_contents)
            num_tokens = estimate_tokens(sanitzed_file_contents)
            warn_excession(num_tokens)
            num_tokens = colorize(f"{CYAN}{BOLD}", num_tokens)
            print(f"Estimated tokens: {num_tokens}")
            
    # Handle tree arguments
    if args.tree:
        file_tree = extract_file_tree(config, entry)
        print(file_tree)



