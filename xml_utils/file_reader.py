import sys


def open_file(path: str) -> str:
    """
    Open a file and return its content
    """
    try:
        with open(path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File {path} non trovato")
        sys.exit(1)
    return content