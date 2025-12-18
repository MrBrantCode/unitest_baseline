"""
QUESTION:
Write a function called `merge_sorted_lists` that takes the head nodes of two sorted linked lists as input and returns the head node of a new sorted linked list that contains all the nodes from the input lists. The function should have a time complexity of O(n), where n is the total number of nodes in the input lists, and use constant extra space. The input linked lists are sorted in ascending order and each node contains an integer value and a reference to the next node.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_sorted_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.value <= list2.value:
        result = list1
        list1 = list1.next
    else:
        result = list2
        list2 = list2.next

    current = result

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return result