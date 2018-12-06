import pytest
import pandas as pd

from lib import load_data, transform


@pytest.fixture(params=["dataset_a", "dataset_b", "dataset_c"])
def data(request):
    return load_data(request.param)


def test_output_shape(data):
    assert transform(data).shape == (10, 1)
