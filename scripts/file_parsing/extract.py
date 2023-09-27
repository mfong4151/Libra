from os import listdir, getcwd
from os.path import isfile
from file_parsing.stringify_file import stringify_file
from typing import List



def unpack_config(config) -> List[str]:
    ignored_files = set(config['ignored_files'])
    ignored_folders = set(config['ignored_folders'])

    return ignored_files, ignored_folders


def extract_file_body(config, dir: str = getcwd()) -> str:
    res = []
    ignored_files, ignored_folders = unpack_config(config)
    
    def dfs(dir: str) -> None:
        if isfile(dir):
            contents = stringify_file(dir)
            res.append(contents)
            return

        for file in listdir(dir):
            if file in ignored_files or file in  ignored_folders:
                continue
            dfs(f"{dir}/{file}")
        return

    dfs(dir)
    return "\n\n".join(res)


def create_piped_name(file: str, depth: int) -> str:
    PIPE_T = "├──"
    PIPE_VR = "│  "
    res = []

    for _ in range(depth + 1): 
        res.append(PIPE_VR)
    res.append(PIPE_T)
    res.append(f"{file}/")

    return ''.join(res)

def extract_file_tree(config, dir: str = getcwd) -> str:
    res = [f"{dir}/"]
    ignored_files, ignored_folders = unpack_config(config)

    def dfs(dir: str, depth: int) -> None:
        if isfile(dir):
            return
        
        for file in listdir(dir):
            if file in ignored_files or file in  ignored_folders:
                continue
            
            new_dir = f"{dir}/{file}"
            res.append(create_piped_name(file, depth))            
            dfs(new_dir, depth + 1)
            
        return
    dfs(dir, 0)
    return "\n".join(res)
