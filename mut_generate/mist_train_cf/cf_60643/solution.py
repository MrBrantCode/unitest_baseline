"""
QUESTION:
Write a function named `lcm_for_list` that calculates the lowest common multiple (LCM) of all integers in an unordered list of n numbers. The function should take a list of integers as input and return the LCM of all numbers in the list. The solution should have a time complexity better than O(n*b), where b is the maximum number in the list.
"""

def gcd(a, b):
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a % b)

def compute_lcm(a, b):
    return (a*b)//gcd(a,b)
  
def lcm_for_list(lst):
    num1 = lst[0]
    num2 = lst[1]
    lcm = compute_lcm(num1, num2)

    for i in range(2, len(lst)):
        lcm = compute_lcm(lcm, lst[i])

    return lcm