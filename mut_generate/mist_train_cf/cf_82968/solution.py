"""
QUESTION:
Create a function named `find_pivot` that takes a list of integers as input and returns the index of the "pivot" element. The pivot element is defined as an element where the sum of all elements to the left is equal to the mean of the elements to the right, and the element itself is a prime number. If no such element exists in the list, the function should return "No pivot found".
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def find_pivot(nums):
    for i in range(len(nums)):
        leftSum = sum(nums[0:i])
        rightMean = sum(nums[i+1:])/len(nums[i+1:]) if len(nums[i+1:])!=0 else 0
        if leftSum == rightMean and is_prime(nums[i]):
            return i
    return "No pivot found"