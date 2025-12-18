"""
QUESTION:
Write a function named `merge_linked_lists` that takes two sorted linked lists as input and returns a new sorted linked list containing all unique elements from both input lists. The function should have a time complexity of O(n log n), where n is the total number of elements in the merged list. The input linked lists are already sorted in ascending order.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_linked_lists(list1, list2):
    # Create a new empty linked list for the merged list
    merged_list = None
    current = None

    # Traverse both linked lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare the values of the two pointers
        if list1.value < list2.value:
            # Add the value from the first list to the merged list
            if merged_list is None:
                merged_list = Node(list1.value)
                current = merged_list
            else:
                current.next = Node(list1.value)
                current = current.next
            list1 = list1.next
        elif list1.value > list2.value:
            # Add the value from the second list to the merged list
            if merged_list is None:
                merged_list = Node(list2.value)
                current = merged_list
            else:
                current.next = Node(list2.value)
                current = current.next
            list2 = list2.next
        else:
            # Add either value to the merged list and move both pointers
            if merged_list is None:
                merged_list = Node(list1.value)
                current = merged_list
            else:
                current.next = Node(list1.value)
                current = current.next
            list1 = list1.next
            list2 = list2.next

    # Add any remaining elements from either list to the merged list
    while list1 is not None:
        current.next = Node(list1.value)
        current = current.next
        list1 = list1.next

    while list2 is not None:
        current.next = Node(list2.value)
        current = current.next
        list2 = list2.next

    return merged_list