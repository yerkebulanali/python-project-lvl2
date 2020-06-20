import json

place = 'tests/fixtures/'


def added(before, after, operation):
    keys = after.keys() - before.keys()
    for i in keys:
        result = '{} {}: {}\n'.format(operation['add'], i, after[i]) + '}'
        return result


def deleted(before, after, operation):
    keys = list(filter(lambda x: x not in list(after.keys()),
                       list(before.keys())))
    for i in keys:
        result = '{} {}: {}\n'.format(operation['delete'], i, before[i])
        return result


def same(before, after, operation):
    keys = list(filter(lambda x: x in list(after.keys()), list(before.keys())))
    for i in keys:
        if after[i] == before[i]:
            result = '{\n' + '{} {}: {}\n'.format(operation['same'],
                                                  i, before[i])
    return result


def changed(before, after, operation):
    keys = list(filter(lambda x: x in list(after.keys()), list(before.keys())))
    for i in keys:
        result = '{} {}: {}\n'.format(operation['add'], i, after[i])\
                 + '{} {}: {}\n'.format(operation['delete'], i, before[i])
    return result


def generate_diff(path_to_file1, path_to_file2):
    before = json.load(open(path_to_file1))
    after = json.load(open(path_to_file2))
    operation = {'same': '   ', 'add': '  +', 'delete': '  -'}
    the_same = same(before, after, operation)
    the_deleted = deleted(before, after, operation)
    the_changed = changed(before, after, operation)
    the_added = added(before, after, operation)
    return the_same, the_changed, the_deleted, the_added


def transform(text):
    return ''.join(text)
