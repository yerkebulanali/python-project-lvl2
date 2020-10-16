import json
import yaml
import os
import argparse
from gendiff import diff
from gendiff import format


def load_file(source):
    _, file_type = os.path.splitext(source)
    if file_type.lower() == '.json':
        return json.load(open(source))
    elif file_type.lower() == '.yml':
        return yaml.safe_load(open(source))
    return None


def generate_diff(old_data, new_data, name=None):
    old_data = load_file(old_data)
    new_data = load_file(new_data)
    if old_data is not None and new_data is not None:
        if name == format.PLAIN:
            return format.plain(diff.generate(old_data, new_data))
        elif name == format.JSON:
            return format.json(diff.generate(old_data, new_data))
        return format.default(diff.generate(old_data, new_data))
    print('Compare yml or json file, please')
    answer = 'Correct name of file: name.json or name.yml'
    return answer


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        default=None,
        help='set format of output'
    )
    args = parser.parse_args()
    return args
