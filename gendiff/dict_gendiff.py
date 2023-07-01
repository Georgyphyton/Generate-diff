def dict_diff(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return (dict1, dict2)
    keys = dict1.keys() | dict2.keys()
    result = []
    for key in sorted(keys):
        if key not in dict1:
            result.append({'key': key,
                           'value': dict2[key],
                           'operator': 'add'})
        elif key not in dict2:
            result.append({'key': key,
                           'value': dict1[key],
                           'operator': 'remove'})
        elif dict1[key] == dict2[key]:
            result.append({'key': key,
                           'value': dict1[key],
                           'operator': 'unchanged'})
        else:
            result.append({'key': key,
                           'value': dict_diff(dict1[key], dict2[key]),
                           'operator': 'changed'})
    return result
