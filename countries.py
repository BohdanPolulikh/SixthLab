import xml.etree.ElementTree as ET
from re import findall


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = ET.iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass



governments = set() # множина всіх форм правління
governments_in_great_country = set() # множина форм правління в країнах зі складною назвою
countries = parse_and_remove('mondial-3.0.xml', 'country')

for country in countries:
    governments.add(country.attrib['government'].lower().strip())
    if len(findall(r'\b\w+', country.attrib['name'])) > 1:
        governments_in_great_country.add(country.attrib['government'].lower().strip())

for government in sorted(governments):
    if government == list(sorted(governments))[-1]:
        print(government, end='.\n\n')
    else:
        print(government, end=', ')

for government in sorted(governments_in_great_country):
    if government == list(sorted(governments_in_great_country))[-1]:
        print(government, end='.')
    else:
        print(government, end=', ')



