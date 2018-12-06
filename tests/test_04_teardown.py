import pytest
import pandas as pd

from lib import load_data, transform, delete_data


@pytest.fixture
def data():
    print("\n✨✨✨ setUp")
    yield load_data("dataset_a")
    print("✨✨✨ tearDown")
    delete_data()


def test_output_shape(data):
    print("✨✨✨ Running test_output_shape", end="")
    assert transform(data).shape == (10, 1)


def test_output_type(data):
    print("✨✨✨ Running test_output_type", end="")
    assert isinstance(transform(data), pd.DataFrame)
