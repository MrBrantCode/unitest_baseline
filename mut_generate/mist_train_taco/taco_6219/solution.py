"""
QUESTION:
Given two polynomial numbers represented by a linked list. The task is to complete the function addPolynomial() that adds these lists meaning adds the coefficients who have the same variable powers.
Note:  Given polynomials are sorted in decreasing order of power.
Example 1:
Input:
LinkedList1:  (1,x^{2) }
LinkedList2:  (1,x^{3})
Output:
1x^3 + 1x^2
Explanation: Since, x^{2} and x^{3} both have
different powers as 2 and 3. So, their
coefficient can't be added up.
Example 2:
Input:
LinkedList1:  (1,x^{3}) -> (2,x^{2})
LinkedList2:  (3,x^{3}) -> (4,x^{2})
Output:
4x^3 + 6x^2
Explanation: Since, x^{3} has two different
coefficients as 3 and 1. Adding them up
will lead to 4x^{3}. Also, x^{2} has two
coefficients as 4 and 2. So, adding them
up will give 6x^{2}.
Your Task:
The task is to complete the function addPolynomial() which should add the polynomial with same powers return the required polynomial in decreasing order of the power in the form of a linked list.
Note: Try to solve the question without using any extra space.
Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N, M <= 10^{5}
1 <= x, y <= 10^{6}
"""

class Node:
    def __init__(self, coef, power):
        self.coef = coef
        self.power = power
        self.next = None

def add_polynomials(poly1, poly2):
    res = Node(0, 0)  # Dummy node to simplify the logic
    temp = res
    
    while poly1 and poly2:
        if poly1.power > poly2.power:
            res.next = Node(poly1.coef, poly1.power)
            poly1 = poly1.next
        elif poly1.power < poly2.power:
            res.next = Node(poly2.coef, poly2.power)
            poly2 = poly2.next
        else:
            res.next = Node(poly1.coef + poly2.coef, poly1.power)
            poly1 = poly1.next
            poly2 = poly2.next
        res = res.next
    
    # If there are remaining terms in poly1
    while poly1:
        res.next = Node(poly1.coef, poly1.power)
        poly1 = poly1.next
        res = res.next
    
    # If there are remaining terms in poly2
    while poly2:
        res.next = Node(poly2.coef, poly2.power)
        poly2 = poly2.next
        res = res.next
    
    return temp.next