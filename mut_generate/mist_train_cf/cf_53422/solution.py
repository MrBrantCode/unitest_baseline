"""
QUESTION:
Write a function `findKthSmallestPrime` that finds the kth smallest prime number in a given array, where k and the array are the function's inputs. The function should run in linear time complexity of O(n), where n is the total number of elements in the array.
"""

def findKthSmallestPrime(arr, k):
    MAX = max(arr)
    
    prime = [True for i in range(MAX + 1)]
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= MAX ):
        if (prime[p] == True):
            for i in range(p * p, MAX+1, p):
                prime[i] = False
        p += 1
     
    prime_numbers = [num for num in arr if prime[num]]
    prime_numbers.sort()

    if len(prime_numbers) < k:
        return "Not enough prime numbers in the array"
    else:
        return prime_numbers[k - 1]