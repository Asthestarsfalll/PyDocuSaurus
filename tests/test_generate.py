import os
import pytest
from python_docstring_markdown import crawl


@pytest.fixture(scope='session')
def docs_dir():
    """Get the directory containing the test files."""
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session')
def sample_package_dir(docs_dir):
    """Get the path to the sample package."""
    return os.path.join(docs_dir, 'sample_package')


@pytest.fixture(scope='session')
def docs_file(docs_dir):
    """Get the path to the documentation file."""
    return os.path.join(docs_dir, 'DOCUMENTATION.md')


@pytest.fixture(scope='session')
def documentation(sample_package_dir, docs_file):
    """Generate and load the documentation content.
    
    This fixture:
    1. Generates documentation from the sample package
    2. Writes it to DOCUMENTATION.md
    3. Yields the documentation content
    4. Cleans up the file after all tests are done
    """
    # Generate the documentation
    docs_content = crawl(sample_package_dir)
    
    # Write to file
    with open(docs_file, 'w') as f:
        f.write(docs_content)
    
    yield docs_content
    
    # Cleanup after all tests are done
    if os.path.exists(docs_file):
        os.remove(docs_file)


def test_documentation_file_exists(docs_file, documentation):
    """Test that the documentation file exists and is not empty."""
    assert os.path.exists(docs_file)
    assert os.path.getsize(docs_file) > 0


def test_documentation_contains_all_modules(documentation):
    """Test that all modules are present in the documentation."""
    assert '# `sample_package`' in documentation
    assert '# `core`' in documentation
    assert '# `utils`' in documentation
    assert '# `models`' in documentation


def test_documentation_contains_key_components(documentation):
    """Test that key classes and functions are documented."""
    assert 'DataProcessor' in documentation
    assert 'load_json' in documentation
    assert 'User' in documentation


def test_documentation_contains_docstring_content(documentation):
    """Test that module docstrings are properly included."""
    assert 'Sample package for testing docstring to markdown conversion' in documentation
    assert 'Core functionality module using Google-style docstrings' in documentation
    assert 'Utility functions module using ReST-style docstrings' in documentation