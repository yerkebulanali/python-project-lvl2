import json
import yaml
import os


ADDED, REMOVED, UPDATED = 'added', 'removed', 'updated'
COMMON, NESTED = 'common', 'nested'


def load_file(source):
    _, file_type = os.path.splitext(source)
    if file_type in ['.json', '.JSON']:
        return json.load(open(source))
    elif file_type in ['.yml', '.yaml', '.YML', '.YAML']:
        return yaml.safe_load(open(source))
    return None


def generate(source1, source2):
    common = source1.keys() & source2.keys()
    before = source1.keys() - source2.keys()
    after = source2.keys() - source1.keys()
    result = {}
    for key in common:
        source1_value = source1[key]
        source2_value = source2[key]
        if source1_value == source2_value and type(source1_value) != dict:
            result[key] = (COMMON, source1_value)
        else:
            if type(source1_value) == dict and type(source2_value) == dict:
                result[key] = (NESTED, generate(source1_value, source2_value))
            else:
                result[key] = (UPDATED, (source2_value, source1_value))
    for key in before:
        source1_value = source1[key]
        result[key] = (REMOVED, source1_value)
    for key in after:
        source2_value = source2[key]
        result[key] = (ADDED, source2_value)
    return result
