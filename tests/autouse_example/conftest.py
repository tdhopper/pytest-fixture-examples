import pytest


@pytest.fixture(autouse=True)
def autouse_example():
    print("\n✨✨✨ Auto setUp")
    yield
    print("✨✨✨ Auto tearDown")
