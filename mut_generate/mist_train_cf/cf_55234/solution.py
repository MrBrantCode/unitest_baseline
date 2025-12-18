"""
QUESTION:
Write a function `exchangeDiffNumber` that takes two lists of integers as input and returns a string indicating whether it is possible to exchange an uneven number of elements between them to make the first list a list of even numbers and the second list a list of odd numbers. If the exchange is possible, return "YES", otherwise return "NO Exchange Possible". If either of the input lists is empty, return "Invalid input: One or both vectors are empty".
"""

def exchangeDiffNumber(lst1, lst2):
    # Check for empty lists
    if not lst1 or not lst2:
        return "Invalid input: One or both lists are empty"

    even_count_lst1 = sum(1 for num in lst1 if num % 2 == 0)
    odd_count_lst2 = sum(1 for num in lst2 if num % 2 != 0)

    # if the number of uneven elements in lst1 and lst2 is the same, exchange possible
    if even_count_lst1 == len(lst1) and odd_count_lst2 == len(lst2):
        return "YES"
    elif (even_count_lst1 != len(lst1) and odd_count_lst2 != len(lst2) and 
          (len(lst1) - even_count_lst1) % 2 == 1 and (len(lst2) - odd_count_lst2) % 2 == 1):
        return "YES"

    # if the number of uneven elements in lst1 and lst2 is not the same, exchange not possible
    return "NO Exchange Possible"