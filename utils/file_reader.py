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
    except PermissionError:
        print(f"Non hai i permessi per aprire il file {path}")
        sys.exit(1)
    except Exception as e:
        print(f"Errore generico: {e}")
        sys.exit(1)
    except EOFError as eof:
        print(f"Errore EOF: {eof}")
        sys.exit(1)
    return content