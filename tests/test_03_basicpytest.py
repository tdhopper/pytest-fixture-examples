import pytest
import pandas as pd

from lib import load_data, transform


@pytest.fixture
def data():
    print("\n✨✨✨ setUp")
    return load_data("dataset_a")


def test_output_shape(data):
    assert transform(data).shape == (10, 1)


def test_output_type(data):
    assert isinstance(transform(data), pd.DataFrame)
