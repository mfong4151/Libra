import argparse

parser = argparse.ArgumentParser(description="Makes copy pasting file contents for chatGPT easier")
parser.add_argument('--config', '-c', action='store_true', help='Displays the contents of the config file')
# parser.add_argument('--ignore, -i')
parser.add_argument('--source', '-src', help='Determines the folder to use as the entry point, where to start.')
parser.add_argument('--tree', '-t', action='store_true', help='Creates a tree diagram of the file structure.')
parser.add_argument('--files', '-f', action='store_false', help='Disables file copy to clipboard')
parser.add_argument('--gpt', '-g', action='store_true', help='HERE COMES THE BIG DADDY MOVE, LETS GOOOO GPT')