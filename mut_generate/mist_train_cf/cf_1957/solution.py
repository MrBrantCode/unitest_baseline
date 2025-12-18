"""
QUESTION:
Create a function called "merge_lists" that takes in two lists, "list1" and "list2". If both lists are empty, raise an "EmptyListsException" with the message "Both lists cannot be empty." If only "list1" is empty, raise an "EmptyList1Exception" with the message "List1 cannot be empty." If only "list2" is empty, raise an "EmptyList2Exception" with the message "List2 cannot be empty." Otherwise, return a new list containing elements from both lists without duplicates. The exception classes should be properly defined and inherit from the Exception class.
"""

class EmptyListsException(Exception):
    def __init__(self):
        super().__init__("Both lists cannot be empty.")

class EmptyList1Exception(Exception):
    def __init__(self):
        super().__init__("List1 cannot be empty.")

class EmptyList2Exception(Exception):
    def __init__(self):
        super().__init__("List2 cannot be empty.")

def merge_lists(list1, list2):
    if not list1 and not list2:
        raise EmptyListsException()
    elif not list1:
        raise EmptyList1Exception()
    elif not list2:
        raise EmptyList2Exception()
    
    merged_list = list(set(list1 + list2))
    return merged_list