"""
QUESTION:
Implement the function `switch_list(mylist)` that takes a list of positive integers `mylist` as input, where the length of `mylist` does not exceed 10^5, and returns a new list with the odd elements and even elements switched, maintaining the original order. The function should have a time complexity of O(N), where N is the length of the input list.
"""

def switch_list(mylist):
    odd_elements = [x for x in mylist if x % 2 != 0]
    even_elements = [x for x in mylist if x % 2 == 0]
    
    switched_list = []
    for odd, even in zip(odd_elements, even_elements):
        switched_list.append(even)
        switched_list.append(odd)
    
    if len(odd_elements) > len(even_elements):
        switched_list.append(odd_elements[-1])
    
    return switched_list