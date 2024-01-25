import sys
from bs4 import BeautifulSoup
from xml_utils import file_reader

"""
Conta il numero di tag figli con lo stesso nome all'interno di un tag padre
Esempio:
<Parent>
    <Child>...</Child>
    <Child>...</Child>
</Parent>
restituisce il numero totale di tag figli
"""
def count_child_tags(file_path, parent_tag, child_tag) -> int:
    content = file_reader.open_file(file_path)
    soup = BeautifulSoup(content, 'xml')

    parent_tags = soup.find_all(parent_tag)
    child_count = 0

    if len(parent_tags) == 0:
        print(f"Nessun tag {parent_tag} trovato")
        sys.exit(1)

    for parent in parent_tags:
        child_tags = parent.find_all(child_tag)
        child_count += len(child_tags)

    return child_count