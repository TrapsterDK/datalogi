## How to setup

This project uses [poetry](https://python-poetry.org/) to manage dependencies and virtual environment, and should be installed before continuing. For more information on how to install poetry see the [poetry documentation](https://python-poetry.org/docs/#installation).

To get started with the project clone the repository and run `poetry install` to install dependencies.

Then run `poetry shell` to activate the virtual environment.

The project uses ruff and black for linting and formatting, this should be added to your editor of choice. For more information on how to add these to your editor see the [ruff documentation](https://beta.ruff.rs/docs/editor-integrations/) and [black documentation](https://black.readthedocs.io/en/stable/integrations/editors.html).

nox is used to run tests and linting, this should already be installed with `poetry install`. To run all tests and linting run `nox`. nox commands can also be run individually, for example `nox -s lint` to run linting. To see all available nox commands run `nox --list-sessions`.

To run a python file in the project add a script to the file `pyproject.toml` under `[tool.poetry.scripts]`, then run the script with `poetry run <script-name>`. For more information on how to add scripts see the [poetry documentation](https://python-poetry.org/docs/pyproject/#scripts).
