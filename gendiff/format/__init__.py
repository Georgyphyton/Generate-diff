from gendiff.format.plain import to_plain
from gendiff.format.stylish import to_stylish
from gendiff.format.jsonf import to_json


def formater(item, format):
    if format == 'stylish':
        return to_stylish(item)
    elif format == 'plain':
        return to_plain(item)
    elif format == 'json':
        return to_json(item)
