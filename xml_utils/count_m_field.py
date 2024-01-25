import sys
from bs4 import BeautifulSoup

"""
Conta il numero di tag figli con lo stesso nome
dato un tag padre
Esempio: 

<Parent>
    <Child>...</Child>
    <Child>...</Child>
</Parent>

Restituisce il numero di tag figli supeflui (in questo caso tutti quelli maggiori di 1)
"""
def count_multiple_field_from_parent(file_path, parent_tag, child_tag) -> int:
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'xml')

    parent_tags = soup.find_all(parent_tag)
    if len(parent_tags) == 0:
        print("Nessun tag {} trovato".format(parent_tag))
        sys.exit(1)
    multiple_child_count = 0
    multiple_child_count = iterate_for_child(parent_tags, child_tag, multiple_child_count)
    return multiple_child_count

def iterate_for_child(parent_tags, child_tag, multiple_child_count) -> int:
    for parent in parent_tags:
        child_tags = parent.find_all(child_tag)
        if len(child_tags) > 1:
            multiple_child_count += 1
    return multiple_child_count