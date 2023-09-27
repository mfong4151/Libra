from os.path import splitext
TWO_BACKSLASH = set(['.js', '.tsx', '.ts' , '.css', '.cpp'])
HASHTAGS = set(['.py', '.rs'])

def file_attrs(file_path: str, file_body: str):
    _, ext = splitext(file_path)
    comment = '//' if ext in TWO_BACKSLASH else '#'
    return '\n'.join([f"{comment}{file_path}", file_body])


def stringify_file(file_path: str) -> str:

    try:
        with open(file_path, 'r') as file:
            return file_attrs(file_path, file.read())
    except FileNotFoundError:
        return ''
    except Exception as e:
        return ''

