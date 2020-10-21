import pytest
import os
import json
from gendiff.app import generate_diff
from gendiff import format

place = './tests/fixtures/'

expected_complex_plain = open(os.path.join(place,
                              'answer_complex_plain.txt')).read()
test_complex_plain_js = generate_diff(
    os.path.join(place, 'before_complex.json'),
    os.path.join(place, 'after_complex.json'), format.PLAIN)
test_complex_plain_yml = generate_diff(
    os.path.join(place, 'before_complex.yml'),
    os.path.join(place, 'after_complex.yml'), format.PLAIN)
expected_complex_default = open(os.path.join(place,
                                'answer_complex_default.txt')).read()
test_complex_default_js = generate_diff(
    os.path.join(place, 'before_complex.json'),
    os.path.join(place, 'after_complex.json'), format.DEFAULT)
test_complex_default_yml = generate_diff(
    os.path.join(place, 'before_complex.yml'),
    os.path.join(place, 'after_complex.yml'), format.DEFAULT)
expected_simple_plain = open(os.path.join(place,
                             'answer_simple_plain.txt')).read()
test_simple_plain_js = generate_diff(
    os.path.join(place, 'before_simple.json'),
    os.path.join(place, 'after_simple.json'), format.PLAIN)
test_simple_plain_yml = generate_diff(
    os.path.join(place, 'before_simple.yml'),
    os.path.join(place, 'after_simple.yml'), format.PLAIN)
expected_simple_default = open(os.path.join(place,
                               'answer_simple_default.txt')).read()
test_simple_default_js = generate_diff(
    os.path.join(place, 'before_simple.json'),
    os.path.join(place, 'after_simple.json'), format.DEFAULT)
test_simple_default_yml = generate_diff(
    os.path.join(place, 'before_simple.yml'),
    os.path.join(place, 'after_simple.yml'), format.DEFAULT)


expected_print = open(os.path.join(place,
                                   'answer_print.txt')).read()
test_print = generate_diff(
    os.path.join(place, 'before_simple.jso'),
    os.path.join(place, 'after_simple.json'), format.PLAIN)


@pytest.mark.parametrize("test_input,expected",
                         [(test_complex_plain_js, expected_complex_plain),
                          (test_complex_plain_yml, expected_complex_plain),
                          (test_complex_default_js, expected_complex_default),
                          (test_complex_default_yml, expected_complex_default),
                          (test_simple_plain_js, expected_simple_plain),
                          (test_simple_plain_yml, expected_simple_plain),
                          (test_simple_default_js, expected_simple_default),
                          (test_simple_default_yml, expected_simple_default),
                          (test_print, expected_print)
                          ])
def test(test_input, expected):
    assert test_input == expected


def test_json():
    with open(os.path.join(place, 'test_json.json')) as result:
        test_file = json.load(result)
    assert json.loads(generate_diff(
        os.path.join(place, 'before_simple.json'),
        os.path.join(place, 'after_simple.json'),
        format.JSON)) == test_file
    assert json.loads(generate_diff(
        os.path.join(place, 'before_simple.yml'),
        os.path.join(place, 'after_simple.yml'),
        format.JSON)) == test_file
