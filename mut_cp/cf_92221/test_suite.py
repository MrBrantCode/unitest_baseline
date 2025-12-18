from solution import entance
This function uses Floyd's Tortoise and Hare algorithm to detect cycles in O(n) time complexity without using extra space.

### test cases
import unittest

class TestDetectCycle(unittest.TestCase):
    def setUp(self):
        # Helper function to create a linked list with a cycle
        def create_cycle_list(values, cycle_index):
            nodes = [ListNode(val) for val in values]
            head = nodes[0]
            for i in range(len(values) - 1):
                nodes[i].next = nodes[i + 1]
            if cycle_index >= 0 and cycle_index < len(values):
                nodes[cycle_index].next = nodes[0]  # Create a cycle
            return head

        # Helper function to create a linked list without a cycle
        def create_no_cycle_list(values):
            nodes = [ListNode(val) for val in values]
            head = nodes[0]
            for i in range(len(values) - 1):
                nodes[i].next = nodes[i + 1]
            return head

        self.create_cycle_list = create_cycle_list
        self.create_no_cycle_list = create_no_cycle_list

    def test_empty_list(self):
        # Test an empty linked list
        head = self.create_no_cycle_list([])
        self.assertFalse(entance(head))

    def test_single_element_list(self):
        # Test a linked list with a single element
        head = self.create_no_cycle_list([1])
        self.assertFalse(entance(head))

    def test_two_element_list_without_cycle(self):
        # Test a two-element linked list without a cycle
        head = self.create_no_cycle_list([1, 2])
        self.assertFalse(entance(head))

    def test_two_element_list_with_cycle(self):
        # Test a two-element linked list with a cycle
        head = self.create_cycle_list([1, 2], 0)
        self.assertTrue(entance(head))

    def test_three_element_list_without_cycle(self):
        # Test a three-element linked list without a cycle
        head = self.create_no_cycle_list([1, 2, 3])
        self.assertFalse(entance(head))

    def test_three_element_list_with_cycle(self):
        # Test a three-element linked list with a cycle
        head = self.create_cycle_list([1, 2, 3], 1)
        self.assertTrue(entance(head))

    def test_four_element_list_without_cycle(self):
        # Test a four-element linked list without a cycle
        head = self.create_no_cycle_list([1, 2, 3, 4])
        self.assertFalse(entance(head))

    def test_four_element_list_with_cycle(self):
        # Test a four-element linked list with a cycle
        head = self.create_cycle_list([1, 2, 3, 4], 2)
        self.assertTrue(entance(head))

if __name__ == '__main__':
    unittest.main()
