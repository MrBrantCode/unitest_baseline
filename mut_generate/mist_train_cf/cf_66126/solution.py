"""
QUESTION:
Create a function named `advanced_sort_multiples_of_three` that takes a list of non-negative integers `l` and an integer `k` as inputs. The function should return the k-th element in the modified list `l`. The list `l` maintains the same elements at indices not divisible by three (considering index starts from 1). At indices divisible by three, the values should correspond to the respective indices of `l`, all sorted in descending order. The function must efficiently handle large numeric arrays and optimize computational complexity. 

The input list `l` contains only non-negative integers and the integer `k` represents the position of the element in the modified list to be returned, considering index starts from 1.
"""

def advanced_sort_multiples_of_three(l: list, k:int) -> int:
    multiples_of_three_indices = [i for i in range(len(l)) if (i+1)%3 == 0]
    multiples_of_three_indices.sort(reverse=True)
    
    for i, index in enumerate(multiples_of_three_indices):
        l[index] = l[i]
    
    return l[k-1]