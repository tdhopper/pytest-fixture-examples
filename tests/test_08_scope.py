import pytest
import pandas as pd

from lib import load_data, transform


@pytest.fixture(scope="session")
def data():
    print("\n✨✨✨ data setUp")
    yield load_data("dataset_a")
    print("✨✨✨ data tearDown")


def test_output_shape(data):
    assert transform(data).shape == (10, 1)
    print("✨✨✨ Running test_output_shape", end="")


def test_output_type(data):
    assert isinstance(transform(data), pd.DataFrame)
    print("✨✨✨ Running test_output_type", end="")
