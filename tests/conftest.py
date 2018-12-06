import pytest

print("✨✨✨ Loading %s" % __file__)


@pytest.fixture
def fixture_from_root():
    print("\n✨✨✨ Loaded fixture from root")
