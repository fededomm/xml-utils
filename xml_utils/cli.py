import typer
from xml_utils import count_c_field, count_m_field, vers

app = typer.Typer()

@app.command() 
def cmf(path: str, parent_tag: str, child_tag: str):
    """
    Conta il numero di tag figli con lo stesso nome all'interno di un tag padre
    """
    cmf = count_m_field.count_multiple_field_from_parent(path, parent_tag, child_tag)
    print(f"Numero di tag figli con lo stesso nome maggiori di 1: {cmf}")
    

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