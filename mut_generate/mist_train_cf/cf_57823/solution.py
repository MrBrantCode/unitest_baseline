"""
QUESTION:
Create a function named `advanced_case_inversion_and_alteration` that takes a string as input and returns a string where the case of alphabetic characters is inverted, odd numerals are replaced with their immediate descendant primes, and special symbols are tripled.
"""

def advanced_case_inversion_and_alteration(string: str) -> str:
    def get_next_prime(n): 
        def is_prime(num):
            if num <= 1:
                return False
            elif num <= 3:
                return True
            elif num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i = i + 6
            return True

        prime = n
        found = False
        
        while not found:
            prime += 2
            if is_prime(prime):
                found = True
                
        return prime

    result = ""
    for char in string:
        if char.isalpha():   
            if char.isupper():
                result += char.lower() 
            else:
                result += char.upper() 
        elif char.isdigit():  
            num = int(char)
            if num % 2 != 0: 
                result += str(get_next_prime(num)) 
            else:
                result += char 
        else:   
            result += char * 3 
    return result