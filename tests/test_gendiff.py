import os
import json
from gendiff.generate_diff import generate_diff
from gendiff.format import DEFAULT, PLAIN, JSON


place = './tests/fixtures/'

files = (('before_complex.json', 'after_complex.json',
          PLAIN, 'answer_complex_plain.txt'),
         ('before_complex.yml', 'after_complex.yml',
          PLAIN, 'answer_complex_plain.txt'),
         ('before_simple.json', 'after_simple.json',
          PLAIN, 'answer_simple_plain.txt'),
         ('before_simple.yml', 'after_simple.yml',
          PLAIN, 'answer_simple_plain.txt'),
         ('before_complex.json', 'after_complex.json',
          DEFAULT, 'answer_complex_default.txt'),
         ('before_complex.yml', 'after_complex.yml',
          DEFAULT, 'answer_complex_default.txt'),
         ('before_simple.json', 'after_simple.json',
          DEFAULT, 'answer_simple_default.txt'),
         ('before_simple.yml', 'after_simple.yml',
          DEFAULT, 'answer_simple_default.txt'),)


def test_default_plain():
    for i in files:
        before_file = i[0]
        after_file = i[1]
        format_file = i[2]
        answer_file = i[3]
        with open(os.path.join(place, answer_file)) as result:
            test_file = result.read()
        assert generate_diff(
            os.path.join(place, before_file),
            os.path.join(place, after_file), format_file) == test_file


def test_json():
    with open(os.path.join(place, 'test_json.json')) as result:
        test_file = json.load(result)
    assert json.loads(generate_diff(
        os.path.join(place, 'before_simple.json'),
        os.path.join(place, 'after_simple.json'), JSON)) == test_file
    assert json.loads(generate_diff(
        os.path.join(place, 'before_simple.yml'),
        os.path.join(place, 'after_simple.yml'), JSON)) == test_file
