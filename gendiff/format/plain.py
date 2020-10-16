from gendiff import diff


def format(source, indentation=''):
    lines = []
    for key, (status, value) in sorted(source.items()):
        if status == diff.NESTED:
            lines.append(format(value, indentation=indentation+key+'.'))
        else:
            text = "Property '{}{}' was {}".format(indentation, key, status)
            complex = '[complex value]'
            if status == diff.ADDED:
                if isinstance(value, dict):
                    lines.append("{} with value: {}".format(text, complex))
                else:
                    lines.append("{} with value: '{}'".format(text,
                                                              str(value)))
            elif status == diff.REMOVED:
                lines.append(text)
            elif status == diff.UPDATED:
                new, old = value
                if isinstance(new, dict):
                    lines.append("{}. From '{}' to {}".format(text,
                                                              old, complex))
                elif isinstance(old, dict):
                    lines.append("{}. From {} to '{}'".format(text,
                                                              complex, new))
                else:
                    lines.append("{}. From '{}' to '{}'".format(text,
                                                                old, new))
    return '\n'.join(lines)
