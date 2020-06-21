import json
import yaml
import os
place = 'tests/fixtures/'


def common_used(operation, i, file):
    return '{} {}: {}\n'.format(operation, i, file)

def added(before, after, operation):
    result = ''
    keys = after.keys() - before.keys()
    for i in keys:
        result += common_used(operation['add'], i, after[i])
    return result + '}'


def deleted(before, after, operation):
    result = ''
    keys = list(filter(lambda x: x not in list(after.keys()),
                       list(before.keys())))
    for i in keys:
        result += common_used(operation['delete'], i, before[i])
    return result


def keys_same(before, after):
    return list(filter(lambda x: x in list(after.keys()), list(before.keys())))


def same(before, after, operation):
    result = ''
    for i in keys_same(before, after):
        if after[i] == before[i]:
            result += common_used(operation['same'], i, before[i])
    return '{\n' + result


def changed(before, after, operation):
    result = ''
    for i in keys_same(before, after):
        if after[i] != before[i]:
            result += common_used(operation['add'], i, after[i]) \
                    + common_used(operation['delete'], i, before[i])
    return result


def load_file(path_to_file1, path_to_file2):
    _, file_type = os.path.splitext(path_to_file1)
    if file_type in ['.json', '.JSON']:
        before = json.load(open(path_to_file1))
        after = json.load(open(path_to_file2))
    elif file_type in ['.yml', '.yaml', '.YML', '.YAML']:
        before = yaml.safe_load(open(path_to_file1))
        after = yaml.safe_load(open(path_to_file2))
    return before, after


def generate_diff(path_to_file1, path_to_file2):
    before, after = load_file(path_to_file1, path_to_file2)
    operation = {'same': '   ', 'add': '  +', 'delete': '  -'}
    the_same = same(before, after, operation)
    the_deleted = deleted(before, after, operation)
    the_added = added(before, after, operation)
    the_changed = changed(before, after, operation)
    return the_same, the_changed, the_deleted, the_added


def transform(text):
    return ''.join(text)
