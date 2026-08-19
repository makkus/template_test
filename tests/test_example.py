"""Example test module for template_test.

This module contains a placeholder test that intentionally fails
to remind developers to implement proper tests.
"""

import pytest

from template_test._version import version


def test_version_exists():
    """Test that the package has a version attribute."""
    assert isinstance(version, str)


def test_todo_implement_tests():
    """Placeholder test that fails to remind developers to implement tests."""
    pytest.fail(
        "TODO: Implement proper tests for template_test!\n"
        "This is a placeholder test that intentionally fails.\n"
        "Replace this with actual tests for your functionality."
    )


def test_sample_fixture(sample_fixture):
    """Example test using a fixture from conftest.py."""
    assert sample_fixture["key"] == "value"
    assert sample_fixture["project"] == "template_test"
