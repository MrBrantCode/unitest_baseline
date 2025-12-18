"""
QUESTION:
Create a function `modify_list` that takes a list of integers and a dictionary with 'add' and 'subtract' keys as input, and returns a new list of integers. For each integer, if it's even and the 'add' value is prime, add the 'add' value to the integer; if it's odd and the 'subtract' value is prime, subtract the 'subtract' value from the integer. Include a helper function `is_prime` to check if a number is prime.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def modify_list(lst, dic):
    new_lst = []
    for num in lst:
        if num % 2 == 0 and is_prime(dic['add']):
            new_lst.append(num + dic['add'])
        elif num % 2 != 0 and is_prime(dic['subtract']):
            new_lst.append(num - dic['subtract'])
        else: 
            new_lst.append(num)
    return new_lst