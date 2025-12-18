from solution import mutation_summary
### test cases
import unittest
import pandas as pd

class TestMutationSummary(unittest.TestCase):
    def setUp(self):
        # Set up a sample DataFrame for testing
        self.sample_df = pd.DataFrame({
            'mutation_type': ['cpg', 'transition', 'transition', 'transversion', 'transversion'],
            'mutation_rate': [0.1, 0.2, 0.3, 0.4, 0.5]
        })

    def test_total_mutations(self):
        # Test if the total number of mutations is calculated correctly
        result = mutation_summary(self.sample_df)
        self.assertEqual(result['total_mutations'], 5)

    def test_average_mutation_rate(self):
        # Test if the average mutation rate for each type is calculated correctly
        result = mutation_summary(self.sample_df)
        expected_avg_rate = {'cpg': 0.1, 'transition': 0.25, 'transversion': 0.45}
        self.assertDictEqual(result['average_mutation_rate'], expected_avg_rate)

    def test_highest_mutation_rate_type(self):
        # Test if the mutation type with the highest mutation rate is identified correctly
        result = mutation_summary(self.sample_df)
        self.assertEqual(result['highest_mutation_rate_type'], 'transversion')  # Since 0.45 > 0.25 > 0.1

    def test_empty_dataframe(self):
        # Test if the function handles an empty DataFrame correctly
        empty_df = pd.DataFrame(columns=['mutation_type', 'mutation_rate'])
        result = mutation_summary(empty_df)
        self.assertEqual(result['total_mutations'], 0)
        self.assertDictEqual(result['average_mutation_rate'], {})
        self.assertEqual(result['highest_mutation_rate_type'], None)  # Assuming the function returns None for empty data

    def test_single_row_dataframe(self):
        # Test if the function handles a DataFrame with a single row correctly
        single_row_df = pd.DataFrame({'mutation_type': ['cpg'], 'mutation_rate': [0.1]})
        result = mutation_summary(single_row_df)
        self.assertEqual(result['total_mutations'], 1)
        self.assertDictEqual(result['average_mutation_rate'], {'cpg': 0.1})
        self.assertEqual(result['highest_mutation_rate_type'], 'cpg')  # Since there's only one type

if __name__ == '__main__':
    unittest.main()
