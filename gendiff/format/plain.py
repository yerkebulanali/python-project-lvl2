from gendiff import diff


def format(source, indeed=''):
    keys = (diff.ADDED, diff.REMOVED, diff.UPDATED)
    result = ''
    for key, value in tuple(sorted(source.items())):
        if value[0] == diff.NESTED:
            result += format(value[1], indeed=indeed+key+'.')
        elif value[0] != diff.COMMON:
            result += "Property '{}{}' was {}".format(indeed, key, value[0])
            if value[0] == keys[0]:
                if isinstance(value[1], dict):
                    result += " with value: [complex value]\n"
                else:
                    result += " with value: '{}'\n".format(str(value[1]))
            elif value[0] == keys[1]:
                result += "\n"
            elif value[0] == keys[2]:
                new, old = value[1]
                if isinstance(new, dict):
                    new = '[complex value]'
                    result += ". From '{}' to {}\n".format(old, new)
                elif isinstance(old, dict):
                    old = '[complex value]'
                    result += ". From {} to '{}'\n".format(old, new)
                else:
                    result += ". From '{}' to '{}'\n".format(old, new)
    return result[0:-1]
