from gendiff.format.plain import format as plain
from gendiff.format.default import format as default
from gendiff.format.json import format as json

PLAIN, DEFAULT, JSON = 'plain', 'default', 'json'


__all__ = ('plain', 'default', 'json')
