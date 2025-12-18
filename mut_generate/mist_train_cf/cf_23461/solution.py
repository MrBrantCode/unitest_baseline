"""
QUESTION:
Write a function named `binToDecimal` that takes a binary number as input and returns its decimal equivalent. The input is a non-negative integer where each digit is either 0 or 1. The function should only use basic arithmetic operations and not rely on built-in binary or decimal conversion functions.
"""

def binToDecimal(num): 
    # Initializing base  
    # value to 1, i.e 2^0 
    base = 1; 
      
    dec_val = 0; 
      
    # Extracting digits of  
    # binary number from   
    # the right most side 
    # and keeping  
    # incrementing the base 
    # by multiply of 2 
    temp = num 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_val += last_digit * base; 
        base = base * 2; 
      
    return dec_val