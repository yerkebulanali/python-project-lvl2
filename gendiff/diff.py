ADDED, REMOVED, UPDATED = 'added', 'removed', 'updated'
COMMON, NESTED = 'common', 'nested'


def generate(old_data, new_data):
    common = old_data.keys() & new_data.keys()
    before = old_data.keys() - new_data.keys()
    after = new_data.keys() - old_data.keys()
    result = {}
    for key in common:
        old_value = old_data[key]
        new_value = new_data[key]
        if old_value == new_value and type(old_value) != dict:
            result[key] = (COMMON, old_value)
        else:
            if type(old_value) == dict and type(new_value) == dict:
                result[key] = (NESTED, generate(old_value, new_value))
            else:
                result[key] = (UPDATED, (new_value, old_value))
    for key in before:
        old_value = old_data[key]
        result[key] = (REMOVED, old_value)
    for key in after:
        new_value = new_data[key]
        result[key] = (ADDED, new_value)
    return result
