"""
QUESTION:
Write a function `find_subset(arr, K)` that returns a subset of the given array `arr` with the maximum possible sum where the subset size is exactly `K` and the difference between the maximum and minimum element in the subset is greater than or equal to 5. The subset must also contain only prime numbers as the maximum and minimum elements. If no such subset exists, return an empty array.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_subset(arr, K):
    arr.sort()
    min_prime = None
    max_prime = None
    
    for num in arr:
        if is_prime(num):
            if min_prime is None:
                min_prime = num
            max_prime = num
    
    if min_prime is None or max_prime is None:
        return []
    
    filtered_arr = [num for num in arr if min_prime <= num <= max_prime]
    
    if len(filtered_arr) < K:
        return []
    
    max_sum = float('-inf')
    max_subset = []
    
    def generate_subset(arr, K, subset, start_idx, cur_sum):
        nonlocal max_sum, max_subset
        
        if len(subset) == K:
            if max(subset) - min(subset) >= 5:
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_subset = subset[:]
            return
        
        for i in range(start_idx, len(arr)):
            generate_subset(arr, K, subset + [arr[i]], i + 1, cur_sum + arr[i])
    
    generate_subset(filtered_arr, K, [], 0, 0)
    
    return max_subset