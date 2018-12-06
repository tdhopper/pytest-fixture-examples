import pandas as pd

from lib import load_data, transform


def test_output_shape():
    data = load_data("dataset_a")
    assert transform(data).shape == (10, 1)


def test_output_type():
    data = load_data("dataset_a")
    assert isinstance(transform(data), pd.DataFrame)
