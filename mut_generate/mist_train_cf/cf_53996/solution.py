"""
QUESTION:
Create a function `classify_numbers` that takes a list of integers as input. The function should return a dictionary where the keys are the input numbers and the values are tuples. The first element of the tuple should be a string describing whether the number is 'Perfect', 'Deficient', or 'Abundant', and the second element should be the abundance of the number. The abundance of a number is the difference between the sum of its proper divisors and the number itself. The function should raise an exception if the input list contains any non-positive numbers. The function should be efficient enough to handle large input lists.
"""

def classify_numbers(lst):
    result = {}
    for n in lst:
        if n <= 0:
            raise Exception("Input list should only contain positive integers")
        else:
            divisors = [1]
            for i in range(2, int(n**.5)+1):
                if n % i == 0:
                    if n // i == i:
                        divisors.append(i)
                    else:
                        divisors.extend([i, n // i])
            if sum(divisors) ==  n:
                result[n] = ('Perfect', 0)
            elif sum(divisors) < n:
                result[n] = ('Deficient', n - sum(divisors))
            else:
                result[n] = ('Abundant', sum(divisors) - n)
    return result