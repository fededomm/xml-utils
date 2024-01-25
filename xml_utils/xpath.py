from bs4 import BeautifulSoup, Tag
from utils import file_reader

def get_xpath(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if siblings == [child] else f"{child.name}[{siblings.index(child)+1}]"
        )
        child = parent
    components.reverse()
    return '/'+('/'.join(components))

def print_xpath(file_path, tag):
    content = file_reader.open_file(file_path)
    soup = BeautifulSoup(content, 'xml')
    elements = soup.find_all(tag)
    for element in elements:
        print(get_xpath(element))

