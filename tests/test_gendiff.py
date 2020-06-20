from gendiff import engine
import os

place = 'tests/fixtures/'


def test_answer():
    with open(os.path.join(place, 'test.txt')) as result:
        file = result.read()
        assert engine.transform(engine.generate_diff(
            os.path.join(place, 'before.json'),
            os.path.join(place, 'after.json'))) == file
