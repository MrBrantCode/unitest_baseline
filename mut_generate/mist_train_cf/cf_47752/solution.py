"""
QUESTION:
Write a function `find_quad_combinations` that takes an array of integers as input and returns the total quantity of distinct quadruplet combinations within the array that result in a cumulative sum of zero. The array can contain duplicate elements, and the order of the quadruplets does not matter. The function should ignore duplicate quadruplets. The input array can be unsorted, and the function should handle edge cases such as an empty array or an array with less than 4 elements.
"""

def find_quad_combinations(arr):
    n = len(arr)
    res = []
    
    if not arr or n < 4:
        return res
    
    arr.sort()
    
    for i in range(n-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1, n-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            
            k, l = j+1, n-1
            while k < l:
                s = arr[i] + arr[j] + arr[k] + arr[l]

                if s < 0:
                    k += 1
                elif s > 0:
                    l -= 1
                else:
                    res.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1

    return len(res)