import pytest

print("✨✨✨ Loading %s" % __file__)


@pytest.fixture
def fixture_from_subdir():
    print("✨✨✨ Loaded fixture from tests/conftest_example")
