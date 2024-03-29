import argparse

parser = argparse.ArgumentParser(description="Makes copy pasting file contents for chatGPT easier")
parser.add_argument('--config', '-c', action='store_true', help='Displays the contents of the config file')
parser.add_argument('--ignore_files', '-ifi', help="Adds folders to ignore")
parser.add_argument('--ignore_folders', '-ifo', help="Adds folders to ignore")
parser.add_argument('--source', '-src', help='Determines the folder to use as the entry point, where to start.')
parser.add_argument('--tree', '-t', action='store_true', help='Creates a tree diagram of the file structure.')
parser.add_argument('--files', '-f', action='store_false', help='Disables file copy to clipboard')
parser.add_argument('--build', '-b', action='store_true', help='If non-empty, will wrap the file string in a prompt for ChatGPT to build off of') 
parser.add_argument('--errors', '-e', action='store_true', help='If non-empty, will create a prompt for handling errors')
parser.add_argument('--promptify', '-p', action='store_true', help='If non-empty, will wrap the file string in a prompt for ChatGPT to build off of')
parser.add_argument('--gpt', '-g', action='store_true', help='HERE COMES THE BIG DADDY MOVE, LETS GOOOO GPT')
parser.add_argument("--sanitize", "-s", action="store_true", help="Sanitizes and copies items to the clipboard based on the config file.")