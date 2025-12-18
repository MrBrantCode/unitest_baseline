"""
QUESTION:
Create a function called `swapElements(lst1, lst2)` that takes two lists of integers as input, aiming to transform the first list into an all-even-numbers list by swapping elements with the second list without changing the total sum of both lists. The function should return "YES" if the transformation is viable and "NO" if not.
"""

def swapElements(lst1, lst2):
    lst1_odd = [i for i in lst1 if i%2 != 0]
    lst2_even = [i for i in lst2 if i%2 == 0]
    
    lst1_even = [i for i in lst1 if i%2 == 0]
    lst2_odd = [i for i in lst2 if i%2 != 0]
    
    for i in range(min(len(lst1_odd), len(lst2_even))):
        lst1_even.append(lst2_even[i])
        lst2_odd.append(lst1_odd[i])
        
    return "YES" if (sum(lst1_even) - sum(lst1_odd)) == (sum(lst2_even) - sum(lst2_odd)) else "NO"