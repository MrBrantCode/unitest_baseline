"""
QUESTION:
Complete the function `will_it_fly(q, w, z, m)`.

Develop a function to assess if object `q`, a list of integers, can attain flight. To fly, `q` must satisfy the following conditions: 
- be palindromic
- have its elements' sum ≤ maximum permissible weight `w`
- contain exactly `z` smallest unique numbers and `m` largest unique numbers

If `z + m` is greater than the distinct elements in `q`, return `False`.
"""

def will_it_fly(q, w, z, m):
    # Check if the sum of the list's elements is less than or equal to the maximum permissible weight
    if sum(q) > w:
        return False
    
    # Check if the list is palindromic
    if q != q[::-1]:
        return False
    
    # Get the unique elements in the list
    unique_elements = set(q)
    
    # Check if z + m is greater than the distinct elements
    if z + m > len(unique_elements):
        return False
    
    # Sort the unique elements
    sorted_unique_elements = sorted(unique_elements)
    
    # Check if the count of smallest unique numbers is exactly z
    if len(sorted_unique_elements[:z]) != z:
        return False
    
    # Check if the count of largest unique numbers is exactly m
    if len(sorted_unique_elements[-m:]) != m:
        return False
    
    return True