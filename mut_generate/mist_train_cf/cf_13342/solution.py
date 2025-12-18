"""
QUESTION:
Write a function `add_lists(list1, list2)` that takes two lists of integers, each representing a number with digits in reverse order, and returns a new list representing the sum of these two numbers. Each list will have the same length, and the integers will be in the range 0 to 9. The function should handle carrying over extra digits to the next position.
"""

def add_lists(list1, list2):
    carry = 0
    result = []
    
    for i in range(len(list1)-1, -1, -1):
        sum = list1[i] + list2[i] + carry
        if sum > 9:
            carry = 1
            result.insert(0, sum % 10)
        else:
            carry = 0
            result.insert(0, sum)
    
    if carry == 1:
        result.insert(0, carry)
    
    return result