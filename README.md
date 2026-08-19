[![PyPI status](https://img.shields.io/pypi/status/template_test.svg)](https://pypi.python.org/pypi/template_test/)
[![PyPI version](https://img.shields.io/pypi/v/template_test.svg)](https://pypi.python.org/pypi/template_test/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/template_test.svg)](https://pypi.python.org/pypi/template_test/)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fmakkus%template_test%2Fbadge%3Fref%3Ddevelop&style=flat)](https://actions-badge.atrox.dev/makkus/template_test/goto?ref=develop)
[![Coverage Status](https://coveralls.io/repos/github/makkus/template_test/badge.svg?branch=develop)](https://coveralls.io/github/makkus/template_test?branch=develop)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# template_test

A test project.

 - Documentation: [https://makkus.github.io/template_test](https://makkus.github.io/template_test)
 - Code: [https://github.com/makkus/template_test](https://github.com/makkus/template_test)

## Description

TODO

## Development

### Requirements

- uv ( https://docs.astral.sh/uv/ )
- git
- make (on Linux / Mac OS X -- optional)
- just (optional)

### Check out the source code & enter the project directory

```
git clone https://github.com/makkus/template_test
cd template_test
```

### Running pre-defined development-related tasks (using `just`)

The included `Makefile` file includes some useful tasks that help with development. This requires `uv` and the `make` tool to be
installed, which should be the case for Linux & Mac OS X systems.

- `just tests`: runs all unit tests
- `just test <pattern>`: runs all unit tests whose name matches the given pattern
- `just typecheck`: run type-checker
- `just lint`: run the `ruff` linter on the source code
- `just format`: run the `ruff` formatter on the source code (similar to `black`)

Alternatively, if you don't have the `just` command available, you can use `uv` directly to run those tasks:

- `uv run pytest tests`
- `uv run mypy src/`
- `uv run ruff check --fix src/`
- `uv run ruff format src/`

## Copyright & license

Copyright (c) 2026 - Markus Binsteiner


This project is published under the 0BSD license, for the license text please check the [LICENSE](/LICENSE) file in this repository.
