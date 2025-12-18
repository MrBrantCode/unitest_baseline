"""
QUESTION:
Find the numbers greater than X and divisible by Z in a list of integers. 

Given a list of integers and two numbers X and Z, return a list of numbers from the input list that are greater than X and divisible by Z. The function should have a time complexity of O(N), where N is the length of the list, and use O(1) extra space, excluding the output list. The list can contain duplicates and the numbers in the list can range from -10^9 to 10^9. The values of X and Z can also range from -10^9 to 10^9.
"""

def entrance(lst, X, Z):
    output = []
    for num in lst:
        if num > X and num % Z == 0:
            output.append(num)
    return output