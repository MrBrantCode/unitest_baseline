"""
QUESTION:
Create a function called `permute` that generates all permutations of a given array of distinct integers without using library functions. Additionally, create a function called `check_condition` that determines whether all permutations of the array meet the condition where the sum of adjacent numbers is always prime. The `permute` function should call `check_condition` to filter the permutations. The `is_prime` function can be used as a helper function to check if a number is prime.

Note: The `permute` function should take an array and the left and right indices as parameters. The `check_condition` function should take a permutation as a parameter and return a boolean value indicating whether the permutation meets the condition.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_condition(permutation):
    for i in range(len(permutation) - 1):
        if not is_prime(permutation[i] + permutation[i+1]):
            return False
    return True

def permute(arr, l, r):
    if l==r:
        if check_condition(arr):
            print(arr)
    else:
        for i in range(l, r):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            arr[l], arr[i] = arr[i], arr[l] 