from bs4 import BeautifulSoup
from utils.timestamp import current_time
from utils.file_reader import open_file
from utils.write_file import append_to_file
from utils.write_file import write_to_file


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
    content = open_file(file_path)
    soup = BeautifulSoup(content, 'xml')
    elements = soup.find_all(tag)
    for element in elements:
        print(get_xpath(element))

def print_xpath_to_file(file_path, tag, output_file):
    content = open_file(file_path)
    soup = BeautifulSoup(content, 'xml')
    elements = soup.find_all(tag)
    now = current_time()
    write_to_file(output_file,"xpath - "+ now + "\n\n")
    for element in elements:
        xpath = get_xpath(element)
        append_to_file(output_file, xpath + "\n")


