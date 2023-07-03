DEEP = 4


def to_stylish(diff, level=0):
    result = ['{']
    for dicts in diff:
        if dicts['operator'] == 'add':
            result.append(f"{level*' '}  + {dicts['key']}: "
                          f"{dict_to_str(dicts['value'], level+DEEP)}")
        elif dicts['operator'] == 'remove':
            result.append(f"{level*' '}  - {dicts['key']}: "
                          f"{dict_to_str(dicts['value'], level+DEEP )}")
        elif isinstance(dicts['value'], tuple):
            result.append(f"{level*' '}  - {dicts['key']}: "
                          f"{dict_to_str(dicts['value'][0], level+DEEP)}")
            result.append(f"{level*' '}  + {dicts['key']}: "
                          f"{dict_to_str(dicts['value'][1], level+DEEP)}")
        elif dicts['operator'] == 'unchanged':
            result.append(f"{level*' '}    {dicts['key']}: "
                          f"{dict_to_str(dicts['value'], level+DEEP)}")
        else:
            result.append(f"{level*' '}    {dicts['key']}: "
                          f"{to_stylish(dicts['value'], level+DEEP)}")
    return '\n'.join(result) + '\n' + level * ' ' + '}'


def dict_to_str(dicti, level):
    if dicti is None:
        return 'null'
    if isinstance(dicti, bool):
        return str(dicti).lower()
    if not isinstance(dicti, dict):
        return str(dicti)
    end = ' ' * level + '}'
    result = '{\n'
    for key, value in dicti.items():
        result += '{x}{b}: {c}\n'.format(
            x=' ' * (level + DEEP),
            b=key,
            c=dict_to_str(value, level + DEEP)
        )
    return result + end
