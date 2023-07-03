from gendiff.format.plain import to_plain
from gendiff.format.stylish import to_stylish


def formater(item, format):
    if format == 'stylish':
        return to_stylish(item)
    elif format == 'plain':
        return to_plain(item)
    raise ValueError(f"Unrecognized formater: {formater}")
