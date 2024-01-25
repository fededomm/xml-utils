import typer
from xml_utils import count_c_field, count_m_field, vers

app = typer.Typer()

@app.command() 
def cmf(path: str, parent_tag: str, child_tag: str, num_of_requested_child: int):
    """
    Conta il numero di tag figli superflui con lo stesso nome all'interno di un tag padre, dato un numero di tag figli richiesti
    """
    cmf = count_m_field.count_multiple_field_from_parent(path, parent_tag, child_tag, num_of_requested_child)
    cef = count_m_field.count_multiple_fields_from_parent_euals_to(path, parent_tag, child_tag, num_of_requested_child)
    print(f"Numero di tag figli con lo stesso nome maggiori di {num_of_requested_child}: {cmf}")
    print(f"Numero di tag figli con lo stesso nome uguali a {num_of_requested_child}: {cef}")

@app.command()
def ccf(path: str, parent_tag: str, child_tag: str):
    """
    Conta il numero di tag figli con lo stesso nome all'interno di un tag padre
    """
    ccf = count_c_field.count_child_tags(path, parent_tag, child_tag)
    print(f"Numero di tag figli con lo stesso nome: {ccf}")

@app.command(help="Stampa la versione")
def version():
    """
    Stampa la versione
    """
    version = vers.vers()
    print(f"xml_utils version: {version}")