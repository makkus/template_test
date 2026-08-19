"""Pytest configuration and shared fixtures for template_test tests."""

import pytest


@pytest.fixture
def sample_fixture():
    """Example fixture that can be used across test modules."""
    return {"key": "value", "project": "template_test"}
