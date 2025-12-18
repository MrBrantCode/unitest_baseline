"""
QUESTION:
Write a function named `by_length` that takes a list of integers as input and returns a list of strings. The function should first filter out the numbers that are not in the range of 1 to 9. Then, it should sort the remaining numbers in descending order and replace each number with its corresponding word equivalent. If the input list is empty or all numbers are outside the range, the function should return an empty list.
"""

def by_length(arr):
    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    
    valid_nums = sorted([n for n in arr if 1 <= n <= 9], reverse=True)  

    return [num2words[n] for n in valid_nums]