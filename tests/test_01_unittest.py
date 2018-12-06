import unittest
import pandas as pd

from lib import load_data, transform


class TransformTestCase(unittest.TestCase):
    def setUp(self):  # Runs before each test
        print("\n✨✨✨ setUp")
        self.data = load_data("dataset_a")

    def tearDown(self):  # Runs after each test
        print("✨✨✨ tearDown")
        self.data = None

    def test_output_shape(self):  # Uses self.data
        print("✨✨✨ Running test_output_shape")
        self.assertEqual(transform(self.data).shape, (10, 1))

    def test_output_type(self):  # Uses self.widget
        print("✨✨✨ Running test_output_type")
        self.assertTrue(isinstance(transform(self.data), pd.DataFrame))

