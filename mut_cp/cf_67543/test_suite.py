from solution import compare_lexicographically
import unittest
# This is a placeholder for the actual implementation details

# Test cases
class TestCompareLexicographically(unittest.TestCase):
    def test_entity_set1_comes_first(self):
        # Test case where EntitySet1 comes before EntitySet2 lexicographically
        self.assertEqual(compare_lexicographically(["apple", "banana"], ["cherry", "date"]), "EntitySet1 comes first in lexicographic order.")

    def test_entity_set2_comes_first(self):
        # Test case where EntitySet2 comes before EntitySet1 lexicographically
        self.assertEqual(compare_lexicographically(["grape", "honeydew"], ["apple", "banana"]), "EntitySet2 comes first in lexicographic order.")

    def test_same_order(self):
        # Test case where both sets are in the same lexicographic order
        self.assertEqual(compare_lexicographically(["apple", "banana"], ["apple", "banana"]), "EntitySet1 and EntitySet2 are in the same leicographic order.")

    def test_mixed_case(self):
        # Test case with mixed case letters to ensure correct lexicographic comparison
        self.assertEqual(compare_lexicographically(["Apple", "Banana"], ["apple", "banana"]), "EntitySet1 comes first in lexicographic order.")

    def test_empty_sets(self):
        # Test case with empty sets
        self.assertEqual(compare_lexicographically([], []), "EntitySet1 and EntitySet2 are in the same lexicographic order.")  # Modified output

    def test_single_element_sets(self):
        # Test case with single element sets
        self.assertEqual(compare_lexicographically(["apple"], ["banana"]), "EntitySet1 comes first in lexicographic order.")
        self.assertEqual(compare_lexicographically(["banana"], ["apple"]), "EntitySet2 comes first in lexicographic order.")

if __name__ == '__main__':
    unittest.main()
