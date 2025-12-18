from solution import mergeTwoLists
### test cases
import unittest

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        # Helper function to create a linked list from a list of values
        def create_linked_list(values):
            dummy = ListNode(0)
            current = dummy
            for value in values:
                current.next = ListNode(value)
                current = current.next
            return dummy.next
        
        # Helper function to convert a linked list to a list of values
        def linked_list_to_list(node):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result
        
        self.create_linked_list = create_linked_list
        self.linked_list_to_list = linked_list_to_list
    
    def test_merge_two_empty_lists(self):
        # Test merging two empty lists
        l1 = self.create_linked_list([])
        l2 = self.create_linked_list([])
        merged_list = mergeTwoLists(l1, l2)
        self.assertEqual(self.linked_list_to_list(merged_list), [])
    
    def test_merge_one_empty_list(self):
        # Test merging one empty list with another non-empty list
        l1 = self.create_linked_list([1, 2, 3])
        l2 = self.create_linked_list([])
        merged_list = mergeTwoLists(l1, l2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 2, 3])
    
    def test_merge_lists_with_same_values(self):
        # Test merging two lists with the same values
        l1 = self.create_linked_list([1, 2, 3])
        l2 = self.create_linked_list([1, 2, 3])
        merged_list = mergeTwoLists(l1, l2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 1, 2, 2, 3, 3])
    
    def test_merge_lists_with_different_values(self):
        # Test merging two lists with different values
        l1 = self.create_linked_list([1, 3, 5])
        l2 = self.create_linked_list([2, 4, 6])
        merged_list = mergeTwoLists(l1, l2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 2, 3, 4, 5, 6])
    
    def test_merge_lists_with_duplicates(self):
        # Test merging two lists with duplicate values
        l1 = self.create_linked_list([1, 1, 2])
        l2 = self.create_linked_list([1, 2, 3])
        merged_list = mergeTwoLists(l1, l2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 1, 1, 2, 2, 3])  # Modified output
    
    def test_merge_lists_with_negative_numbers(self):
        # Test merging two lists with negative numbers
        l1 = self.create_linked_list([-3, -1, 1])
        l2 = self.create_linked_list([-2, 0, 2])
        merged_list = mergeTwoLists(l1, l2)
        self.assertEqual(self.linked_list_to_list(merged_list), [-3, -2, -1, 0, 1, 2])  # Modified output

if __name__ == '__main__':
    unittest.main()
