"""
QUESTION:
Write a function `relativeSortArray(arr1, arr2)` that sorts the elements of `arr1` based on the relative ordering of items in `arr2`. Elements that don't appear in `arr2` should be placed at the end of `arr1` in ascending order, with even numbers before odd numbers. The function should work under the following constraints: 

- `1 <= arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All the elements of `arr2` are distinct and each `arr2[i]` is in `arr1`.
"""

def relativeSortArray(arr1, arr2):
    count = {num: 0 for num in arr1}
    
    for num in arr1:
        count[num] += 1
    
    res = []
    for num in arr2:
        res += [num] * count[num]
        del count[num]
    
    remaining_evens = sorted(k for k,v in count.items() if k%2 == 0 for _ in range(v))
    remaining_odds = sorted(k for k,v in count.items() if k%2 != 0 for _ in range(v))
    res += remaining_evens + remaining_odds
    
    return res