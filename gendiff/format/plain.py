def to_plain(lists_of_items):
    def walk(lists, res_key):
        result = []
        for dicts in lists:
            if isinstance(dicts['value'], list):
                result.append(walk(dicts['value'], res_key+dicts['key']+'.'))
            elif dicts['operator'] == 'remove':
                result.append(f"Property '{res_key}{dicts['key']}' was removed")
            elif dicts['operator'] == 'add':
                result.append(f"Property '{res_key}{dicts['key']}' was "
                              f"added with value: {complex(dicts['value'])}")
            elif dicts['operator'] == 'changed':
                result.append(f"Property '{res_key}{dicts['key']}' was updated."
                              f" From {complex(dicts['value'][0])}"
                              f" to {complex(dicts['value'][1])}")
        return '\n'.join(result)
    return walk(lists_of_items, '')


def complex(item):
    if isinstance(item, dict):
        return '[complex value]'
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    return f"'{str(item)}'"
