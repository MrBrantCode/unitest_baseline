"""
QUESTION:
Given a linked list and a number k. You have to reverse first part of linked list with k nodes and the second part with n-k nodes.
Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5
k = 2
Output: 2 -> 1 -> 5 -> 4 -> 3
Explanation: As k = 2 , so the first part 2
nodes: 1 -> 2 and the second part with 3 nodes:
3 -> 4 -> 5. Now after reversing the first part: 
2 -> 1 and the second part: 5 -> 4 -> 3.
So the output is: 2 -> 1 -> 5 -> 4 -> 3
Example 2:
Input: 1 -> 2 -> 4 -> 3
k = 3
Output: 4 -> 2 -> 1 -> 3
Explanation: As k = 3 , so the first part 
3 nodes: 4 -> 2 -> 1 and the second part
with 1 nodes: 3. Now after reversing the 
first part: 1 -> 2 -> 4 and the 
second part: 3. So the output is: 1 -> 2 -> 4 -> 3
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which takes head node of the linked list and a integer k as input parameters and returns head node of the linked list after reversing both parts. 
Constraints:
1 <= N <= 10^{5 }
1 <= k < N^{ }
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
"""

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list_parts(head: Optional[Node], k: int) -> Optional[Node]:
    if head is None:
        return None
    
    # Step 1: Traverse the linked list and store the data in a list
    current = head
    data_list = []
    while current is not None:
        data_list.append(current.data)
        current = current.next
    
    # Step 2: Reverse the first k elements and the remaining elements
    first_part = data_list[:k][::-1]
    second_part = data_list[k:][::-1]
    
    # Step 3: Combine the reversed parts
    reversed_data_list = first_part + second_part
    
    # Step 4: Create a new linked list from the reversed data list
    new_head = None
    current = None
    for data in reversed_data_list:
        if new_head is None:
            new_head = Node(data)
            current = new_head
        else:
            current.next = Node(data)
            current = current.next
    
    return new_head