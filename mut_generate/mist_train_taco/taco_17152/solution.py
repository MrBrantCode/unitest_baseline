"""
QUESTION:
Sort the given Linked List using quicksort. which takes O(n^2) time in worst case and O(nLogn) in average and best cases, otherwise you may get TLE.
Input:
In this problem, method takes 1 argument: address of the head of the linked list. The function should not read any input from stdin/console.
The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list.
There are multiple test cases. For each test case, this method will be called individually.
Output:
Set *headRef to head of resultant linked list.
User Task:
The task is to complete the function quickSort() which should set the *headRef to head of the resultant linked list.
Constraints:
1<=T<=100
1<=N<=200
Note: If you use "Test" or "Expected Output Button" use below example format
Example:
Input:
2
3
1 6 2
4
1 9 3 8
Output:
1 2 6
1 3 8 9
Explanation:
Testcase 1: After sorting the nodes, we have 1, 2 and 6.
Testcase 2: After sorting the nodes, we have 1, 3, 8 and 9.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def quick_sort_linked_list(head):
    if head is None or head.next is None:
        return head
    
    pivot = head
    current = head.next
    less_than_pivot = None
    greater_than_pivot = None
    
    while current is not None:
        next_node = current.next
        if current.data < pivot.data:
            current.next = less_than_pivot
            less_than_pivot = current
        else:
            current.next = greater_than_pivot
            greater_than_pivot = current
        current = next_node
    
    less_than_pivot = quick_sort_linked_list(less_than_pivot)
    greater_than_pivot = quick_sort_linked_list(greater_than_pivot)
    
    pivot.next = greater_than_pivot
    
    if less_than_pivot is None:
        return pivot
    
    sorted_head = less_than_pivot
    while less_than_pivot.next is not None:
        less_than_pivot = less_than_pivot.next
    
    less_than_pivot.next = pivot
    return sorted_head