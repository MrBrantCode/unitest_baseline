"""
QUESTION:
You are given the head of a linked list. You have to replace all the values of the nodes with the nearest prime number. If more than one prime number exists at an equal distance, choose the smallest one.
Example 1:
Input:
2 → 6 → 10
Output:
2 → 5 → 11
Explanation:
The nearest prime of 2 is 2 itself.
The nearest primes of 6 are 5 and 7,
since 5 is smaller so, 5 will be chosen.
The nearest prime of 10 is 11.
 
Example 2:
Input:
1 → 15 → 20
Output:
2 → 13 → 19
Explanation:
The nearest prime of 1 is 2.
The nearest primes of 15 are 13 and 17,
since 13 is smaller so, 13 will be chosen.
The nearest prime of 20 is 19.
Your Task:
The task is to complete the function primeList() which contains a reference to the head as the only argument. This function should return the head of the modified linked list.
Expected Time Complexity: O(number of nodes * sqrt(value of node)).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ Number of Nodes ≤ 10^{4}
1 ≤ Value on Node ≤ 10^{4}
"""

from typing import Optional
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def replace_with_nearest_prime(head: Optional[Node]) -> Optional[Node]:
    def newprime(n):
        i = n
        j = n
        while not (isprime(i) or isprime(j)):
            i -= 1
            j += 1
        if isprime(i):
            return i
        return j

    def isprime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    temp = head
    while temp:
        temp.data = newprime(temp.data)
        temp = temp.next
    return head