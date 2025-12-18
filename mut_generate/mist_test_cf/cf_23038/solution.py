"""
QUESTION:
Create a function `countPrimesInRange` that takes two integers `start` and `end` as input and returns the total count of prime numbers found within the range from `start` to `end` (inclusive). The function should have a space complexity of O(1) and optimize for time complexity.
"""

def countPrimesInRange(start, end):
    count = 0

    for num in range(start, end + 1):
        if num < 2 or (num > 2 and num % 2 == 0):
            continue
        
        isPrime = True
        
        for div in range(3, int(num ** 0.5) + 1, 2):
            if num % div == 0:
                isPrime = False
                break
        
        if isPrime:
            count += 1
    
    return count