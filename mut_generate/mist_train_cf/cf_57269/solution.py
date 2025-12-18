"""
QUESTION:
Write a function `arrange_elements(arr)` that takes an array of integers as input and returns `True` if the array can be rearranged such that the elements are sorted, and all prime elements are at even indices and all non-prime elements are at odd indices after rearrangement, with a maximum of 4 swaps. The rearrangement should first sort the elements and then swap the elements at even and odd indices if necessary. The array should be divided into two parts: elements less than the mean and elements greater than or equal to the mean. If the number of elements less than the mean is even, one element from the greater than or equal part should be moved to the less than part. The function should use a helper function `is_prime(n)` to check if a number is prime.
"""

def arrange_elements(arr):
    if not arr:
        return True

    def is_prime(n):
        if n < 2 or n != int(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    swaps = 0
    odd_index = [i for i in range(1, len(arr), 2)]
    mean_arr = sum(arr) / len(arr)
    below_mean_elements = [i for i in arr if i < mean_arr]
    above_mean_elements = [i for i in arr if i >= mean_arr]

    if len(below_mean_elements) % 2 == 0:
        below_mean_elements.append(above_mean_elements.pop(0))

    prime_indices = [i for i in odd_index if is_prime(arr[i])]
    non_prime_indices = [i for i in range(len(arr)) if i not in prime_indices]

    for i in prime_indices:
        if i%2 == 0:
            for j in non_prime_indices:
                if j%2 != 0:
                    arr[i], arr[j] = arr[j] , arr[i]
                    swaps += 1
                    if swaps >= 4: 
                        break
                    if swaps >= 4: 
                        break

    sorted_arr = sorted(below_mean_elements + above_mean_elements)
    return arr == sorted_arr