"""
QUESTION:
Write a function named `even_odd_count` that takes a list of integers as input and returns a list of pairs, where each pair contains the count of even and odd digits in the corresponding input integer, respectively. The input integers may be positive or negative.
"""

def even_odd_count(nums):
    result = []
    for num in nums:
        num = abs(num)        
        digits = [int(i) for i in str(num)]
        even_count = sum([1 for d in digits if d % 2 == 0])
        odd_count = sum([1 for d in digits if d % 2 != 0])
        result.append([even_count, odd_count])
    return result