from gendiff import diff


def add_inner_dict(source, intentation):
    result = ''
    for key, values in source.items():
        result += '    ' * (intentation + 1) + str(key) + ': '
        if isinstance(values, dict):
            result += '{' + '\n'
            result += add_inner_dict(values, intentation + 1)
        else:
            result += str(values) + '\n'
    result += '    ' * intentation + '}' + '\n'
    return result


def add_value(operator, key, value, intentation):
    result = '    ' * intentation + operator + key + ': '
    if isinstance(value, dict):
        result += '{' + '\n' + add_inner_dict(value, intentation + 1)
    else:
        result += str(value) + '\n'
    return result


def final_pack(status, value, key, intentation):
    result = ''
    if status == diff.UPDATED:
        new_value, old_value = value
        result += add_value('  - ', key, old_value, intentation)
        result += add_value('  + ', key, new_value, intentation)
    elif status == diff.ADDED:
        result += add_value('  + ', key, value, intentation)
    elif status == diff.REMOVED:
        result += add_value('  - ', key, value, intentation)
    else:
        result += add_value('    ', key, value, intentation)
    return result


def format(source, intentation=0):
    result = '{' + '\n'
    for key, (status, value) in sorted(source.items()):
        if status == diff.NESTED:
            result += '    ' * (intentation + 1) + key + ': '
            result += format(value, intentation + 1) + '\n'
        else:
            result += final_pack(status, value, key, intentation)
    if result[-1] != '}':
        result = result + ('    ' * intentation) + '}'
    else:
        result = result + '}'
    return result
