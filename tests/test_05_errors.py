import pytest


@pytest.fixture
def bad_fixture():
    return bad_function()


def bad_function():
    undefined


def test_fails():
    bad_function()


def test_errors(bad_fixture):
    bad_fixure

