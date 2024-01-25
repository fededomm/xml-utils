import sys
from bs4 import BeautifulSoup

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
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'xml')

    parent_tags = soup.find_all(parent_tag)
    child_count = 0

    if len(parent_tags) == 0:
        print("Nessun tag {} trovato".format(parent_tag))
        sys.exit(1)

    for parent in parent_tags:
        child_tags = parent.find_all(child_tag)
        child_count += len(child_tags)

    return child_count