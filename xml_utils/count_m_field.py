import sys
from bs4 import BeautifulSoup

from utils import file_reader,iterate

"""
Conta il numero di tag figli con lo stesso nome
dato un tag padre
Esempio: 

<Parent>
    <Child>...</Child>
    <Child>...</Child>
</Parent>

Restituisce il numero di tag figli supeflui (in questo caso tutti quelli maggiori di num_of_requested_child)
"""
def count_multiple_field_from_parent(file_path, parent_tag, child_tag, num_of_requested_child) -> int:
    content = file_reader.open_file(file_path)
    soup = BeautifulSoup(content, 'xml')

    parent_tags = soup.find_all(parent_tag)

    if len(parent_tags) == 0:
        print(f"Nessun tag {parent_tag} trovato")
        sys.exit(1)

    multiple_child_count = 0
    multiple_child_count = iterate.iterate_n_check(parent_tags, child_tag, multiple_child_count, num_of_requested_child)
    return multiple_child_count


def count_multiple_fields_from_parent_euals_to(file_path, parent_tag, child_tag, num_of_requested_child) -> int:
    content = file_reader.open_file(file_path)
    soup = BeautifulSoup(content, 'xml')

    parent_tags = soup.find_all(parent_tag)

    if len(parent_tags) == 0:
        print(f"Nessun tag {parent_tag} trovato")
        sys.exit(1)

    multiple_child_count = 0
    multiple_child_count = iterate.iterate_n_check_equals(parent_tags, child_tag, multiple_child_count, num_of_requested_child)
    return multiple_child_count

