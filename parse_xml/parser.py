from os.path import exists
import xml.etree.ElementTree as et

from parse_manual.parsed_function import ParsedFunction
from parse_manual.parsed_class import ParsedClass
from parse_manual.parsed_property import ParsedProperty


def parse(file: str) -> dict:
    result = {}
    element_tree = load_file(file)

    result['functions'] = get_functions(element_tree)
    result['classes'] = get_classes(element_tree)

    return result


def load_file(path: str):
    if exists(path):
        return et.ElementTree(file=path)


def get_functions(element_tree: et.ElementTree):
    # We use the python hashtable (dict) to quickly access the right functions later
    function_dict = {}
    functions = element_tree.findall('func')

    assert id not in function_dict, 'Encountered duplicate function id!'

    for function in functions:
        new_function = process_function(function)
        function_dict[new_function.name] = new_function

    return function_dict


def get_classes(element_tree: et.ElementTree):
    classes_dict = {}
    classes = element_tree.findall('class')

    for current_class in classes:
        new_class = process_class(current_class)
        classes_dict[new_class.name] = new_class

    return classes_dict


def process_function(function_tree) -> ParsedFunction:
    result = ParsedFunction()

    result.name = function_tree.find('id').text
    result.type = function_tree.find('type').text
    result.value = function_tree.find('value').text

    return result


def process_class(cls_tree) -> ParsedClass:
    result = ParsedClass()

    result.name = cls_tree.find('name').text

    meta_class_tree = cls_tree.find('metaclass')

    if meta_class_tree is not None:
        result.meta_class = meta_class_tree.text

    properties = cls_tree.findall('property')

    for current_property in properties:
        new_property = ParsedProperty()
        new_property.name = current_property.find('name').text
        new_property.value = current_property.find('type').text

        result.properties.append(new_property)

    return result