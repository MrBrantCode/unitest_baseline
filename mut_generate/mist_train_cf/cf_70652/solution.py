"""
QUESTION:
Create a function named `sort_function` that takes an input list of integers and a sorting rule function as parameters. The function should sort the input list into two subgroups: one for non-prime numbers and one for prime numbers. The numbers in each subgroup should be sorted based on the provided rule function. The function should return a list containing the sorted subgroups in the order of non-prime numbers followed by prime numbers. The function should also utilize a helper function named `is_prime` to determine the primality of a given number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sort_function(input_list, rule_func):
    prime_list = []
    nonprime_list = []
    for i in input_list:
        if is_prime(i):
            prime_list.append(i)
        else:
            nonprime_list.append(i)
    
    prime_list.sort(key=rule_func)
    nonprime_list.sort(key=rule_func)

    return [nonprime_list, prime_list]