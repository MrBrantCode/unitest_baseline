"""
QUESTION:
Implement a function named `advanced_textual_transformation` that takes an input string. The function should modify the string by swapping the case of alphabetic characters, replacing odd digits with the next prime number, and tripling any special characters. The next prime number is defined as the first prime number that appears immediately after the given digit.
"""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

def next_prime(n): 
    found_prime = False
    number = n
    while not found_prime:
        number += 1
        if is_prime(number):
            found_prime = True
    return number

def advanced_textual_transformation(string: str) -> str:
    transformed_string = ''
    for character in string:
        if character.isalpha():
            transformed_string += character.swapcase()
        elif character.isdigit():
            transformed_string += str(next_prime(int(character))) if int(character)%2 !=0 else character
        else:
            transformed_string += character*3
    return transformed_string