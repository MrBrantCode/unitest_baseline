"""
QUESTION:
Split a list of integers into two parts, where the first part contains all odd numbers and the second part contains all even numbers, both maintaining their relative order. The function, named `split_odd_even`, should take a list as input and return two lists. It must be implemented in O(n) time complexity. The input list will always have an even number of elements.
"""

def split_odd_even(mylist):
    odd_list = []
    even_list = []
    
    for num in mylist:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
            
    return odd_list, even_list