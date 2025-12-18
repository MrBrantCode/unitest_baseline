"""
QUESTION:
Write a function that takes two arguments, and returns a new array populated with the elements **that only appear once, in either one array or the other, taken only once**; display order should follow what appears in arr1 first, then arr2: 

```python
hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5]) # [4, 5]
hot_singles(["tartar", "blanket", "cinnamon"], ["cinnamon", "blanket", "domino"]) # ["tartar", "domino"]
hot_singles([77, "ciao"], [78, 42, "ciao"]) # [77, 78, 42]
hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5, 4]) # [4,5]
```

SPECIAL THANKS: @JulianKolbe !
"""

def find_unique_elements(arr1, arr2):
    unique_elements = []
    combined_set = set(arr1) ^ set(arr2)
    
    for element in arr1 + arr2:
        if element in combined_set and element not in unique_elements:
            unique_elements.append(element)
    
    return unique_elements