"""
QUESTION:
Write a function `filter_primes_from_linked_list` that takes the head node of a singly linked list of integers as input. The function should return the head node of a new linked list that contains only the prime numbers from the original list, with no duplicates, in descending order.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes_from_linked_list(head):
    if not head:
        return None
    
    curr = head
    primes = set()
    
    while curr:
        if is_prime(curr.val):
            primes.add(curr.val)
        curr = curr.next
    
    primes = sorted(primes, reverse=True)
    
    if not primes:
        return None
    
    new_head = Node(primes[0])
    curr = new_head
    
    for i in range(1, len(primes)):
        curr.next = Node(primes[i])
        curr = curr.next
    
    return new_head