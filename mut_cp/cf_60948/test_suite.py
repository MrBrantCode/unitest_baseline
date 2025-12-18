from solution import optimize_redshift_performance
### test case
import unittest

class TestOptimizeRedshiftPerformance(unittest.TestCase):
    """
    Test cases for the optimize_redshift_performance function.
    """

    def setUp(self):
        """
        Set up the initial state of the cluster dictionary before each test.
        """
        self.cluster = {
            'nodes': 4,
            'compression': None,
            'archive': None
        }

    def test_optimize_redshift_performance(self):
        """
        Test that the function correctly optimizes the Redshift cluster by upscaling,
        implementing columnar compression, and archiving historical data.
        """
        expected_cluster = {
            'nodes': 5,
            'compression': 'columnar',
            'archive': 'historical_data'
        }
        result = optimize_redshift_performance(self.cluster)
        self.assertEqual(result, expected_cluster)

    def test_nodes_increment(self):
        """
        Test that the number of nodes is incremented by one.
        """
        self.cluster['nodes'] = 4
        expected_cluster = {
            'nodes': 5,
            'compression': 'columnar',
            'archive': 'historical_data'
        }
        result = optimize_redshift_performance(self.cluster)
        self.assertEqual(result['nodes'], expected_cluster['nodes'])

    def test_compression_set(self):
        """
        Test that the compression type is set to 'columnar'.
        """
        self.cluster['compression'] = 'none'
        expected_cluster = {
            'nodes': 5,
            'compression': 'columnar',
            'archive': 'historical_data'
        }
        result = optimize_redshift_performance(self.cluster)
        self.assertEqual(result['compression'], expected_cluster['compression'])

    def test_archive_set(self):
        """
        Test that the archive setting is set to 'historical_data'.
        """
        self.cluster['archive'] = 'none'
        expected_cluster = {
            'nodes': 5,
            'compression': 'columnar',
            'archive': 'historical_data'
        }
        result = optimize_redshift_performance(self.cluster)
        self.assertEqual(result['archive'], expected_cluster['archive'])  # Modified here

if __name__ == '__main__':
    unittest.main()
