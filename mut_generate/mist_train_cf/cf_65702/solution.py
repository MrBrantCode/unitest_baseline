"""
QUESTION:
Write a function called `prod_signs` that takes an array of non-zero integers as input. The function should return a tuple containing the product of the signs of each distinct integer in the array (represented as 1 for positive and -1 for negative), the sum of the absolute values of each distinct integer, and the count of distinct integers. If the input array is empty, the function should return `None`. The function should ignore zero values and duplicates in the array.
"""

def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        store = set()
        product = 1
        sum_abs = 0
        count = 0
        
        for num in arr:
            if num != 0 and num not in store:
                product *= (1 if num > 0 else -1)
                sum_abs += abs(num)
                count += 1
                store.add(num)
                
        return product, sum_abs, count