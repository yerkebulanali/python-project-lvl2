from gendiff import diff
from gendiff import format


def generate_diff(source1, source2, name=None):
    source1 = diff.load_file(source1)
    source2 = diff.load_file(source2)
    if source1 is not None and source2 is not None:
        if name == format.PLAIN:
            return format.plain(diff.generate(source1, source2))
        elif name == format.JSON:
            return format.json(diff.generate(source1, source2))
        return format.default(diff.generate(source1, source2))
