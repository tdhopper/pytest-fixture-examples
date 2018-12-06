import pandas as pd
import numpy as np


def load_data(dataset_name=None):
    return pd.DataFrame(np.random.randint(0, 100, size=(10, 1)), columns=list("A"))


def transform(data):
    return data


def delete_data():
    pass
