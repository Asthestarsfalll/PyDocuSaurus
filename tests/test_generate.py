import difflib
import os

import pytest

from python_docstring_markdown import crawl


@pytest.fixture(scope="session")
def test_dir():
    """Get the directory containing the test files."""
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def sample_package_dir(test_dir):
    """Get the path to the sample package."""
    return os.path.join(test_dir, "sample_package")


@pytest.fixture(scope="session")
def docs_file(test_dir):
    """Get the path to the documentation file."""
    return os.path.join(test_dir, "data/DOCUMENTATION.md")


@pytest.fixture(scope="session")
def generated_markdown(sample_package_dir, docs_file):
    """Generate and load the documentation content."""
    # Generate the documentation
    content = crawl(sample_package_dir)

    yield content


def test_generated_markdown(generated_markdown, docs_file):
    """Compare generated markdown to expected content in data/DOCUMENTATION.md."""

    with open(docs_file, "r", encoding="utf8") as f:
        expected_content = f.read()

    if generated_markdown != expected_content:
        diff = list(
            difflib.ndiff(
                expected_content.splitlines(keepends=True),
                generated_markdown.splitlines(keepends=True),
            )
        )
        print("".join(diff), end="")
        raise AssertionError("Generated markdown does not match expected content.")
