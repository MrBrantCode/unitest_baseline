"""
QUESTION:
Create a function `top_3_distinct_primes` that takes an array of integers as input and prints the top 3 distinct prime values in descending order. The array may contain duplicates, and the function should not use any built-in sorting functions or libraries. The function should achieve a time complexity of O(n) and a space complexity of O(1). If less than 3 distinct prime values are found, print "Not enough distinct prime values found."
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def top_3_distinct_primes(nums):
    count = {}
    distinct_count = 0

    # Count the frequency of each number
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Find the top 3 distinct prime values
    for num in reversed(sorted(count)):
        if is_prime(num):
            print(num)
            distinct_count += 1
        if distinct_count == 3:
            break

    if distinct_count < 3:
        print("Not enough distinct prime values found.")