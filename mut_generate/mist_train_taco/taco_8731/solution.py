"""
QUESTION:
# Task
 Your task is to find the similarity of given sorted arrays `a` and `b`, which is defined as follows: 
 
 you take the number of elements which are present in both arrays and divide it by the number of elements which are present in at least one array.

 It also can be written as a formula `similarity(A, B) = #(A ∩ B) / #(A ∪ B)`, where `#(C)` is the number of elements in C, `∩` is intersection of arrays, `∪` is union of arrays.

 This is known as `Jaccard similarity`.

 The result is guaranteed to fit any floating-point type without rounding.

# Example

 For `a = [1, 2, 4, 6, 7]` and `b = [2, 3, 4, 7]`:
```
elements [2, 4, 7] are present in both arrays;
elements [1, 2, 3, 4, 6, 7] are present in at least one of the arrays.
So the similarity equals to 3 / 6 = 0.5.```

# Input/Output


 - `[input]` integer array `a`

  A `sorted` array of positive integers. 
  
  All elements are `different` and are `less than 100`.
  
  `1 ≤ a.length ≤ 100`


 - `[input]` integer array `b`

  An array in the same format as `a`.


 - `[output]` a float number

  The similarity of the arrays.
  
  ```Haskell
  
  In Haskell the two arrays are passed as a touple.
  ```
"""

def calculate_jaccard_similarity(a: list[int], b: list[int]) -> float:
    """
    Calculate the Jaccard similarity between two sorted arrays of integers.

    The Jaccard similarity is defined as the size of the intersection of the arrays
    divided by the size of the union of the arrays.

    Parameters:
    - a (list[int]): A sorted list of integers.
    - b (list[int]): A sorted list of integers.

    Returns:
    - float: The Jaccard similarity between the two arrays.
    """
    intersection_size = len(set(a) & set(b))
    union_size = len(set(a) | set(b))
    
    if union_size == 0:
        return 0.0  # To handle the case where both arrays are empty
    
    return intersection_size / union_size