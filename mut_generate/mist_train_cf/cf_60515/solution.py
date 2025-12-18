"""
QUESTION:
Implement a function named `optimized_bubble_sort` that sorts a list of integers in either ascending or descending order. The function takes two parameters: a list of integers (`arr`) and a string (`order`) that determines the order of sorting. The list should have between 1 and 10^3 elements, with values ranging from -10^6 to 10^6. The `order` parameter should be either 'asc' for ascending order or 'desc' for descending order. The function should return a new sorted list without modifying the original list.
"""

from typing import List

def optimized_bubble_sort(arr: List[int], order: str) -> List[int]:
    arr = arr.copy()
    
    for i in range(len(arr)):
        swapped = False  
        
        for j in range(0, len(arr) - i - 1):  
            if (order == 'asc' and arr[j] > arr[j + 1]) or (order == 'desc' and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
                
        if not swapped:  
            break
            
    return arr