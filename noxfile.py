"""Nox sessions."""

from pathlib import Path

import nox
from nox_poetry import Session, session

nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["fmt_check", "lint", "type_check", "test"]  # , "docs"]


@session(venv_backend="none")
def python(s: Session) -> None:
    """Run python with the src directory included in PYTHONPATH.

    Args:
        s (Session): Nox session
    """
    # add src to PYTHONPATH so that we can import datalogi
    s.env["PYTHONPATH"] = str(Path.cwd() / "src")
    s.run("python", *s.posargs)


@session(python=["3.11"])
def test(s: Session) -> None:
    """Run the test suite with pytest.

    Args:
        s (Session): Nox session
    """
    s.install(".", "pytest", "pytest-cov")

    files = [f"tests/{arg}" for arg in s.posargs] if s.posargs else ["tests"]

    s.run(
        "python",
        "-m",
        "pytest",
        "--cov=src/datalogi",
        "--cov-report=html",
        "--cov-report=term",
        *files,
    )


# serve pytest coverage report
@session(venv_backend="none")
def cov_serve(s: Session) -> None:
    """Serve the pytest coverage report.

    Args:
        s (Session): Nox session
    """
    s.run("python", "-m", "http.server", "-b", "127.0.0.1", "--directory", "htmlcov")


# For some sessions, set venv_backend="none" to simply execute scripts within the existing Poetry
# environment. This requires that nox is run within `poetry shell` or using `poetry run nox ...`.
@session(venv_backend="none")
def fmt(s: Session) -> None:
    """Format code using ruff and black.

    Args:
        s (Session): Nox session
    """
    s.run("ruff", "check", ".", "--select", "I", "--fix")
    s.run("black", ".")


@session(venv_backend="none")
def fmt_check(s: Session) -> None:
    """Check code formatting using ruff and black.

    Args:
        s (Session): Nox session
    """
    s.run("ruff", "check", ".", "--select", "I")
    s.run("black", "--check", ".")


@session(venv_backend="none")
def lint(s: Session) -> None:
    """Lint code using ruff.

    Args:
        s (Session): Nox session
    """
    s.run("ruff", "check", ".")


@session(venv_backend="none")
def lint_fix(s: Session) -> None:
    """Lint code using ruff and fix issues.

    Args:
        s (Session): Nox session
    """
    s.run("ruff", "check", ".", "--fix")


@session(venv_backend="none")
def type_check(s: Session) -> None:
    """Type check code using mypy.

    Args:
        s (Session): Nox session
    """
    s.run("mypy", "src", "tests", "noxfile.py")


# Environment variable needed for mkdocstrings-python to locate source files.
doc_env = {"PYTHONPATH": "datalogi"}


@session(venv_backend="none")
def docs(s: Session) -> None:
    """Build documentation using mkdocs.

    Args:
        s (Session): Nox session
    """
    s.run("mkdocs", "build", env=doc_env)


@session(venv_backend="none")
def docs_serve(s: Session) -> None:
    """Serve documentation using mkdocs.

    Args:
        s (Session): Nox session
    """
    s.run("mkdocs", "serve", env=doc_env)
