"""
QUESTION:
Create a function called `sum_of_primes_in_linked_list` that takes the head of a singly linked list as input, where each node contains an integer. The function should return the sum of all prime numbers in the linked list. The function should iterate over the linked list and check if each number is a prime number using a helper function `is_prime`, which takes an integer as input and returns `True` if it is a prime number and `False` otherwise. The linked list nodes are defined as objects with an integer `data` attribute and a `next` attribute pointing to the next node in the list.
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

def is_prime(n: int) -> bool:
    if n < 2: 
        return False
    if n == 2: 
        return True  
    if n % 2 == 0: 
        return False
    max_divisor = int(n**0.5)  
    for d in range(3, 1 + max_divisor, 2): 
        if n % d == 0:  
            return False
    return True

def sum_of_primes_in_linked_list(head: Node) -> int:
    sum_of_primes = 0
    current_node = head
    
    while current_node is not None:
        if is_prime(current_node.data):
            sum_of_primes += current_node.data
        current_node = current_node.next
    
    return sum_of_primes