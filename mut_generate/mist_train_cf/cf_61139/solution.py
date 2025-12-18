"""
QUESTION:
Create a function `filter_and_sum` that takes an array of mixed data types as input, filters out all integers and prime numbers, and returns the filtered array along with the sum of the removed prime numbers. The function should not use any built-in functions for identifying primes. The output should be a dictionary with keys 'filteredArray' and 'sumOfPrimes'.
"""

def filter_and_sum(arr): 
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    filteredArray = []
    sumOfPrimes = 0
    
    for ele in arr:
        if type(ele) != int:
            filteredArray.append(ele)
        elif is_prime(ele):
            sumOfPrimes += ele
        else:
            filteredArray.append(ele)
            
    return { 'filteredArray': filteredArray, 'sumOfPrimes': sumOfPrimes }