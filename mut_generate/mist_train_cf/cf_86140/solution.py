"""
QUESTION:
Write a function `prime_digit_finder` that takes a list of integers `num_list` and an integer `k` as input, and returns the kth least significant prime digit in the array. The function should consider only the prime digits 2, 3, 5, and 7, and maintain a linear computational complexity of O(n), where n is the total count of elements in the array. If the kth prime digit does not exist, return -1.
"""

def prime_digit_finder(num_list, k):
    count_arr = [0]*10
    prime_digits = [2, 3, 5, 7]

    for num in num_list:
        for digit in str(num):
            count_arr[int(digit)] += 1

    for prime in prime_digits:
        if count_arr[prime] >= k:
            return prime
        else:
            k -= count_arr[prime]  

    return -1  