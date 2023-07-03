def to_plain(diff):
    def walk(lists, res_key):
        result = []
        for dic in lists:
            if isinstance(dic['value'], list):
                result.append(walk(dic['value'], res_key + dic['key'] + '.'))
            elif dic['operator'] == 'remove':
                result.append(f"Property '{res_key}{dic['key']}' was removed")
            elif dic['operator'] == 'add':
                result.append(f"Property '{res_key}{dic['key']}' was "
                              f"added with value: {complex(dic['value'])}")
            elif dic['operator'] == 'changed':
                result.append(f"Property '{res_key}{dic['key']}' was updated."
                              f" From {complex(dic['value'][0])}"
                              f" to {complex(dic['value'][1])}")
        return '\n'.join(result)
    return walk(diff, '')


def complex(item):
    if isinstance(item, dict):
        return '[complex value]'
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    if isinstance(item, int):
        return str(item)
    return f"'{str(item)}'"
