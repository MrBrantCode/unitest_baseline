from solution import pandas_to_numpy
### test cases
import unittest
import pandas as pd
import numpy as np

class TestPandasToNumpy(unittest.TestCase):

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame()
        expected_output = np.array([], dtype=object).reshape(0, 0)
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))

    def test_single_element_dataframe(self):
        # Test with a DataFrame containing a single element
        df = pd.DataFrame([[1]])
        expected_output = np.array([[1]])
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))

    def test_dataframe_with_integers(self):
        # Test with a DataFrame containing integer values
        df = pd.DataFrame([[1, 2], [3, 4]])
        expected_output = np.array([[1, 2], [3, 4]])
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))

    def test_dataframe_with_floats(self):
        # Test with a DataFrame containing float values
        df = pd.DataFrame([[1.1, 2.2], [3.3, 4.4]])
        expected_output = np.array([[1.1, 2.2], [3.3, 4.4]])
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))

    def test_dataframe_with_strings(self):
        # Test with a DataFrame containing string values
        df = pd.DataFrame([['a', 'b'], ['c', 'd']])
        expected_output = np.array([['a', 'b'], ['c', 'd']])
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))

    def test_dataframe_with_nan_values(self):
        # Test with a DataFrame containing NaN values
        df = pd.DataFrame([[1, np.nan], [np.nan, 2]])
        expected_output = np.array([[1, np.nan], [np.nan, 2]])
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))

    def test_dataframe_with_mixed_types(self):
        # Test with a DataFrame containing mixed data types
        df = pd.DataFrame([[1, 'b'], ['c', 2]])
        expected_output = np.array([[1, 'b'], ['c', 2]])
        self.assertTrue(np.array_equal(pandas_to_numpy(df), expected_output))  

if __name__ == '__main__':
    unittest.main()
