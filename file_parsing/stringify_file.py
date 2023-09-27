

def file_attrs(file_path: str, file_body: str):
    return '\n'.join([f"#{file_path}", file_body])


def stringify_file(file_path: str) -> str:

    try:
        with open(file_path, 'r') as file:
            return file_attrs(file_path, file.read())
    except FileNotFoundError:
        return ''
    except Exception as e:
        return ''

