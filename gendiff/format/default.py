from gendiff import diff


def add_inner_dict(source, indeed):
    result = ''
    for key, values in source.items():
        if isinstance(values, dict):
            result += '    ' * (indeed + 1) + str(key) + ': '
            result += '{' + '\n'
            result += add_inner_dict(values, indeed + 1)
        else:
            result += '    ' * (indeed + 1) + str(key) + ': '
            result += str(values) + '\n'
    result += '    ' * indeed + '}' + '\n'
    return result


def add_dict(operator, key, value, indeed):
    result = '    ' * indeed + operator + key + ': '
    if isinstance(value, dict):
        result += '{' + '\n' + add_inner_dict(value, indeed + 1)
    else:
        result += str(value) + '\n'
    return result


def final_pack(item1, item2, key, indeed):
    result = ''
    if item1 == diff.UPDATED:
        new_value, old_value = item2
        result += add_dict('  - ', key, old_value, indeed)
        result += add_dict('  + ', key, new_value, indeed)
    else:
        if item1 == diff.ADDED:
            result += add_dict('  + ', key, item2, indeed)
        elif item1 == diff.REMOVED:
            result += add_dict('  - ', key, item2, indeed)
        elif item1 == diff.COMMON:
            result += add_dict('    ', key, item2, indeed)
    return result


def format(source, indeed=0):
    result = '{' + '\n'
    for key, value in tuple(sorted(source.items())):
        if value[0] == diff.NESTED:
            result += '    ' * (indeed + 1) + key + ': '
            result += format(value[1], indeed + 1) + '\n'
        else:
            result += final_pack(value[0], value[1], key, indeed)
    if result[-1] != '}':
        result = result + ('    ' * indeed) + '}'
    else:
        result = result + '}'
    return result
