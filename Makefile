pypi:
	python3 -m pip install --user --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple yerkebulanali-gendiff

install:
	poetry install

config:
	poetry config repositories.yerkebulanali https://test.pypi.org/legacy/

build:
	poetry build

publish:
	poetry publish -r yerkebulanali

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/