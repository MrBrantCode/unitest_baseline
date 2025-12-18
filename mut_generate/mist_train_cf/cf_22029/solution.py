"""
QUESTION:
Find the top k largest numbers in a list of up to 10^6 elements, where duplicates are allowed. The function should have a time complexity of O(n) and cannot use built-in sorting functions or libraries. Implement a function named `find_top_k_largest` that takes a list of numbers and a positive integer k as input and returns a list of the top k largest numbers.
"""

def find_top_k_largest(numbers, k):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    unique_numbers = sorted(list(counts.keys()), reverse=True)
    top_k_largest = []
    for num in unique_numbers:
        if len(top_k_largest) == k:
            break
        count = counts[num]
        if count >= k - len(top_k_largest):
            top_k_largest.extend([num] * (k - len(top_k_largest)))
        else:
            top_k_largest.extend([num] * count)
    return top_k_largest